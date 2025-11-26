from AssessmentModel import AssessmentModel

class CourseModel:
    """
    A course taken by a student.
    """

    desired_mark: float
    name: str
    assessments: list[AssessmentModel]

    def __init__(self, desired_mark: float=-1, name: str="", assessments: list=None) -> None:
        if assessments is None:
            assessments = []
        self.desired_mark = desired_mark
        self.name = name
        self.assessments = assessments

    def get_mark(self) -> float:
        """
        Calculates and returns this CourseModel's current grade
        """
        if self.assessments:
            return self._calculate_mark()
        return -1

    def get_required_mark(self) -> float:
        """
        Calculates and returns the mark on this CourseModel's remaining
        assessments to achieve it's <desired_mark>
        """
        if self.assessments:
            return self._calculate_mark_needed()
        return -1

    def set_desired_mark(self, desired_mark: float) -> None:
        """
        Sets this CourseModel's <desired_mark>
        """
        self.desired_mark = desired_mark

    def get_desired_mark(self) -> float:
        """
        Returns this CourseModel's <desired_mark>
        """
        return self.desired_mark

    def set_name(self, name: str) -> None:
        """
        Sets this CourseModel's <name>
        """
        self.name = name

    def get_name(self) -> str:
        """
        Returns this CourseModel's <name>
        """
        return self.name

    def add_assessment(self, name: str, weight: float=-1, mark: float=-1) -> None:
        """
        Creates and adds an AssessmentModel to <assessments>
        """
        assessment = AssessmentModel(name, weight, mark)
        self.assessments.append(assessment)

    def remove_assessment(self, name: str) -> None:
        """
        Removes an AssessmentModel from <assessments>
        """
        for assessment in self.assessments:
            if assessment.name == name:
                self.assessments.remove(assessment)

    def get_assessment(self, name: str) -> AssessmentModel:
        """
        Returns the AssessmentModel that matches <name>
        """
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        raise ValueError("Assessment is not in this course.")

    #Private method to calculate this CourseModel's current mark.
    def _calculate_mark(self) -> float:
        total_score_weighted = 0
        total_weight_completed = 0

        for assessment in self.assessments:
            if assessment.mark != -1 and assessment.weight != -1:
                total_score_weighted += (assessment.mark * (assessment.weight / 100))
                total_weight_completed += assessment.weight

        if total_weight_completed == 0:
            return 0.0
        return (total_score_weighted / (total_weight_completed / 100))

    # Private method to calculate the mark needed to obtain <desired_mark>
    # for this CourseModel
    def _calculate_mark_needed(self) -> float:
        total_score_weighted = 0
        total_weight_completed = 0

        for assessment in self.assessments:
            if assessment.mark != -1 and assessment.weight != -1:
                total_score_weighted += (assessment.mark * (assessment.weight / 100))
                total_weight_completed += assessment.weight

        remaining_weight = 100 - total_weight_completed
        if remaining_weight <= 0:
            return 0.0
        points_needed = self.desired_mark - total_score_weighted

        return (points_needed / remaining_weight) * 100
