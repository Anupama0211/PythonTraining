from unittest import mock
import pytest

from func.dice import guess_number
from func.url_response import get_response

#spec
mock_roll_dice = mock.Mock(name="Roll Dice",**{'a':10, 'b':30}, return_value=10)


print(mock_roll_dice.a, mock_roll_dice.b, mock_roll_dice.c)



#check how many times its called
# print(mock_roll_dice.assert_called_once())



# side effect: pass func to side_effect




# magic_mock = mock.MagicMock(name="Roll Dice Magic", return_value=11)
# def test_dummy():
#     print(len(magic_mock))
#     print(list(magic_mock))
#     print("Match")



# basic mock
@mock.patch('func.dice.roll_dice')
def test_guess_number_wins(mock_roll_dice):
    value = 2
    mock_roll_dice.return_value = value
    assert guess_number(value) == "you win"




# mock with params
@pytest.mark.parametrize('input, output', [(3, "you lost"), (2, "you win")], ids =['wincase','losecase'])
@mock.patch('func.dice.roll_dice')
def test_guess_number(mock_roll_dice, input, output):
    mock_roll_dice.return_value = 2
    assert guess_number(input) == output






@mock.patch('func.url_response.requests.get')
def test_url_response(mock_response_get):
    mock_response_get.return_value = mock.Mock(**{'status_code':200, 'json.return_value':{'slideshow':{'author':'Yours Truly'}}})
    response = get_response()
    mock_response_get.assert_called_once_with('https://httpbin.org/json')
    assert isinstance(response,dict) and response['author'] == 'Yours Truly'
     
