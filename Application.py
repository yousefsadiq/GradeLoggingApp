"""
Grade Logging App
"""

import tkinter as tk
from ServiceModel import ServiceModel
from CourseController import CourseController

def main():
    root = tk.Tk()
    service = ServiceModel("grades.db")
    controller = CourseController(root, service)
    root.mainloop()

if __name__ == "__main__":
    main()
