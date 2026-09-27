import pytest
from streamshield.limits import ResourceLimits

def test_key_limit() -> None:
    with pytest.raises(ValueError): ResourceLimits(2).validate_key("abc")
