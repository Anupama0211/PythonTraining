import os, sys
import pytest
from func.save import save_data
from func.person import is_eligible


# def test_save_data(tmpdir):
#     file_path = os.path.join(tmpdir, "temp.txt")
#     line = "Save this data in file"
#     save_data(line,filepath=file_path)
#     with open(file_path, 'r') as file:
#         assert file.readline() == line


# def test_person_age(sample_person):
#     assert sample_person.get_age() == 20

# def test_person_add_credit(sample_person):
#     assert sample_person.add_credit(10) == 10

# def test_person_get_credit(sample_person):
#     assert sample_person.get_credit() == 0




@pytest.mark.parametrize('sample_person_with_param, output',[({'a':1,'b':2}, False), (30, True)], indirect=['sample_person_with_param'])
def test_person_is_eligible(sample_person_with_param, output):
    assert is_eligible(sample_person_with_param) == output