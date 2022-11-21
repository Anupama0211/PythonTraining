"""
4.Create fixture that params and returns instance of SimpleInterest.
 Create a parameterized testcases that generates valid principal, months, ROI and pass it to the fixture.
Assert instance.month_to_year() returns valid number of years. Output of should also be parametrized
"""
import pytest


@pytest.mark.parametrize(
    "sample_simple_interest_with_params,output",
    [
        ({'principal': 10300, 'months': 13, 'roi': 6}, 1),
        ({'principal': 12300, 'months': 25, 'roi': 8}, 2),
        ({'principal': 10330, 'months': 36, 'roi': 10}, 3)
    ],
    indirect=['sample_simple_interest_with_params'])
def test_months_to_years(sample_simple_interest_with_params, output):
    assert sample_simple_interest_with_params.months_to_years() == output
