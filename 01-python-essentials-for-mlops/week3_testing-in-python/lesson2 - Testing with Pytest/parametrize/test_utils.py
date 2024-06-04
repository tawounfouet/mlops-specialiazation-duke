import pytest
from utils import str_to_bool


def test_yes_is_true():
    result = str_to_bool('yes')
    assert result is True


def test_y_is_true():
    result = str_to_bool('y')
    assert result is True



@pytest.mark.parametrize('value', ['y', 'yes', ''])
def test_is_true(value):
    result = str_to_bool(value)
    assert result is True
