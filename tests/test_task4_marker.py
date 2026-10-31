import pytest
from figure import Figure


@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.unit
def test_square_length():
    assert Figure("квадрат", 5).get_figure_length() == 5


def test_without_marker():
    assert Figure("прямокутник", 3).type == "прямокутник"