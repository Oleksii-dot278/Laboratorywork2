import pytest
from figure import Figure


@pytest.fixture
def square_10():
    return Figure("квадрат", 10)


def test_square_10_properties(square_10):
    assert square_10.type == "квадрат"
    assert square_10.get_figure_length() == 10