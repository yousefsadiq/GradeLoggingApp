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
        self.grid_frame.grid_columnconfigure(0, weight=5)
        for i in range(1, len(headers)):
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Using enumerate so we iterate through headers list and assigns a index position which becomes
        # its column position with the column name being the header
        for column_name, text in enumerate(headers):
            tk.Label(self.grid_frame, text=text, font=("Arial", 12, "bold")).grid(
                row=0, column=column_name, pady=(0,10), sticky="ew")

        # To add a new course with the button to add on the bottom of the courses
        footer = tk.Frame(master)
        footer.pack(pady=20)
        add_button = tk.Button(footer, text="➕", font=("Arial", 16))
        add_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()