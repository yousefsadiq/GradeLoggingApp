"""
The UI of the Assessments page in the grade logging app
"""

import tkinter as tk

class AssessmentView:
    def __init__(self, master, course_name):
        self.window = tk.Toplevel(master)# a Toplevel widget is used to create a new,
                                        # independent window separate from the main window
        self.window.title("Assessments" + course_name)
        self.window.geometry('700x600')

        header_frame = tk.Frame(self.window)
        header_frame.pack(fill='x', padx=20, pady=20)
        tk.Label(header_frame, text=course_name + " Assessments",
                 font=("Arial", 20, "bold")).pack(side='left')

        # Frame to hold the assessment rows.
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack(fill="both", padx=20, expand=True)

        # Create tables manually with the headers (4) and widgets (4)
        self.grid_frame.grid_columnconfigure(0, weight=3) # Assessment Name. Stretched the longest
        self.grid_frame.grid_columnconfigure(1, weight=1)
        self.grid_frame.grid_columnconfigure(2, weight=1)
        self.grid_frame.grid_columnconfigure(3, weight=1) # Actions menu containing edit and delete

        # Exact same method of added headers in their columns like in CourseView.py
        headers = ["Assessment Name", "Grade (%)", "Weight", ""]
        for column_number, text in enumerate (headers):
            tk.Label(self.grid_frame, text=text, font=('Arial', 10, "bold")).grid(
                row=0, column=column_number, pady=(0,10), sticky="ew"
            )

        self.row_counter = 1

        # Footer with the add button
        footer = tk.Frame(self.window)
        footer.pack(pady=20)
        add_button = tk.Button(footer, text="➕", font=("Arial", 16))
        add_button.pack()

if __name__ == "__main__":
    master = tk.Tk()
    master.withdraw()
    AssessmentView(master, "Sample Course") # We do not assign this to a variable as this opens once only and works alone.
    master.mainloop()                             # It is not connecting to the main window, it is its own window.