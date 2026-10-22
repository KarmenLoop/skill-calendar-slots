# Calendar Slots · 空闲时段

[English](README.md) | 简体中文

从一组忙碌时间里找出能开会的空档。先合并需要考虑的日历，再设置查询范围和缓冲时间，结果会统一为 UTC，方便核对。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-calendar-slots/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-calendar-slots/issues)

## 能做什么

09:00–12:00 UTC 中有一小时忙碌，样例得到四个 30 分钟空档，truncated 为 false。

工具不连接日历账号，也不预订会议；结果只反映你提供的忙碌区间。

![空闲时段 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-calendar-slots-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-calendar-slots 0.2.1`。09:00–12:00 UTC 中有一小时忙碌，样例得到四个 30 分钟空档，truncated 为 false。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

所有时间戳都要带 UTC 偏移。duration_minutes 是会议时长，step_minutes 是候选起点间隔，buffer_minutes 是忙碌区间前后的缓冲。

合并两个人的忙碌区间，再加 10 分钟缓冲，比较结果。可用 max_slots 限制返回数量；truncated 为 true 表示仍有其他空档。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**能直接预订 Google Calendar 或 Outlook 会议吗？** 不能。需要先导出忙碌时间，实际预订和邀请由另行授权的集成完成。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
