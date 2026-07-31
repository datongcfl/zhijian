"""HTML report generation for the SLOP detector CLI."""

from __future__ import annotations

import html

from zhijian.renderer_text import generate_text_report


def generate_html_report(result) -> str:
    """Generate HTML report with proper escaping to prevent XSS."""
    score = getattr(result, "weighted_deficit_score", result.deficit_score)
    text_report = html.escape(generate_text_report(result))

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>智检 - AI 代码质量报告</title>
    <style>
        body {{ font-family: monospace; max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .score {{ font-size: 2em; font-weight: bold; }}
        .clean {{ color: green; }}
        .suspicious {{ color: orange; }}
        .critical {{ color: red; }}
        pre {{ background: #f5f5f5; padding: 15px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>AI Code Quality Report</h1>
    <div class="score">Score: {score:.1f}/100</div>
    <pre>{text_report}</pre>
</body>
</html>"""
    return html_content
