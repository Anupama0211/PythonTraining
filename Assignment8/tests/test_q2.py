"""
Create parametrized testcases that generates invalid months and valid principal, ROI.
Assert that instance of SimpleInterest should raise error for months_to_years()
"""

import pytest

from Assignment8.func.calculate_interest import SimpleInterest


@pytest.mark.parametrize(
    "principal, months, roi",
    [
        (2300, 11, 8),
        (4500, 3, 6),
        (5000, 5, 10),
    ],
    ids=['test1', 'test2', 'test3']
)
def test_invalid_months_raises_exception(principal, months, roi):
    simple_interest_obj = SimpleInterest(principal, months, roi)
    with pytest.raises(ValueError) as error:
        assert simple_interest_obj.months_to_years() == months // 12
        assert error.value == 'Months cannot be less than 12'
