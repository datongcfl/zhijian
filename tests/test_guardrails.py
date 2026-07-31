"""Guardrail regression tests for high-risk CLI and report behavior."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from zhijian.cli import main
from zhijian.config import Config
from zhijian.core import SlopDetector
from zhijian.git_integration import GitIntegration
from zhijian.models import DDCResult, FileAnalysis, InflationResult, LDRResult, SlopStatus
from zhijian.renderer_html import generate_html_report


def _minimal_file_analysis(file_path: str) -> FileAnalysis:
    return FileAnalysis(
        file_path=file_path,
        ldr=LDRResult(
            total_lines=1,
            logic_lines=1,
            empty_lines=0,
            ldr_score=1.0,
            grade="S",
        ),
        inflation=InflationResult(
            jargon_count=0,
            avg_complexity=0.0,
            inflation_score=0.0,
            status="clean",
            jargon_found=[],
        ),
        ddc=DDCResult(
            imported=[],
            actually_used=[],
            unused=[],
            fake_imports=[],
            type_checking_imports=[],
            usage_ratio=1.0,
            grade="S",
        ),
        deficit_score=0.0,
        status=SlopStatus.CLEAN,
    )


def test_html_report_escapes_text_report_content() -> None:
    result = _minimal_file_analysis("</pre><script>alert(1)</script>.py")

    html = generate_html_report(result)

    assert "</pre><script>alert(1)</script>.py" not in html
    assert "&lt;/pre&gt;&lt;script&gt;alert(1)&lt;/script&gt;.py" in html


def test_analysis_cache_write_failure_does_not_abort_scan(tmp_path, monkeypatch) -> None:
    source = tmp_path / "sample.py"
    source.write_text("def ok():\n    return 1\n", encoding="utf-8")

    class BrokenCache:
        def __init__(self, *_args, **_kwargs) -> None:
            pass

        def get(self, **_kwargs):
            return None

        def put(self, **_kwargs) -> None:
            raise sqlite3.OperationalError("readonly")

    monkeypatch.setattr("zhijian.core.FileAnalysisCache", BrokenCache)

    result = SlopDetector().analyze_file(str(source))

    assert result.file_path == str(source.resolve())


def test_analysis_cache_init_failure_disables_cache(monkeypatch) -> None:
    class BrokenCache:
        def __init__(self, *_args, **_kwargs) -> None:
            raise sqlite3.OperationalError("readonly")

    monkeypatch.setattr("zhijian.core.FileAnalysisCache", BrokenCache)

    detector = SlopDetector()

    assert detector._analysis_cache is None


def test_pre_commit_hook_uses_current_zhijian_cli(tmp_path, monkeypatch) -> None:
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    monkeypatch.setattr(GitIntegration, "is_git_repo", staticmethod(lambda _path=".": True))

    installed = GitIntegration.install_pre_commit_hook(str(tmp_path))
    hook = (git_dir / "hooks" / "pre-commit").read_text(encoding="utf-8")

    assert installed is True
    assert "zhijian" in hook
    assert "slop-detector --files" not in hook
    assert "--record-history" not in hook
    assert "--fail-on" not in hook


def test_mcp_command_fails_gracefully(capsys) -> None:
    exit_code = main(["mcp"])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert "MCP support is not installed" in captured.err


def test_config_instances_do_not_share_nested_defaults() -> None:
    first = Config()
    second = Config()

    first.config["weights"]["ldr"] = 0.99

    assert second.config["weights"]["ldr"] == 0.40
