"""
Create parametrized testcases that generates samples of valid principal, months, ROI for the
testcases. Assert that arguments for SimpleInterest instance are set.
"""
import pytest

from Assignment8.func.calculate_interest import SimpleInterest


@pytest.mark.parametrize(
    "principal, months, roi",
    [
        (2300, 12, 8),
        (4500, 14, 6),
        (500, 5, 10),
    ],
    ids=['test1', 'test2', 'test3']
)
def test_simple_interest(principal, months, roi):
    simple_interest_obj = SimpleInterest(principal, months, roi)
    assert simple_interest_obj.principal == principal
    assert simple_interest_obj.months == months
    assert simple_interest_obj.roi == roi
