import tkinter as tk
from tkinter import ttk
import sqlite3

class LoanView:
    def __init__(self, root):
        self.root = root
        self.root.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Client ID", "Amount", "Interest Rate", "Start Date", "End Date"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Client ID", text="Client ID")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Interest Rate", text="Interest Rate")
        self.tree.heading("Start Date", text="Start Date")
        self.tree.heading("End Date", text="End Date")
        self.tree.pack(fill="both", expand=True)

        self.load_loans()

        self.add_loan_button = ttk.Button(self.root, text="Add Loan", command=self.add_loan)
        self.add_loan_button.pack(pady=10)

    def load_loans(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM loans")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def add_loan(self):
        self.add_loan_window = tk.Toplevel(self.root)
        self.add_loan_window.title("Add Loan")

        self.client_id_label = ttk.Label(self.add_loan_window, text="Client ID")
        self.client_id_label.pack(pady=5)
        self.client_id_entry = ttk.Entry(self.add_loan_window)
        self.client_id_entry.pack(pady=5)

        self.amount_label = ttk.Label(self.add_loan_window, text="Amount")
        self.amount_label.pack(pady=5)
        self.amount_entry = ttk.Entry(self.add_loan_window)
        self.amount_entry.pack(pady=5)

        self.interest_rate_label = ttk.Label(self.add_loan_window, text="Interest Rate")
        self.interest_rate_label.pack(pady=5)
        self.interest_rate_entry = ttk.Entry(self.add_loan_window)
        self.interest_rate_entry.pack(pady=5)

        self.start_date_label = ttk.Label(self.add_loan_window, text="Start Date (YYYY-MM-DD)")
        self.start_date_label.pack(pady=5)
        self.start_date_entry = ttk.Entry(self.add_loan_window)
        self.start_date_entry.pack(pady=5)

        self.end_date_label = ttk.Label(self.add_loan_window, text="End Date (YYYY-MM-DD)")
        self.end_date_label.pack(pady=5)
        self.end_date_entry = ttk.Entry(self.add_loan_window)
        self.end_date_entry.pack(pady=5)

        self.save_button = ttk.Button(self.add_loan_window, text="Save", command=self.save_loan)
        self.save_button.pack(pady=20)

    def save_loan(self):
        client_id = self.client_id_entry.get()
        amount = self.amount_entry.get()
        interest_rate = self.interest_rate_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        if not client_id or not amount or not interest_rate or not start_date or not end_date:
            self.message_label.config(text="All fields are required")
            return

        try:
            conn = sqlite3.connect('financier.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO loans (clientId, amount, interestRate, startDate, endDate) VALUES (?, ?, ?, ?, ?)",
                           (client_id, amount, interest_rate, start_date, end_date))
            conn.commit()
            conn.close()

            self.add_loan_window.destroy()
            self.load_loans()
        except sqlite3.IntegrityError:
            self.message_label.config(text="An error occurred while saving the loan")
        except ValueError:
            self.message_label.config(text="Invalid input")