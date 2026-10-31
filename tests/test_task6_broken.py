from figure import Figure


def test_broken():
    assert Figure("квадрат", 10).get_figure_length() == 999