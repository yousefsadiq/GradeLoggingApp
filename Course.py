"""
A course taken by a student.
"""

from Assessment import Assessment

class Course:

    name: str
    assessments: list[Assessment]

    def __init__(self, name: str) -> None:
        self.name = name
        self.assessments = []

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def add_assessment(self, assessment: Assessment) -> None:
        self.assessments.append(assessment)

    def remove_assessments(self, assessment: Assessment) -> None:
        self.assessments.remove(assessment)

    def get_assessments(self, assessment: Assessment) -> Assessment:
        for item in self.assessments:
            if item == assessment:
                return assessment
        raise ValueError("Assessment is not in this course.")