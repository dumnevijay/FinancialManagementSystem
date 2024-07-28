from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import date

class get_date():
    def get_data():
        root = Tk()
        root.title("Date Picker")
        root.geometry("500x300")


        today = date.today()

        cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)
        cal.pack(pady=20)

        def grab_days(cal):
            return cal.get_date()

        my_button = Button(root, text="Get Date", command=cal.get_date())
        my_button.pack(pady=20)

        my_label = Label(root, text="")
        my_label.pack(pady=20)
        # Run the application
        root.mainloop()
