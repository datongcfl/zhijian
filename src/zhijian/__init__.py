"""智检 (Zhijian) - AI 代码质量检测工具

基于 AI-SLOP-Detector 和 sloppylint 合并，专注于检测 AI 生成代码的常见问题。

功能特点：
- 39 个检测规则，覆盖噪音、占位符、幻觉、跨语言泄漏、复杂度、风格等
- 4 维评分引擎 (LDR/ICR/DDC/Purity)
- 插件化架构，易于扩展新的检测规则
- 纯离线运行，无需 API Key
"""

__version__ = "1.0.0"
__author__ = "智检团队"

from zhijian.core import SlopDetector
from zhijian.models import (
    DDCResult,
    FileAnalysis,
    InflationResult,
    LDRResult,
    ProjectAnalysis,
    SlopStatus,
)

__all__ = [
    "SlopDetector",
    "SlopStatus",
    "LDRResult",
    "InflationResult",
    "DDCResult",
    "FileAnalysis",
    "ProjectAnalysis",
]
