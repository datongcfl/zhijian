"""MCP server 测试：工具清单与输出大小防护（2026-08-02）。"""

from __future__ import annotations

import io
import json
import sys

from zhijian.mcp.server import MAX_REPORT_CHARS, _cap_text, run_stdio_server


def test_cap_text_keeps_short_text() -> None:
    assert _cap_text("short") == "short"


def test_cap_text_truncates_long_text_with_marker() -> None:
    long_text = "x" * (MAX_REPORT_CHARS + 1000)
    capped = _cap_text(long_text)
    assert len(capped) <= MAX_REPORT_CHARS + 200
    assert "truncated" in capped
    assert f"total {len(long_text)}" in capped


def test_mcp_tools_list_matches_registered_tools(monkeypatch, capsys) -> None:
    """tools/list 必须与真实注册一致：zhijian.scan + zhijian.list_patterns（无 scan_file）。"""
    lines = [
        '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}',
        '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}',
    ]
    monkeypatch.setattr(sys, "stdin", io.StringIO("\n".join(lines)))
    run_stdio_server()
    out = capsys.readouterr().out
    responses = [json.loads(line) for line in out.splitlines() if line.strip()]
    assert len(responses) == 2
    tools = responses[1]["result"]["tools"]
    names = [t["name"] for t in tools]
    assert names == ["zhijian.scan", "zhijian.list_patterns"]
    assert "zhijian.scan_file" not in names
