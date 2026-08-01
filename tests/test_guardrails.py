"""Guardrail regression tests for high-risk CLI and report behavior."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from types import SimpleNamespace

from zhijian.cli import main
from zhijian.cli_commands import (
    _resolve_governance_record_path,
    _run_autofix,
    _run_cross_file,
    _run_gate,
    _run_governance,
    _run_js_analysis,
    _run_verify_governance,
)
from zhijian.config import Config
from zhijian.core import SlopDetector
from zhijian.git_integration import GitIntegration
from zhijian.git_hook_runner import run as run_git_hook
from zhijian.ml.pipeline import PipelineReport
from zhijian.ml.scorer import MLScorer, _extract_features_from_analysis
from zhijian.models import (
    DDCResult,
    FileAnalysis,
    InflationResult,
    LDRResult,
    ProjectAnalysis,
    SlopStatus,
)
from zhijian.operations_cleanup import _looks_like_dead_code
from zhijian.patterns.base import Axis, Issue, Severity
from zhijian.prioritization import ProjectPrioritizer
from zhijian.renderer_html import generate_html_report
from zhijian.renderer_rich import _build_single_file_content


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


def _issue(pattern_id: str, severity: Severity = Severity.LOW) -> Issue:
    return Issue(
        pattern_id=pattern_id,
        severity=severity,
        axis=Axis.QUALITY,
        file=Path("sample.py"),
        line=1,
        column=0,
        message=f"{pattern_id} message",
    )


def _minimal_project_analysis(project_path: str = ".") -> ProjectAnalysis:
    file_result = _minimal_file_analysis(str(Path(project_path) / "ok.py"))
    return ProjectAnalysis(
        project_path=project_path,
        total_files=1,
        deficit_files=0,
        clean_files=1,
        avg_deficit_score=0.0,
        weighted_deficit_score=0.0,
        avg_ldr=1.0,
        avg_inflation=0.0,
        avg_ddc=1.0,
        overall_status=SlopStatus.CLEAN,
        file_results=[file_result],
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
    assert "python -m zhijian.git_hook_runner" in hook
    assert "for FILE in" not in hook
    assert "slop-detector --files" not in hook
    assert "--record-history" not in hook
    assert "--fail-on" not in hook


def test_git_hook_runner_handles_nul_separated_staged_filenames(monkeypatch) -> None:
    calls = []

    def fake_run(args, **kwargs):
        calls.append((args, kwargs))
        if args[:3] == ["git", "diff", "--cached"]:
            return SimpleNamespace(stdout=b"normal.py\0dir/space name.py\0")
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr("zhijian.git_hook_runner.subprocess.run", fake_run)
    monkeypatch.setattr("zhijian.git_hook_runner.sys.executable", "python")

    assert run_git_hook([]) == 0

    checked_files = [call[0][3] for call in calls[1:]]
    assert checked_files == ["normal.py", "dir/space name.py"]


def test_git_hook_runner_returns_failed_scan_exit_code(monkeypatch) -> None:
    def fake_run(args, **_kwargs):
        if args[:3] == ["git", "diff", "--cached"]:
            return SimpleNamespace(stdout=b"bad.py\0")
        return SimpleNamespace(returncode=1)

    monkeypatch.setattr("zhijian.git_hook_runner.subprocess.run", fake_run)

    assert run_git_hook([]) == 1


def test_mcp_command_dispatches_to_stdio_server(monkeypatch) -> None:
    from zhijian.mcp import server

    monkeypatch.setattr(server, "run_stdio_server", lambda: 0)

    assert main(["mcp"]) == 0


def test_config_instances_do_not_share_nested_defaults() -> None:
    first = Config()
    second = Config()

    first.config["weights"]["ldr"] = 0.99

    assert second.config["weights"]["ldr"] == 0.40


def test_git_root_with_empty_stdout_is_treated_as_unavailable(monkeypatch) -> None:
    class Result:
        stdout = None

    def fake_run(*_args, **kwargs):
        assert kwargs["encoding"] == "utf-8"
        assert kwargs["errors"] == "replace"
        return Result()

    monkeypatch.setattr("zhijian.prioritization.subprocess.run", fake_run)

    assert ProjectPrioritizer(Config())._resolve_git_root(".") is None


def test_ci_report_smoke_uses_packaged_ci_gate(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "zhijian.cli_analysis._run_analysis_phase",
        lambda _args, _detector: (_minimal_file_analysis("ok.py"), 0.0),
    )

    exit_code = main(["ok.py", "--ci-report", "--json", "--no-history"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert '"verdict": "pass"' in captured.out


def test_operations_commands_smoke_with_lightweight_detector(monkeypatch, tmp_path, capsys) -> None:
    class FakeDetector:
        def __init__(self, config_path=None) -> None:
            self.config = Config(config_path)

        def analyze_project(self, project_path: str) -> ProjectAnalysis:
            return _minimal_project_analysis(project_path)

    monkeypatch.setattr("zhijian.cli.SlopDetector", FakeDetector)

    assert main(["explain", "bare_except", "--json"]) == 0
    assert main(["health", str(tmp_path), "--json"]) == 0
    assert main(["audit", str(tmp_path), "--json"]) == 0
    assert main(["sweep", "dead-code", str(tmp_path), "--json"]) == 0

    output = capsys.readouterr().out
    assert '"command": "health"' in output
    assert '"command": "audit"' in output
    assert '"command": "dead-code"' in output


def test_dead_code_sweep_does_not_treat_todo_in_real_file_as_placeholder(tmp_path) -> None:
    source = tmp_path / "real.py"
    source.write_text(
        "# TODO: tune this later\n\n"
        "def add(left, right):\n"
        "    return left + right\n",
        encoding="utf-8",
    )

    assert _looks_like_dead_code(str(source)) is False


def test_dead_code_sweep_detects_module_that_is_only_placeholders(tmp_path) -> None:
    source = tmp_path / "placeholder.py"
    source.write_text(
        '"""Future integration."""\n\n'
        "def sync_remote():\n"
        "    raise NotImplementedError('todo')\n\n"
        "class Adapter:\n"
        "    def send(self):\n"
        "        pass\n",
        encoding="utf-8",
    )

    assert _looks_like_dead_code(str(source)) is True


def test_ml_scorer_extracts_pattern_features_and_scores() -> None:
    result = _minimal_file_analysis("ml.py")
    result.pattern_issues = [
        _issue("god_function", Severity.HIGH),
        _issue("java_style_getter", Severity.MEDIUM),
        _issue("dead_code", Severity.LOW),
    ]
    result.deficit_score = 42.0

    features = _extract_features_from_analysis(result)

    assert features["pattern_count_high"] == 1.0
    assert features["cross_language_patterns"] == 1.0
    assert features["god_function_count"] == 1.0
    assert features["dead_code_count"] == 1.0

    classifier = SimpleNamespace(
        model_type="fake",
        predict=lambda _features: (0.8, 0.9),
    )
    score = MLScorer(classifier).score(result)

    assert score is not None
    assert score.label == "slop"
    assert score.agreement is True
    assert score.to_dict()["features_used"] == len(features)


def test_rich_single_file_content_includes_patterns_and_ml_score() -> None:
    result = _minimal_file_analysis("rich.py")
    result.status = SlopStatus.SUSPICIOUS
    result.deficit_score = 50.0
    result.pattern_issues = [_issue("dead_code", Severity.HIGH)]
    result.ml_score = SimpleNamespace(
        slop_probability=0.72,
        confidence=0.81,
        model_type="fake",
        agreement=True,
        label="slop",
    )

    content = _build_single_file_content(result)

    assert "Pattern Issues" in content.plain
    assert "dead_code message" in content.plain
    assert "ML Score" in content.plain
    assert "Slop Probability: 72.0%" in content.plain


def test_cli_commands_degrade_cleanly_when_optional_modules_are_missing(
    tmp_path, capsys
) -> None:
    result = _minimal_project_analysis(str(tmp_path))

    _run_autofix(result, dry_run=True)
    _run_cross_file(result)
    _run_governance(str(tmp_path), result)
    verify_code = _run_verify_governance(str(tmp_path))
    _run_js_analysis(str(tmp_path / "none.txt"))

    captured = capsys.readouterr()
    combined = captured.out + captured.err
    assert "Auto-fix support is not installed" in combined
    assert "Cross-file analysis support is not installed" in combined
    assert "Governance support is not installed" in combined
    assert "Governance verification support is not installed" in combined
    assert "No JS/TS files found" in combined
    assert verify_code == 2


def test_cli_gate_prints_project_decision(capsys) -> None:
    result = _minimal_project_analysis(".")

    _run_gate(result)

    output = capsys.readouterr().out
    assert "[Gate Decision]" in output
    assert "Allowed" in output
    assert "AuditHash" in output


def test_resolve_governance_record_path_prefers_project_record(tmp_path) -> None:
    cr_ep = tmp_path / ".cr-ep"
    cr_ep.mkdir()
    record = cr_ep / "governance_record.json"
    record.write_text("{}", encoding="utf-8")

    assert _resolve_governance_record_path(str(tmp_path)) == record
    assert _resolve_governance_record_path(str(record)) == record


def test_ml_pipeline_report_summary_and_dict_are_stable() -> None:
    metrics = SimpleNamespace(accuracy=0.9, precision=0.8, recall=0.7, f1_score=0.75)
    report = PipelineReport(
        n_samples=10,
        n_train=8,
        n_test=2,
        model_type="random_forest",
        metrics={"rf": metrics},
        model_path="models/model.pkl",
        feature_importance=[("ldr_score", 0.42)],
    )

    summary = report.summary()
    payload = report.to_dict()

    assert "[ML Pipeline Report]" in summary
    assert "Saved: models/model.pkl" in summary
    assert payload["metrics"]["rf"]["f1_score"] == 0.75
    assert payload["feature_importance"] == [("ldr_score", 0.42)]
