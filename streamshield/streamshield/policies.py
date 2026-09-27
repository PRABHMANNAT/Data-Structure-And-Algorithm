from enum import StrEnum

class LateDataPolicy(StrEnum):
    REJECT = "reject"
    DROP = "drop"

def should_raise(policy: LateDataPolicy) -> bool:
    return policy == LateDataPolicy.REJECT
