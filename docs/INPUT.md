# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| window_start/window_end | Offset-aware timestamps; positive interval, at most 31 days. |
| duration_minutes | Positive integer. |
| step_minutes | Optional positive integer, default 15. |
| buffer_minutes | Optional nonnegative integer, default 0. |
| busy | Objects with start and end timestamps; all calendars combined. |

## Example

```json
{
  "window_start": "2026-10-19T09:00:00Z",
  "window_end": "2026-10-19T12:00:00Z",
  "duration_minutes": 30,
  "step_minutes": 30,
  "buffer_minutes": 0,
  "busy": [
    {
      "start": "2026-10-19T10:00:00Z",
      "end": "2026-10-19T11:00:00Z"
    }
  ]
}
```

## Result

slots (start/end UTC), merged_busy, and truncated. Results are capped at 1,000 slots.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
