"""
The UI of the Assessments page in the grade logging app
"""

import tkinter as tk

class AssessmentView:
    def __init__(self, master, course_name):
        self.window = tk.Toplevel(master)
        # a Toplevel widget is used to create a new, independent window separate from the main window
        self.window.title("Assessments" + course_name)

        tk.Label(self.window, text="Assessments Page", font=("Arial", 16)).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    AssessmentView(root, "TEST101") # We do not assign this to a variable as this opens once only and works alone.
    root.mainloop()                             # It is not connecting to the main window, it is its own separate window.