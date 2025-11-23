"""
The UI of the Courses page in the grade logging app
"""

import tkinter as tk
from tkinter import messagebox as mb
from AssessmentsView import AssessmentView

class CourseView:
    def __init__(self, master):
        self.master = master
        master.title("Grade Logging App")
        master.geometry("1000x600")

        header_frame = tk.Frame(master)
        header_frame.pack(fill='x', padx=20, pady=20)
        tk.Label(header_frame, text="My Courses",
                 font=("Arial", 24, "bold")).pack(side='left')

        # Frame to hold the course rows in a grid layout
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(fill='both', padx=20, expand=True)

        headers = ["Course Name", "Current Grade", "Desired Grade",
                   "Required Grade", "Actions"]

        # Configure columns, first column gets more space, others get weight 1
        self.grid_frame.grid_columnconfigure(0, weight=5)
        for i in range(1, len(headers)):
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Using enumerate so we iterate through headers list and assigns an index position
        # which becomes its column position with the column name being the header
        for column_name, text in enumerate(headers):
            tk.Label(self.grid_frame, text=text, font=("Arial", 12, "bold")).grid(
                row=0, column=column_name, pady=(0,10), sticky="ew")

        self.row_counter = 1 # first row after headers.
                             # used to track rows and where to add the new row

        # To add a new course with the button to add on the bottom of the courses
        footer = tk.Frame(master)
        footer.pack(pady=20)
        add_button = tk.Button(footer, text="➕", font=("Arial", 16),
                               command=self.add_course_new)
        add_button.pack()

    def add_course_new(self):
        """
        Adds a single row to the course grid.
        """

        r = self.row_counter

        # Widgets for each column header, including the button
        # Initializing Entries and Labels. For smoothness and ability to use them as variables

        # Course Name ENTRY
        name = tk.Entry(self.grid_frame, justify='center', font=('Arial', 10))
        name.grid(row=r, column=0, padx=5, pady=10, stick='ew')

        # Current Grade LABEL
        current = tk.Label(self.grid_frame, justify='center', text='--%', fg='green')
        current.grid(row=r, column=1)

        # Desired Grade ENTRY
        desired = tk.Entry(self.grid_frame, justify='center')
        desired.grid(row=r, column=2, sticky='ew')

        # Required Grade LABEL
        required = tk.Label(self.grid_frame, justify='center', text='--%', fg='gray')
        required.grid(row=r, column=3)

        #---Action Column---#
        # use a separate frame for the action column to pack
        # multiple small buttons horizontally
        action_frame = tk.Frame(self.grid_frame)
        action_frame.grid(row=r, column=4)

        # Edit button opens the assessments,
        # uses a lambda function to read the entry content when clicked
        tk.Button(action_frame, text='📝', font=('Arial', 11),command=lambda:
                  self.open_assessments(course_name=name.get())).pack(side='left', padx=4)

        tk.Button(action_frame, text='🗑', font=('Arial', 11), fg='red',command=lambda: self.delete_row(
            [name, current, desired, required, action_frame])
                  ).pack(side='left', padx=4)
        # using lambda function as we need to add arguments,
        # normal function does not allow that.

        # Increment the row counter for the next row to be inserted
        self.row_counter += 1

    def open_assessments(self, course_name):
        """
        Opens the Assessments popup for a course.
        """
        if not course_name:
            course_name = "New Course" # If the user puts nothing in "course name" field.
        AssessmentView(self.master, course_name)

    def delete_row(self, widgets):
        """
        Confirm and delete a course row.
        """

        if mb.askyesno("Confirm Delete Course", "Are you sure you want to delete this course? "
                        "This action cannot be undone. You will lose all progress of this course."):
            for widget in widgets:
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()