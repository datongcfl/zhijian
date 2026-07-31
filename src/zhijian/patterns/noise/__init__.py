"""噪音检测模式集合

这些模式检测 AI 生成代码中的噪音问题：
- 冗余注释
- 空文档字符串
- 通用文档字符串
- 版本历史注释
"""

from zhijian.patterns.noise.redundant_comment import RedundantComment
from zhijian.patterns.noise.empty_docstring import EmptyDocstring
from zhijian.patterns.noise.generic_docstring import GenericDocstring
from zhijian.patterns.noise.changelog_comment import ChangelogComment

NOISE_PATTERNS = [
    RedundantComment(),
    EmptyDocstring(),
    GenericDocstring(),
    ChangelogComment(),
]

__all__ = [
    "RedundantComment",
    "EmptyDocstring",
    "GenericDocstring",
    "ChangelogComment",
    "NOISE_PATTERNS",
]
