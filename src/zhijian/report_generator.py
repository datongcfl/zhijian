"""智检报告生成器 - 生成 Markdown 格式的扫描报告"""

from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# 严重度 emoji
SEVERITY_EMOJI = {
    "critical": "🔴",
    "high": "🟠",
    "medium": "🟡",
    "low": "🟢",
}

# 状态 emoji
STATUS_EMOJI = {
    "clean": "✅",
    "suspicious": "⚠️",
    "inflated_signal": "🔶",
    "critical_deficit": "🚨",
    "dependency_noise": "📦",
}

# 状态中文标签
STATUS_LABEL = {
    "clean": "CLEAN (健康)",
    "suspicious": "SUSPICIOUS (可疑)",
    "inflated_signal": "INFLATED (有水分)",
    "critical_deficit": "CRITICAL (严重问题)",
    "dependency_noise": "DEP_NOISE (依赖噪音)",
}

# 问题类型说明
PATTERN_DESCRIPTIONS = {
    "phantom_import": "导入了不存在的模块",
    "god_function": "函数太长或太复杂",
    "deep_nesting": "嵌套太深",
    "nested_complexity": "深嵌套+高复杂度",
    "lint_escape": "noqa/type:ignore 注释",
    "global_statement": "使用 global 语句",
    "function_clone_cluster": "克隆函数簇",
    "bare_except": "裸 except 捕获所有异常",
    "pass_placeholder": "空函数占位",
    "empty_except": "空 except 块",
    "todo_comment": "TODO 注释",
    "fixme_comment": "FIXME 注释",
    "hack_comment": "HACK 注释",
    "xxx_comment": "XXX 注释",
    "interface_only_class": "只有接口没有实现的类",
    "exact_duplicate_pair": "完全重复的函数",
    "return_constant_stub": "返回固定值的 stub",
    "return_none_placeholder": "只返回 None 的占位函数",
    "not_implemented": "只抛 NotImplementedError",
    "ellipsis_placeholder": "只有 ... 的占位函数",
    "star_import": "from x import *",
    "mutable_default_arg": "可变默认参数",
    "redundant_comment": "冗余注释",
    "empty_docstring": "空文档字符串",
    "generic_docstring": "无信息量的通用文档",
    "changelog_in_code": "代码中写版本历史",
    "overconfident_comment": "过度自信注释",
    "hedging_comment": "犹豫不决注释",
    "apologetic_comment": "道歉式注释",
    "assumption_comment": "假设性注释",
    "single_method_class": "单方法类",
    "placeholder_variable_naming": "占位符变量名",
    "js_push": "JavaScript .push() 泄漏",
    "java_equals": "Java .equals() 泄漏",
    "ruby_each": "Ruby .each 泄漏",
    "go_println": "Go fmt.Println 泄漏",
    "csharp_length": "C# .Length 泄漏",
    "php_strlen": "PHP strlen 泄漏",
}

# 修复建议
FIX_SUGGESTIONS = {
    "bare_except": {
        "priority": "P0",
        "fix": "改为 `except Exception:` 或捕获具体异常",
    },
    "mutable_default_arg": {
        "priority": "P0",
        "fix": "使用 `None` 作为默认值，在函数体内初始化",
    },
    "nested_complexity": {
        "priority": "P0",
        "fix": "提取子函数、使用 early return、减少嵌套",
    },
    "phantom_import": {
        "priority": "P1",
        "fix": "添加 src 到 packages 配置，或使用相对导入",
    },
    "god_function": {
        "priority": "P1",
        "fix": "拆分为多个职责单一的小函数",
    },
    "deep_nesting": {
        "priority": "P1",
        "fix": "使用 guard clause、提取子函数",
    },
    "global_statement": {
        "priority": "P1",
        "fix": "改为函数参数或类属性",
    },
    "function_clone_cluster": {
        "priority": "P2",
        "fix": "提取公共逻辑到基类或工具函数",
    },
    "pass_placeholder": {
        "priority": "P2",
        "fix": "实现函数或标记为 abstract",
    },
    "empty_except": {
        "priority": "P2",
        "fix": "至少记录日志: `except Exception as e: logger.error(e)`",
    },
}


