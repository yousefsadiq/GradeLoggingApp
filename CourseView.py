'''
The UI of the Courses page in the grade logging app
'''

import tkinter as tk

class CourseView:
    def __init__(self, master):
        self.master = master
        master.title("Grade Logging App")

        tk.Label(master, text="My Courses", font=("Arial", 24)).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()