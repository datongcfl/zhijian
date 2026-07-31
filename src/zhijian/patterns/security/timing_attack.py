"""安全检测：时序攻击漏洞检测器

检测使用 == 比较密码/密钥/敏感数据的代码。
应使用 secrets.compare_digest() 防止时序攻击。

示例：
- if password == config.SECRET:   ← 危险
- if token == expected_token:     ← 危险
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class TimingAttackPattern(RegexPattern):
    """检测可能的时序攻击漏洞"""

    id = "timing_attack"
    severity = Severity.HIGH
    axis = Axis.QUALITY
    message = "Sensitive comparison using == — use secrets.compare_digest() to prevent timing attacks"
    pattern = re.compile(
        r"(?:password|passwd|secret|token|key|api_key|auth|credential|signature)\s*==\s*\w+"
        r"|"
        r"\w+\s*==\s*(?:password|passwd|secret|token|key|api_key|auth|credential|signature)",
        re.IGNORECASE,
    )