def generate_markdown_report(data: Dict[str, Any], project_name: str = "") -> str:
    """生成 Markdown 格式的扫描报告。

    Args:
        data: analyze_project() 返回的 ProjectAnalysis 字典
        project_name: 项目名称（可选）

    Returns:
        Markdown 格式的报告字符串
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not project_name:
        project_name = data.get("project_path", "未知项目")

    lines = []
    lines.append(f"# {project_name} - AI 代码质量扫描报告")
    lines.append("")
    lines.append(f"> 扫描时间: {now}")
    lines.append(f"> 扫描工具: 智检 (zhijian) v1.0.0")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === 一、项目概览 ===
    lines.append("## 一、项目概览")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    lines.append(f"| 总文件数 | {data['total_files']} |")
    lines.append(f"| 干净文件 | {data['clean_files']} |")
    lines.append(f"| 问题文件 | {data['deficit_files']} |")
    status = data.get("overall_status", "unknown")
    lines.append(f"| 总体状态 | {STATUS_EMOJI.get(status, '❓')} {STATUS_LABEL.get(status, status)} |")
    lines.append(f"| 平均缺陷分 | {data['avg_deficit_score']:.1f}/100 |")
    lines.append(f"| 加权缺陷分 | {data['weighted_deficit_score']:.1f}/100 |")
    lines.append(f"| LDR (逻辑密度) | {data.get('avg_ldr', 0)*100:.1f}% |")
    lines.append(f"| DDC (依赖使用率) | {data.get('avg_ddc', 0)*100:.1f}% |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === 二、问题类型统计 ===
    issue_counts: Counter = Counter()
    issue_severities: Dict[str, str] = {}
    total_issues = 0

    for f in data.get("file_results", []):
        for issue in f.get("pattern_issues", []):
            issue_counts[issue["pattern_id"]] += 1
            issue_severities[issue["pattern_id"]] = issue["severity"]
            total_issues += 1

    lines.append(f"## 二、问题类型统计 ({total_issues} 个问题)")
    lines.append("")
    lines.append("| 问题类型 | 数量 | 严重度 | 说明 |")
    lines.append("|---------|------|--------|------|")
    for pid, count in issue_counts.most_common():
        sev = issue_severities.get(pid, "medium")
        emoji = SEVERITY_EMOJI.get(sev, "⚪")
        desc = PATTERN_DESCRIPTIONS.get(pid, pid)
        lines.append(f"| {pid} | {count} | {emoji} {sev} | {desc} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === 三、问题文件详细列表 ===
    lines.append("## 三、问题文件详细列表")
    lines.append("")

    sorted_files = sorted(
        [f for f in data.get("file_results", []) if f.get("pattern_issues")],
        key=lambda x: -x.get("deficit_score", 0),
    )

    for f in sorted_files:
        file_path = f.get("file_path", "未知文件")
        status = f.get("status", "unknown")
        emoji = STATUS_EMOJI.get(status, "❓")
        label = STATUS_LABEL.get(status, status)

        lines.append(f"### {emoji} `{file_path}`")
        lines.append("")
        lines.append(f"- **状态**: {label}")
        lines.append(f"- **缺陷分**: {f.get('deficit_score', 0):.1f}/100")
        lines.append(f"- **LDR**: {f.get('ldr', {}).get('ldr_score', 0)*100:.1f}%")
        lines.append(f"- **DDC**: {f.get('ddc', {}).get('usage_ratio', 0)*100:.1f}%")
        lines.append("")

        issues = f.get("pattern_issues", [])
        if issues:
            lines.append("| 行号 | 严重度 | 规则 | 问题描述 |")
            lines.append("|------|--------|------|----------|")
            for issue in issues:
                se = SEVERITY_EMOJI.get(issue["severity"], "⚪")
                msg = issue["message"][:60]
                lines.append(f"| {issue['line']} | {se} {issue['severity']} | {issue['pattern_id']} | {msg} |")
            lines.append("")

    # === 四、修复建议 ===
    lines.append("---")
    lines.append("")
    lines.append("## 四、修复建议")
    lines.append("")

    # 按优先级分组
    p0, p1, p2 = [], [], []
    for pid, count in issue_counts.most_common():
        suggestion = FIX_SUGGESTIONS.get(pid)
        if suggestion:
            item = (pid, count, suggestion["fix"])
            if suggestion["priority"] == "P0":
                p0.append(item)
            elif suggestion["priority"] == "P1":
                p1.append(item)
            else:
                p2.append(item)

    if p0:
        lines.append("### 🔴 P0 (必须修复)")
        lines.append("")
        for i, (pid, count, fix) in enumerate(p0, 1):
            lines.append(f"{i}. **{pid}** ({count}处) — {PATTERN_DESCRIPTIONS.get(pid, pid)}")
            lines.append(f"   - 修复: {fix}")
        lines.append("")

    if p1:
        lines.append("### 🟠 P1 (建议修复)")
        lines.append("")
        for i, (pid, count, fix) in enumerate(p1, 1):
            lines.append(f"{i}. **{pid}** ({count}处) — {PATTERN_DESCRIPTIONS.get(pid, pid)}")
            lines.append(f"   - 修复: {fix}")
        lines.append("")

    if p2:
        lines.append("### 🟡 P2 (可选优化)")
        lines.append("")
        for i, (pid, count, fix) in enumerate(p2, 1):
            lines.append(f"{i}. **{pid}** ({count}处) — {PATTERN_DESCRIPTIONS.get(pid, pid)}")
            lines.append(f"   - 修复: {fix}")
        lines.append("")

    # === 五、评分说明 ===
    lines.append("---")
    lines.append("")
    lines.append("## 五、评分说明")
    lines.append("")
    lines.append("| 维度 | 权重 | 说明 |")
    lines.append("|------|------|------|")
    lines.append("| LDR (逻辑密度) | 40% | 代码行占比，越高越好 |")
    lines.append("| ICR (膨胀检测) | 30% | 注释空话 vs 实际复杂度 |")
    lines.append("| DDC (依赖使用) | 20% | 实际使用的导入占比 |")
    lines.append("| Purity (纯度) | 10% | 严重问题的指数衰减 |")
    lines.append("")
    lines.append("**判定等级**: CLEAN (<30) → SUSPICIOUS (30-50) → INFLATED (50-70) → CRITICAL (≥70)")
    lines.append("")
    lines.append("---")
    lines.append(f"*报告由智检 (zhijian) v1.0.0 自动生成 — {now}*")

    return "\n".join(lines)


def save_report(data: Dict[str, Any], output_path: str, project_name: str = "") -> str:
    """生成并保存报告到文件。

    Args:
        data: analyze_project() 返回的 ProjectAnalysis 字典
        output_path: 输出文件路径
        project_name: 项目名称

    Returns:
        保存的文件路径
    """
    md = generate_markdown_report(data, project_name)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(md, encoding="utf-8")
    return str(path.resolve())
