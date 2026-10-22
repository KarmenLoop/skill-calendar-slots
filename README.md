# Calendar Slots

English | [简体中文](README.zh-CN.md)

Find meeting-sized gaps in a set of busy intervals. Bring the calendars together yourself, choose the search window and buffer, and inspect the available slots in UTC.

[Download v0.2.1](https://github.com/KarmenLoop/skill-calendar-slots/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-calendar-slots/issues)

## What it does

The 09:00–12:00 UTC window with 10:00–11:00 busy leaves four 30-minute slots. truncated is false.

There is no calendar account connection or booking action. Returned times describe only the intervals you supplied.

![Calendar Slots sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-calendar-slots-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-calendar-slots 0.2.1`. The 09:00–12:00 UTC window with 10:00–11:00 busy leaves four 30-minute slots. truncated is false.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Give every timestamp an explicit UTC offset. Use duration_minutes for meeting length, step_minutes for start spacing, and buffer_minutes around busy intervals.

Combine two people’s busy intervals, add a 10-minute buffer, and compare the results. Use max_slots to limit output; a true truncated flag means more slots exist.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Can it book Google Calendar or Outlook meetings?** No. Export the relevant busy intervals first. Booking and invitations require a separate authorized integration.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
