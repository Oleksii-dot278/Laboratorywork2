import pytest
from figure import Figure


@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


def test_allowed_not_empty(allowed_figures):
    assert len(allowed_figures) > 0


def test_square_in_allowed(allowed_figures):
    assert "квадрат" in allowed_figures