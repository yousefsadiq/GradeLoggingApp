"""
A course taken by a student.
"""

from Assessment import Assessment

class Course:

    mark: float
    name: str
    assessments: list[Assessment]

    def __init__(self, name: str) -> None:
        self.mark = -1
        self.name = name
        self.assessments = []

    def set_mark(self, name: str, mark: float) -> None:
        for assessment in self.assessments:
            if assessment.name == name:
                assessment.set_mark(mark)

    def get_mark(self) -> float:
        if self.assessments:
            return self._calculate_mark()
        return -1

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def add_assessment(self, name: str, weight: float, mark: float=-1) -> None:
        if mark != -1:
            assessment = Assessment(name, weight)
        else:
            assessment = Assessment(name, weight, mark)
        self.assessments.append(assessment)

    def remove_assessments(self, name: str) -> None:
        for assessment in self.assessments:
            if assessment.name == name:
                self.assessments.remove(assessment)

    def get_assessments(self, name: str) -> Assessment:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        raise ValueError("Assessment is not in this course.")

    def _calculate_mark(self) -> float:
        marks = []
        for assessment in self.assessments:
            marks.append((assessment.mark, assessment.weight))
        final_mark = 0
        for mark in marks:
            final_mark += (mark[0] * (mark[1]) / 100)
        return final_mark
