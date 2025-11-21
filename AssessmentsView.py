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