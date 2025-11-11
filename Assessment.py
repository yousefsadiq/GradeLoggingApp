"""
A weighted task for some course.
"""

class Assessment:

    name: str
    weight: float
    mark: float

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.mark = -1

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_weight(self, weight: float) -> None:
        self.weight = weight

    def get_weight(self) -> float:
        return self.weight

    def set_mark(self, mark: float) -> None:
        self.mark = mark

    def get_mark(self) -> float:
        return self.mark
