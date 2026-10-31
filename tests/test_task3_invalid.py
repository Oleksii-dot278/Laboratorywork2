import pytest
from figure import Figure


@pytest.mark.parametrize("bad_type", ["коло", "", "ромб"])
def test_invalid_type_value(bad_type):
    with pytest.raises(ValueError):
        Figure(bad_type, 5)


@pytest.mark.parametrize("bad_type", [123, None])
def test_invalid_type_error(bad_type):
    with pytest.raises(TypeError):
        Figure(bad_type, 5)


@pytest.mark.parametrize("bad_length", [0, -1, -10])
def test_invalid_length_value(bad_length):
    with pytest.raises(ValueError):
        Figure("квадрат", bad_length)


@pytest.mark.parametrize("bad_length", ["5", None])
def test_invalid_length_type(bad_length):
    with pytest.raises(TypeError):
        Figure("квадрат", bad_length)