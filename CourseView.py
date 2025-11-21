'''
The UI of the Courses page in the grade logging app
'''

import tkinter as tk

class CourseView:
    def __init__(self, master):
        self.master = master
        master.title("Grade Logging App")
        master.geometry("900x500")

        tk.Label(master, text="My Courses", font=("Arial", 24, "bold")).pack(pady=20)

        # Frame to hold the course rows in a grid layout
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(fill='both', padx=20, expand=True)

        # Create column headers
        headers = ["Course Name", "Current Grade", "Desired Grade", "Required Grade", " "]


        for i in range(5):
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Using enumerate so we iterate through headers list and assigns a index position which becomes
        # its column position with the column name being the header
        for column_name, text in enumerate(headers):
            (tk.Label(self.grid_frame, text=text, font=("Arial", 12, "bold"))
             .grid(row=0, column=column_name))

        # To add a new course with the button to add on the bottom of the courses
        footer = tk.Frame(master)
        footer.pack(pady=20)

        add_button = tk.Button(footer, text="➕", font=("Arial", 16))
        add_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseView(root)
    root.mainloop()