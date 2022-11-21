import pytest
from func.calculator import add, add_integers


def test_add_number():
    assert add(1,2) == 3




# #test string addition
def test_add_string():
    assert add("a","b") == "ab"


# #raise exception
def test_add_integers():
    #use match
    # with pytest.raises(ValueError) as exe:
    assert add_integers("a","b") == "ab"
    # assert exe.value == "a and b should be integers"