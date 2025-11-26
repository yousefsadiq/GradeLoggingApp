"""
The UI of the Courses page in the grade logging app
"""

import tkinter as tk

class CourseView:
    def __init__(self, master):
        self.master = master
        self.controller = None

        master.title("Grade Logging App")
        master.geometry("1000x600")

        # Click anywhere to save Entry
        master.bind("<Button-1>", self.save_on_click)

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
                               command=lambda: self.controller.add_course())
        add_button.pack()

    def save_on_click(self, event):
        """
        Detect if the previously focused widget was an Entry and save it
        """
        focused = self.master.focus_get()
        if isinstance(focused, tk.Entry) and event.widget != focused:
            self.master.focus_set()

    def set_controller(self, controller):
        """
        Sets a new CourseController for this CourseView.
        """
        self.controller = controller

    def add_course_row(self, course=None):
        """
        Adds a single row to the course grid.
        """

        r = self.row_counter

        # Widgets for each column header, including the button
        # Initializing Entries and Labels. For smoothness and ability to use them as variables

        # Course Name ENTRY
        name = tk.Entry(self.grid_frame, justify='center', font=('Arial', 12))
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

        # Populate data if a course exists
        if course:
            name.insert(0, course.name)
            if course.desired_mark != -1:
                desired.insert(0, str(course.desired_mark))
            curr_mark = course.get_mark()
            req_mark = course.get_required_mark()
            if curr_mark != -1:
                current.config(text=f"{curr_mark:.2f}%")
            else:
                required.config(text="--%")

            if req_mark != -1:
                required.config(text=f"{req_mark:.2f}%")
            else:
                required.config(text="--%")

        # Bindings
        save_callback = lambda e: self.controller.update_course(name, desired)
        name.bind("<FocusOut>", save_callback)
        name.bind("<Return>", save_callback)
        desired.bind("<FocusOut>", save_callback)
        desired.bind("<Return>", save_callback)

        # Edit button opens the assessments,
        # uses a lambda function to read the entry content when clicked
        tk.Button(action_frame, text='📝', font=('Arial', 11),
                  command=lambda: self.controller.open_assessments(name)).pack(side='left', padx=4)

        row_widgets = [name, current, desired, required, action_frame]
        tk.Button(action_frame, text='🗑', font=('Arial', 11), fg='red',
                  command=lambda: self.controller.delete_course(name, row_widgets)).pack(side='left', padx=4)
        # using lambda function as we need to add arguments,
        # normal function does not allow that.

        # Increment the row counter for the next row to be inserted
        self.row_counter += 1

        return name, current, required

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()