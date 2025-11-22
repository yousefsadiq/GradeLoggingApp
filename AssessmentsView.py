"""
The UI of the Assessments page in the grade logging app
"""

import tkinter as tk
from tkinter import messagebox

class AssessmentView:
    def __init__(self, master, course_name):
        self.window = tk.Toplevel(master)# a Toplevel widget is used to create a new,
                                        # independent window separate from the main window
        self.window.title(course_name + " Assessments")
        self.window.geometry('700x600')

        header_frame = tk.Frame(self.window)
        header_frame.pack(fill='x', padx=20, pady=20)
        tk.Label(header_frame, text="Assessments",
                 font=("Arial", 20, "bold")).pack(side='left')

        # Frame to hold the assessment rows.
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack(fill="both", padx=20, expand=True)

        # Create tables manually with the headers (4) and widgets (4)
        self.grid_frame.grid_columnconfigure(0, weight=3) # wide assessment name column
        self.grid_frame.grid_columnconfigure(1, weight=1)
        self.grid_frame.grid_columnconfigure(2, weight=1)
        self.grid_frame.grid_columnconfigure(3, weight=0) # Actions menu containing edit and delete

        # Exact same method of added headers in their columns like in CourseView.py
        headers = ["Assessment Name", "Grade (%)", "Weight", ""]
        for column_number, text in enumerate (headers):
            tk.Label(self.grid_frame, text=text, font=('Arial', 10, "bold")).grid(
                row=0, column=column_number, pady=(0,10), sticky="ew"
            )

        self.row_counter = 1    # to track rows so we know here to add the new table

        # Footer with the add button
        footer = tk.Frame(self.window)
        footer.pack(pady=20)
        add_button = tk.Button(footer, text="➕", font=("Arial", 16),
                               command=self.add_assessment
                               )
        add_button.pack()

    def add_assessment(self):
        """
        Adds a single table row to the assessment grid.
        """
        r = self.row_counter

        name = tk.Entry(self.grid_frame, justify='center')
        name.grid(row=r, column=0, padx=5, pady=10, stick='ew')

        grade = tk.Entry(self.grid_frame, justify='center', width=3)
        grade.grid(row=r, column=1, padx=5, stick='ew')

        weight = tk.Entry(self.grid_frame, justify='center', width=3)
        weight.grid(row=r, column=2, padx=5, stick='ew')

        delete_button = tk.Button(self.grid_frame, text='🗑', fg='red',
                                  command=lambda: self.delete_row(
            [name, grade, weight, delete_button])
                  )
        delete_button.grid(row=r, column=3)

        self.row_counter += 1 # So that a new table gets added in the next row.

    def delete_row(self, widgets):
        """
        Confirm and delete an assessment row
        """
        if messagebox.askyesno("Confirm Delete Assessment",
                "Are you sure you want to delete this course? "
        "This action cannot be undone. You will lose all progress of this assessment."):
            for widget in widgets:
                widget.destroy()

if __name__ == "__main__":
    master = tk.Tk()
    master.withdraw()
    AssessmentView(master, "Sample Course") # We do not assign this to a variable as this opens once only and works alone.
    master.mainloop()                             # It is not connecting to the main window, it is its own window.