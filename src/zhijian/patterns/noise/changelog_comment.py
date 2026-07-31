"""噪音检测：版本历史注释检测器

检测代码中的版本历史注释，这类信息应该放在 git commits 中，而不是代码里。
例如：
- # v1.2.3 - added new feature
- # v2.0.0: fixed bug
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class ChangelogComment(RegexPattern):
    """检测代码中的版本历史注释"""

    id = "changelog_in_code"
    severity = Severity.LOW
    axis = Axis.NOISE
    message = "Version history belongs in git commits, not code comments"
    pattern = re.compile(
        r"#\s*v?\d+\.\d+.*[-:].*\b(added|fixed|changed|removed|updated)\b", re.IGNORECASE
    )
