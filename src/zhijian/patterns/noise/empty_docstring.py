"""噪音检测：空文档字符串检测器

检测空的或占位符文档字符串，例如：
- """"""
- """TODO"""
- """pass"""
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class EmptyDocstring(RegexPattern):
    """检测空的或占位符文档字符串"""

    id = "empty_docstring"
    severity = Severity.MEDIUM
    axis = Axis.NOISE
    message = "Empty or placeholder docstring"
    pattern = re.compile(r'"""(\s*|\s*TODO.*|\s*FIXME.*|\s*pass\s*|\s*\.\.\.\s*)"""', re.IGNORECASE)
