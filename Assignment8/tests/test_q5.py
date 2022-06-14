"""
Mock all functions in calculate_interest() to return valid values.
Assert calculate interest returns expected output.
Assert all mock were called once
"""
from unittest import mock

from Assignment8.func.calculate_interest import SimpleInterest


def test_calculate_interest():
    SimpleInterest.months_to_years = mock.Mock(return_value=4)
    SimpleInterest.validate_principal = mock.Mock(return_value=10000)
    SimpleInterest.validate_rate_of_interest = mock.Mock(return_value=10)
    simple_interest = SimpleInterest(10000, 48, 10)
    assert simple_interest.calculate_interest() == 4000
    SimpleInterest.validate_principal.assert_called_once()
    SimpleInterest.months_to_years.assert_called_once()
    SimpleInterest.validate_rate_of_interest.assert_called_once()
