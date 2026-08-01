# 智检工程规则

## 架构边界

- `cli*.py` 只负责参数、命令分发、输出路由和退出码。
- `core.py` 负责扫描编排，缓存、ML、语言分析等可选能力不得阻塞基础扫描。
- `patterns/` 只放规则检测逻辑；新增规则必须注册并有正反测试。
- `renderer_*` 只做展示，不改变分析结果。
- `config.py` 负责默认配置和用户配置合并，默认配置不得被实例间共享污染。

## 高风险测试门禁

以下变更必须有负向测试：

| 领域 | 必测失败路径 |
|------|--------------|
| HTML 报告 | 恶意文件名、恶意代码片段、规则消息包含 HTML/JS |
| 缓存/历史库 | HOME 只读、数据库只读、数据库损坏、缓存写失败 |
| CLI 参数 | README 示例、旧参数兼容或明确拒绝、退出码 |
| Git hook | 当前命令可执行、失败时阻止提交、无 staged Python 文件时放行 |
| 配置 | 非法权重、嵌套配置实例隔离、缺失配置文件 |
| 文件扫描 | ignore 生效、路径含空格、跨平台路径分隔符 |

## 安全规则

- HTML 输出必须 escape 所有动态文本。
- shell/subprocess 必须使用参数列表，不拼接用户输入命令。
- 缓存、历史、遥测属于辅助能力；失败时记录 warning 并继续核心扫描。
- 不把用户扫描内容、文件路径或代码片段发送到网络，除非用户明确开启并能看到配置。
- 报告中不要泄露 `.env`、密钥、token 或数据库内容。

## 发布前检查

发布前必须通过：

```bash
python -m pytest
python -m py_compile src/zhijian/cli.py src/zhijian/core.py src/zhijian/config.py src/zhijian/renderer_html.py
python -m zhijian.cli --version
python -m zhijian.cli . --project --json --no-history
python -m zhijian.cli src/zhijian/renderer_html.py --output _tmp_review_report.html --no-history --no-color
```

如果任一命令失败，不得发布。
