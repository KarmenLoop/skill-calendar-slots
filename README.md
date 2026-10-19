# KarmenLoop Calendar Slots

Calendar Slots finds meeting times from the busy intervals you give it. It accounts for meeting length, time zones, and the buffer each person needs.

By [KarmenLoop](https://github.com/KarmenLoop).

[![Release](https://img.shields.io/github/v/release/KarmenLoop/skill-calendar-slots)](https://github.com/KarmenLoop/skill-calendar-slots/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](docs/INPUT.md)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](docs/COMPATIBILITY.md)

[Download](https://github.com/KarmenLoop/skill-calendar-slots/releases) · [Quick start](#quick-start) · [Documentation](#documentation) · [Contribute](CONTRIBUTING.md) · [Contact](https://github.com/KarmenLoop/skill-calendar-slots/issues)

The code is [MIT licensed](LICENSE). The local helper needs Python 3.9 or later, with no subscription or provider API key.

## Introduction

Provide a scheduling window, a duration, and busy intervals with explicit UTC offsets. The helper merges overlaps, applies the buffers, and returns complete slots on a fixed UTC grid. It does not read calendars or book a meeting.

The package includes an agent skill, a local Python helper, example data, and tests. The skill guides the conversation; the helper processes the supplied data.

## Capabilities

- Merge overlapping busy intervals from several calendars.
- Apply buffers and meeting duration.
- Return bounded, reproducible UTC candidate slots.

## Quick start

Requirements: Python 3.9+. Git is needed only for cloning; downloading the release archive also works. On Windows, replace python3 with py -3 if that is your installed launcher.

```sh
git clone https://github.com/KarmenLoop/skill-calendar-slots.git
cd skill-calendar-slots
python3 scripts/run.py --input examples/input.json
python3 -m unittest discover -s tests -v
```

Compare the result with [examples/expected.json](examples/expected.json). For your own data, follow the [input format](docs/INPUT.md). Relative file paths are resolved from the directory where you run the command.

To save a result without overwriting an existing file:

```sh
python3 scripts/run.py --input examples/input.json --output result.json
```

### Install the agent skill

Install it for the agent host you use:

```sh
python3 install.py --host codex
# Alternatives: --host deepseek, --host grok, or --host agents
```

The installer copies the skill into your host's skill directory. It stops if that directory already exists. To choose another location, pass `--destination` with a new directory. Host settings, credentials, permissions, and other skills are left alone.

In Codex, invoke $karmen-calendar-slots. In Grok Build, invoke /karmen-calendar-slots. In another compatible host, select the installed skill by name. Example request:

> Find a few times when everyone is free for a 30-minute meeting.

Refresh your host's skill discovery if needed. See [compatibility and its verification limits](docs/COMPATIBILITY.md).

## How it works

Busy intervals are buffered, clipped, sorted, and merged. A fixed UTC grid yields only complete meetings that do not intersect the merged busy intervals.

The result is JSON, so you can save it or pass it to another tool. Exit code `0` means the helper finished, even when its findings need attention. Exit code `2` means the input or a file operation failed. The helper does not run shell commands from the input or overwrite an existing output file.

## Documentation

- [Agent instructions](SKILL.md): selection, workflow, and completion criteria.
- [Input and output](docs/INPUT.md): fields and complete example.
- [Compatibility](docs/COMPATIBILITY.md): installation targets and host limits.
- [Validation](docs/VALIDATION.md): observed local results and acceptance scenarios.
- [Sources](docs/SOURCES.md): public research references and design decisions.
- [Changelog](CHANGELOG.md): release history.

## Limitations

No recurring-event expansion or timezone-database conversion is included. Inputs must be concrete intervals with offsets. The helper does not reserve a slot.

Examples are synthetic. Local tests establish the covered helper behavior; they do not establish an authenticated provider integration or the quality of every future model response. Tools and account access remain those of the host.

## Contributing

Bug reports, focused improvements, documentation fixes, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), include a sanitized reproduction, and run the tests. Development needs no third-party runtime dependency.

## Support

Use [GitHub Issues](https://github.com/KarmenLoop/skill-calendar-slots/issues) for bugs and feature requests. [SUPPORT.md](SUPPORT.md) explains what to include. Never attach keys, customer records, or private conversations.

## License

Copyright © 2026 KarmenLoop. [MIT](LICENSE) permits commercial use and secondary development under its terms. Third-party services retain their own terms; see [NOTICE.md](NOTICE.md).

## Acknowledgements

This is an independent KarmenLoop implementation. [Research notes](docs/SOURCES.md) identify public design references from the Meta, DeepSeek, and xAI ecosystems as applicable. No upstream code or brand assets are bundled, and no affiliation or endorsement is claimed.

## Contact

[KarmenLoop](https://github.com/KarmenLoop) · [Issues](https://github.com/KarmenLoop/skill-calendar-slots/issues) · [Security reporting](SECURITY.md)
