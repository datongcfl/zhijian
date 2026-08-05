"""Pre-commit hook runner for staged Python files."""

from __future__ import annotations

import subprocess
import sys
from typing import Sequence


def _staged_python_files() -> list[str]:
    try:
        result = subprocess.run(
            [
                "git",
                "diff",
                "--cached",
                "--name-only",
                "-z",
                "--diff-filter=ACM",
                "--",
                "*.py",
            ],
            capture_output=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"[-] Unable to list staged Python files: {exc}", file=sys.stderr)
        return []

    names = result.stdout.split(b"\0")
    return [name.decode("utf-8", errors="replace") for name in names if name]


def run(argv: Sequence[str] | None = None) -> int:
    extra_args = list(argv) if argv else []
    print("[*] Running Zhijian on staged Python files...")

    files = _staged_python_files()
    if not files:
        print("[+] No Python files to check")
        return 0

    exit_code = 0
    for file_path in files:
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "zhijian.cli",
                    file_path,
                    "--no-history",
                    "--fail-threshold",
                    "70",
                    *extra_args,
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )
        except subprocess.TimeoutExpired:
            print(f"[-] Zhijian timed out on {file_path}", file=sys.stderr)
            return 1
        if result.returncode != 0:
            exit_code = result.returncode

    if exit_code != 0:
        print("[-] Zhijian failed. Run: zhijian <file> --verbose")
    return exit_code


def main() -> int:
    return run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
