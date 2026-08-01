# 智检 Agent 协作规则

## 项目定位

`智检` 是本地 AI 代码质量静态分析 CLI 工具，包名与命令入口为 `zhijian`。

## 版本事实

- 版本唯一事实源：项目根目录 `VERSION`。
- `pyproject.toml` 的 `project.version` 与 `src/zhijian/__init__.py` 的 `__version__` 必须与 `VERSION` 保持一致。
- 如果三个来源不一致，先停止发布判断，在报告中列出冲突，不凭记忆选择版本。

## 开工检查

涉及代码修改、审查、发布、报告或数据处理时：

1. 读取 `VERSION`、`AGENTS.md`、`ENGINEERING.md`、`README.md`。
2. 确认本次任务影响的高风险域。
3. 先补或确认负向测试，再改高风险实现。
4. 不删除 `.env`、数据库、缓存库、用户报告、原始样本、备份和归档。

## 高风险域

- HTML、Markdown、JSON、文本报告渲染。
- 用户代码和配置文件解析。
- 路径扫描、ignore/suppression 规则、跨平台路径。
- SQLite 缓存、历史库、遥测队列。
- Git hook、subprocess、外部二进制探测。
- CLI 参数兼容、退出码和 CI gate 行为。

## 证据目录

- 审查、验证和发布证据写入工作区 `_logs/智检/`。
- 报告命名包含日期和版本，例如 `审查报告-YYYYMMDD-vX.Y.Z.md`。

## 完成检查

代码变更完成前至少运行：

```bash
python -m pytest
python -m py_compile src/zhijian/cli.py src/zhijian/core.py src/zhijian/config.py
python -m zhijian.cli --version
python -m zhijian.cli src/zhijian/renderer_html.py --output _tmp_review_report.html --no-history --no-color
```

涉及 CLI 文档、hook、报告或 CI gate 时，补充对应 smoke test。
