import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from run import process
from runtime import load_json

class SkillTests(unittest.TestCase):
    def sample(self):
        return json.loads((ROOT / "examples/input.json").read_text())

    def test_example_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/run.py"), "--input", str(ROOT / "examples/input.json")], cwd=ROOT, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), process(self.sample()))

    def test_invalid_input_does_not_write_output(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder) / "bad.json", Path(folder) / "result.json"
            source.write_text("[]")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/run.py"), "--input", str(source), "--output", str(output)], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(output.exists())

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "result.json"
            output.write_text("keep")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/run.py"), "--input", str(ROOT / "examples/input.json"), "--output", str(output)], cwd=ROOT, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_text(), "keep")

    def test_install_to_temporary_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / "skill"
            command = [sys.executable, str(ROOT / "install.py"), "--destination", str(dest)]
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((dest / "SKILL.md").is_file())
            self.assertTrue((dest / "scripts/run.py").is_file())
            self.assertFalse((dest / ".git").exists())
            example = subprocess.run([sys.executable, str(dest / "scripts/run.py"), "--input", str(dest / "examples/input.json")], cwd=dest, capture_output=True, text=True, timeout=10)
            self.assertEqual(example.returncode, 0, example.stderr)
            second = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertEqual(second.returncode, 2)

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "bad.json"
            source.write_text('{"value":1,"value":2}')
            with self.assertRaises(ValueError):
                load_json(source)


    def test_exact_boundaries_are_available(self):
        slots = process(self.sample())["slots"]
        self.assertEqual(len(slots), 4)
        self.assertEqual(slots[1]["end"], "2026-10-19T10:00:00+00:00")

    def test_naive_time_rejected(self):
        data = self.sample()
        data["window_start"] = "2026-10-19T09:00:00"
        with self.assertRaises(ValueError):
            process(data)

    def test_requested_slot_limit_reports_more_available_times(self):
        data = dict(self.sample(), max_slots=2)
        result = process(data)
        self.assertEqual(len(result['slots']), 2)
        self.assertTrue(result['truncated'])

    def test_exact_slot_limit_is_not_truncated(self):
        result = process(dict(self.sample(), max_slots=4))
        self.assertEqual(len(result['slots']), 4)
        self.assertFalse(result['truncated'])

    def test_slot_limit_must_be_a_bounded_integer(self):
        for value in [0, 1001, True, 1.5]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                process(dict(self.sample(), max_slots=value))

if __name__ == "__main__":
    unittest.main()
