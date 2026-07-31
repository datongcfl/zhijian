"""风格检测：犹豫不决注释检测器

检测 AI 生成的犹豫不决注释，这类注释暗示代码可能存在问题。
例如：
- # should work
- # hopefully this fixes it
- # probably correct
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class HedgingComment(RegexPattern):
    """检测犹豫不决的注释"""

    id = "hedging_comment"
    severity = Severity.HIGH
    axis = Axis.STYLE
    message = "Hedging comment suggests uncertainty - verify code works"
    pattern = re.compile(
        r"#\s*(should work|hopefully|probably|might work|try this|i think|seems to|appears to)\b",
        re.IGNORECASE,
    )
