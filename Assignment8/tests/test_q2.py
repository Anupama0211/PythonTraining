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
def test_valid_years(principal, months, roi):
    simple_interest_obj = SimpleInterest(principal, months, roi)
    with pytest.raises(ValueError) as exe:
        assert simple_interest_obj.months_to_years() == months // 12
        assert exe.value == 'Months cannot be less than 12'
