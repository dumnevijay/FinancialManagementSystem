import tkinter as tk

class InterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Interest Calculator")

        # Create and place the input label and entry
        self.input_label = tk.Label(root, text="Enter number:")
        self.input_label.grid(row=0, column=0)

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(root, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=1)

        # Create and place the interest label and entry
        self.interest_label = tk.Label(root, text="Interest (20%):")
        self.interest_label.grid(row=1, column=0)

        self.interest_var = tk.StringVar()
        self.interest_entry = tk.Entry(root, textvariable=self.interest_var, state='readonly')
        self.interest_entry.grid(row=1, column=1)

        # Trace changes to the input variable
        self.input_var.trace("w", self.calculate_interest)

    def calculate_interest(self, *args):
        try:
            number = float(self.input_var.get())
            interest = number * 0.2
            self.interest_var.set(f"{interest:.2f}")
        except ValueError:
            # Handle case where the input is not a valid number
            self.interest_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterestCalculator(root)
    root.mainloop()
