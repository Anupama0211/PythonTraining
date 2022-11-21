import pytest
import sys
from func.calculator import add, add_integers

# skip
# skip with reason
@pytest.mark.skip
def test_add_number_1():
    assert add(1, 2) == 3


# skipif
# # skip with condition
@pytest.mark.skipif(sys.version_info > (3,0),reason="Skip if python 3.0 or greater")
def test_add_string():
    assert add("a","b") == "ab"



# # xfail
@pytest.mark.xfail(sys.platform == 'linux', reason="Allow exeception for linux")
def test_add_number():
    assert add(1,2) == 3
    raise Exception




# parameterize
# with ids
@pytest.mark.additi
@pytest.mark.parametrize(
    "inp1, inp2, output",
    [
        (1, 2, 3),
        (5, 2, 7),
        (5, 5, 10),
    ],
    ids = ['test1','test2','test3']
)
def test_add_number_param(inp1, inp2, output):
    assert add(inp1, inp2) == output

