"""
The controller class to allow a CourseModel and CourseView to interact.
"""
import tkinter as tk
from tkinter import messagebox

from ServiceModel import ServiceModel
from CourseView import CourseView
from AssessmentController import AssessmentController
from CourseModel import CourseModel

class CourseController:

    root: tk.Tk
    service: ServiceModel
    view: CourseView
    row_map: dict

    def __init__(self, root: tk.Tk, service: ServiceModel) -> None:
        self.root = root
        self.service = service
        self.view = CourseView(root)
        self.view.set_controller(self)
        self.row_map = {}
        self.load_courses()

    def load_courses(self):
        """
        Fetches all courses from the local database and populates
        the view.
        """
        courses = self.service.get_all_courses()
        for course_id, course_obj in courses:
            key_widget = self.view.add_course_row(course_obj)
            self.row_map[key_widget] = course_id

    def add_course(self):
        """
        Creates a default course in the database and adds it to the UI.
        """
        course = CourseModel(name="New Course", desired_mark=0.0)
        id = self.service.add_course(course)

        key_widget = self.view.add_course_row(course)
        self.row_map[key_widget] = id

    def update_course(self, name_widget, desired_widget):
        """
        Called when a user edits a field and leaves.
        """
        course_id = self.row_map.get(name_widget)
        if course_id is None:
            return
        try:
            name_val = name_widget.get()
            if desired_widget.get():
                desired_val = float(desired_widget.get())
            else:
                desired_val = -1
            updated_course = CourseModel(name=name_val, desired_mark=desired_val)
            self.service.update_course(course_id, updated_course)
        except ValueError:
            return

    def delete_course(self, key_widget, all_row_widgets):
        """
        Deletes a course from the local database and it's row
        from the UI.
        """
        if messagebox.askyesno("Confirm Delete", "Are you sure? This cannot be undone."):
            course_id = self.row_map.get(key_widget)
            if course_id:
                self.service.delete_course(course_id)
                del self.row_map[key_widget]

                for widget in all_row_widgets:
                    widget.destroy()

    def open_assessments(self, key_widget):
        """
        Opens the Assessment window for the specific course
        """
        course_id = self.row_map.get(key_widget)
        if course_id:
            AssessmentController(self.root, self.service, course_id, self)