"""安全检测模式集合

这些模式检测代码中的安全问题：
- 时序攻击漏洞
- 错误信息泄露
"""

from zhijian.patterns.security.timing_attack import TimingAttackPattern
from zhijian.patterns.security.error_leakage import ErrorLeakagePattern

SECURITY_PATTERNS = [
    TimingAttackPattern(),
    ErrorLeakagePattern(),
]

__all__ = [
    "TimingAttackPattern",
    "ErrorLeakagePattern",
    "SECURITY_PATTERNS",
]
