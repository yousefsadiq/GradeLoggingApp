import tkinter as tk
from tkinter import messagebox

from AssessmentView import AssessmentView
from AssessmentModel import AssessmentModel
from ServiceModel import ServiceModel

class AssessmentController:
    """
    A controller class to allow an AssessmentModel and AssessmentView to interact
    """
    service: ServiceModel
    course_id: int
    view = AssessmentView
    row_map: dict

    def __init__(self, root: tk.Tk, service: ServiceModel, course_id: int, course_controller) -> None:
        self.service = service
        self.course_id = course_id
        self.course_controller = course_controller

        self.row_map = {}

        course = self.service.get_course(course_id)
        if course:
            course_name = course.name
        else:
            course_name = "New Course"

        self.view = AssessmentView(root, course_name)
        self.view.set_controller(self)
        self.load_data()

    def load_data(self) -> None:
        """
        Load in a course's list of assessments.
        """
        assessments_data = self.service.get_assessments_with_ids(self.course_id)

        for assessment_id, assessment_obj in assessments_data:
            key_widget = self.view.add_assessment_row(assessment_obj)
            self.row_map[key_widget] = assessment_id

    def add_assessment(self):
        """
        Add an assessment to the database and this AssessmentController's <view>
        """
        new_assessment = AssessmentModel(name="New Assessment", weight=0, mark=0)
        new_id = self.service.add_assessment(self.course_id, new_assessment)

        key_widget = self.view.add_assessment_row(new_assessment)
        self.row_map[key_widget] = new_id
        self.course_controller.recalculate_marks(self.course_id)

    def update_assessment(self, name_widget, grade_widget, weight_widget):
        """
        Update an assessment within the database and this AssessmentController's <view>
        """
        assessment_id = self.row_map.get(name_widget)
        if not assessment_id:
            return
        try:
            name = name_widget.get()
            if grade_widget.get():
                mark = float(grade_widget.get())
            else:
                mark = -1
            if weight_widget.get():
                weight = float(weight_widget.get())
            else:
                weight = -1
            assessment_obj = AssessmentModel(name, weight, mark)
            self.service.update_assessment(assessment_id, assessment_obj)
            self.course_controller.recalculate_marks(self.course_id)
        except ValueError:
            return

    def delete_assessment(self, key_widget, row_widgets):
        """
        Delete an assessment from the database and from this AssessmentController's <view>
        """
        if messagebox.askyesno("Delete", "Delete this assessment?"):
            assessment_id = self.row_map.get(key_widget)
            if assessment_id:
                self.service.delete_assessment(assessment_id)
                del self.row_map[key_widget]
                for widget in row_widgets:
                    widget.destroy()
        self.course_controller.recalculate_marks(self.course_id)

    def on_close(self):
        """
        When the assessments window is closed, the course window will recalculate grades.
        """
        self.view.window.destroy()
        self.course_controller.recalculate_marks(self.course_id)

