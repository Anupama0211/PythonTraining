import pytest
from func.person import Person

#scopes; function, modules, session etc
@pytest.fixture()
def sample_person():
    print('FIXTURE')
    return Person("Prashant", 20, 0)



@pytest.fixture
def sample_person_with_param(request):
    print(request.param['a'])
    return Person("Prashant", request.param, 0)
