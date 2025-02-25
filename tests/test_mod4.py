import sys
sys.path.append('.')
from bin import sample_code

def test_sample_function():
    result = sample_code.some_function()
    assert result == expected_result
