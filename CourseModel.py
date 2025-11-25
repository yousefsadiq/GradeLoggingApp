"""
A course taken by a student.
"""

from AssessmentModel import AssessmentModel

class CourseModel:

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
        if self.assessments:
            return self._calculate_mark()
        return -1

    def set_desired_mark(self, desired_mark: float) -> None:
        self.desired_mark = desired_mark

    def get_desired_mark(self) -> float:
        return self.mark

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def add_assessment(self, name: str, weight: float, mark: float=-1) -> None:
        if mark != -1:
            assessment = AssessmentModel(name, weight)
        else:
            assessment = AssessmentModel(name, weight, mark)
        self.assessments.append(assessment)

    def remove_assessments(self, name: str) -> None:
        for assessment in self.assessments:
            if assessment.name == name:
                self.assessments.remove(assessment)

    def get_assessments(self, name: str) -> AssessmentModel:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        raise ValueError("Assessment is not in this course.")

    def __eq__(self, other):
        if isinstance(other, CourseModel):
            if self.name == other.assessments and self.assessments == other.assessments and self.desired_mark == other.desired_mark:
                return True
        return False

    def _calculate_mark(self) -> float:
        marks = []
        for assessment in self.assessments:
            if assessment.mark != -1:
                marks.append((assessment.mark, assessment.weight))
        final_mark = 0
        for mark in marks:
            final_mark += (mark[0] * (mark[1]) / 100)
        return final_mark

    def _calculate_mark_needed(self) -> float:
        weight = 0
        for assessment in self.assessments:
            if assessment.mark != -1:
                weight += assessment.weight
        remaining_weight = (100 - weight) / 100
        return (self.desired_mark - self.get_mark() * weight) / remaining_weight
