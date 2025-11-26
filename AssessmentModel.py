class AssessmentModel:
    """
    A weighted task for a course.
    """

    name: str
    weight: float
    mark: float

    def __init__(self, name: str="", weight: float=-1, mark: float=-1) -> None:
        self.name = name
        self.weight = weight
        self.mark = mark

    def set_name(self, name: str) -> None:
        """
        Sets this AssessmentModel's <name>
        """
        self.name = name

    def get_name(self) -> str:
        """
        Returns this AssessmentModel's <name>
        """
        return self.name

    def set_weight(self, weight: float) -> None:
        """
        Sets this AssessmentModel's <weight>
        """
        self.weight = weight

    def get_weight(self) -> float:
        """
        Returns this AssessmentModel's <weight>
        """
        return self.weight

    def set_mark(self, mark: float) -> None:
        """
        Sets this AssessmentModel's <mark>
        """
        self.mark = mark

    def get_mark(self) -> float:
        """
        Returns this AssessmentModel's <mark>
        """
        return self.mark
