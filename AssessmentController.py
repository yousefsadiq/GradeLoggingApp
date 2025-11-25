import tkinter as tk
from tkinter import messagebox

from AssessmentView import AssessmentView
from AssessmentModel import AssessmentModel
from CourseController import CourseController
from ServiceModel import ServiceModel

class AssessmentController:

    root: tk.Tk
    service: ServiceModel
    course_id: int
    course_controller: CourseController
    view = AssessmentView
    row_map: dict

    def __init__(self, root, service, course_id, course_controller):
        self.service = service
        self.course_id = course_id
        self.course_controller = course_controller

        self.row_map = {}

        course = self.service.get_course(course_id)
        if course:
            course_name = course.name
        else:
            course_name = "New Course"

    def load_data(self):
        """
        Access a course to obtain it's assessments list.
        """
        assessments_data = self.service.get_assessments_with_ids(self.course_id)

        for assessment_id, assessment_obj in assessments_data:
            key_widget = self.view.add_assessment_row(assessment_obj)
            self.row_map[key_widget] = assessment_id

    def add_assessment(self):
        new_assessment = AssessmentModel(name="New Assessment", weight=0, mark=0)
        new_id = self.service.add_assessment(self.course_id, new_assessment)

        key_widget = self.view.add_assessment_row(new_assessment)
        self.row_map[key_widget] = new_id

    def update_assessment(self, name_widget, grade_widget, weight_widget):
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
        except ValueError:
            return

    def delete_assessment(self, key_widget, row_widgets):
        if messagebox.askyesno("Delete", "Delete this assessment?"):
            assessment_id = self.row_map.get(key_widget)
            if assessment_id:
                self.service.delete_assessment(assessment_id)
                del self.row_map[key_widget]
                for widget in row_widgets:
                    widget.destroy()

    def on_close(self):
        """
        When the assessments window is closed, the course window
        should have recalculated grades.
        """
        self.view.window.destroy()

