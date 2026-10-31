class Figure:
    FIGURES = ("квадрат", "трикутник", "прямокутник")

    def __init__(self, figure_type, length):
        if not isinstance(figure_type, str):
            raise TypeError("Тип фігури має бути рядком")
        if figure_type not in self.FIGURES:
            raise ValueError("Недозволений тип фігури")
        if isinstance(length, bool) or not isinstance(length, (int, float)):
            raise TypeError("Довжина має бути числом")
        if length <= 0:
            raise ValueError("Довжина має бути більшою за 0")

        self.type = figure_type
        self._length = length

    def get_figure_length(self):
        return self._length