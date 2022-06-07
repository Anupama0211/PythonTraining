"""
Use simple fixture that returns instance of SimpleInterest and create test function to assert validate_principal() to be true.
"""
import pytest


def test_validate_principal(sample_simple_interest):
    assert sample_simple_interest.validate_principal() == 1222


@pytest.mark.parametrize(
    "sample_simple_interest_with_params",
    [({'principal': 100, 'months': 20, 'roi': 6})],
    indirect=['sample_simple_interest_with_params'])
def test_validate_principal_raises_error(sample_simple_interest_with_params):
    with pytest.raises(ValueError) as exe:
        assert sample_simple_interest_with_params.validate_principal() == 100
        assert exe.value == f"Principal amount has to be between 1000 and 100000"
