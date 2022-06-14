import pytest

from Assignment8.func.calculate_interest import SimpleInterest


@pytest.fixture()
def sample_simple_interest():
    return SimpleInterest(1222, 13, 6)


@pytest.fixture()
def sample_simple_interest_with_params(request):
    return SimpleInterest(request.param['principal'], request.param['months'], request.param['roi'])
