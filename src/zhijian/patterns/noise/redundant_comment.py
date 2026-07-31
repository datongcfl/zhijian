"""噪音检测：冗余注释检测器

检测只是重复代码的注释，例如：
- # increment x  在 x += 1 上面
- # return value  在 return value 上面
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class RedundantComment(RegexPattern):
    """检测重复代码的注释"""

    id = "redundant_comment"
    severity = Severity.MEDIUM
    axis = Axis.NOISE
    message = "Redundant comment restating obvious code"
    pattern = re.compile(
        r"#\s*(increment|decrement|set|assign|return|get|initialize|init|create)\s+\w+\s*$",
        re.IGNORECASE,
    )
