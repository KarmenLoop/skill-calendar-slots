# 输入与输出

[English](INPUT.md) | 简体中文 · [教程](tutorial.zh-CN.md)

对应 **v0.2.1**。输入为 UTF-8 JSON 对象，最大 10 MiB。支持 --input 文件路径与 --input -；拒绝重复 JSON 键和非有限常量。

| 字段 | 约定 |
| --- | --- |
| window_start / window_end | 带 UTC 偏移的时间戳；正区间，最长 31 天。 |
| duration_minutes | 正整数，会议持续分钟数。 |
| step_minutes | 可选正整数，默认 15，为候选起点间隔。 |
| buffer_minutes | 可选非负整数，默认 0，为忙碌区间缓冲。 |
| busy | 忙碌区间数组，每项有 start 与 end；应包含所有需要考虑的日历。 |
| max_slots | 可选整数 1–1000，默认 1000。只有还存在完整空档时 truncated 才为 true。 |

## 样例

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

[完整预期结果](../examples/expected.json)。JSON 键名保留英文以匹配程序接口；字符串内容使用你的实际记录。退出码 0 代表处理完成，不代表所报告问题已经通过。

## 错误与副作用

工具不联网，不执行提交的命令。只读取输入及约定中明确指出的本地路径；默认向终端输出，只在明确 --output 时写入新文件。无效输入退出码为 2，已有结果文件不覆盖。写入失败可能留下不完整新文件，应先检查。安装是独立的明确操作。
