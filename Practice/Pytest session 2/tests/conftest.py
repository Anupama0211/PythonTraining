import pytest
from func.person import Person

#scopes; function, modules, session etc
@pytest.fixture()
def sample_person():
    print('FIXTURE')
    return Person("Prashant", 20, 0)




@pytest.fixture
def sample_person_with_param(request):
    return Person("Prashant", request.param, 0)





# Bootstrapping hooks
def pytest_load_initial_conftests(early_config, parser, args):
    pass



# Initialization hooks
def pytest_addoption(parser, pluginmanager):
    pass



# Collection hooks
def pytest_collect_file(file_path, path, parent):
    pass


# Test running hooks
def pytest_runtest_setup(item):
    pass



# Reporting hooks
def pytest_make_collect_report(collector):
    pass