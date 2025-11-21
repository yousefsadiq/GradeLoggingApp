'''
The UI of the Courses page in the grade logging app
'''

import tkinter as tk

class CourseView:
    def __init__(self, master):
        self.master = master
        master.title("Grade Logging App")
        master.geometry("1000x600")

        header_frame = tk.Frame(master)
        header_frame.pack(fill='x', padx=20, pady=20)
        tk.Label(header_frame, text="My Courses", font=("Arial", 24, "bold")).pack(side='left')

        # Frame to hold the course rows in a grid layout
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(fill='both', padx=20, expand=True)

        headers = ["Course Name", "Current Grade", "Desired Grade", "Required Grade", "Actions"]

        # Configure columns, first column gets more space, others get weight 1
        self.grid_frame.grid_columnconfigure(0, weight=7)
        for i in range(1, len(headers)):
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Using enumerate so we iterate through headers list and assigns a index position which becomes
        # its column position with the column name being the header
        for column_name, text in enumerate(headers):
            tk.Label(self.grid_frame, text=text, font=("Arial", 12, "bold")).grid(
                row=0, column=column_name, pady=(0,10), sticky="ew")

        self.row_counter = 1 # first row after headers. used to track rows

        # To add a new course with the button to add on the bottom of the courses
        footer = tk.Frame(master)
        footer.pack(pady=20)
        add_button = tk.Button(footer, text="➕", font=("Arial", 16), command=self.add_course_new)
        add_button.pack()

    def add_course_new(self):
        # Widgets for each column header, including the button
        tk.Entry(self.grid_frame, justify='center', font=('Arial', 10)).grid(row=self.row_counter, column=0, padx=5, pady=10, stick='ew')
        tk.Label(self.grid_frame, justify='center', text='--%').grid(row=self.row_counter, column=1)
        tk.Entry(self.grid_frame, justify='center').grid(row=self.row_counter, column=2)
        tk.Label(self.grid_frame, justify='center', text='--%').grid(row=self.row_counter, column=3)
        tk.Button(self.grid_frame, text='📝', font=('Arial', 11)).grid(row=self.row_counter, column=4, padx=5)

        self.row_counter += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()