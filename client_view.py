import tkinter as tk
from tkinter import ttk
import sqlite3

class ClientView:
    def __init__(self, root):
        self.root = root
        self.root.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Contact", "Email"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Email", text="Email")
        self.tree.pack(fill="both", expand=True)

        self.load_clients()

        self.add_client_button = ttk.Button(self.root, text="Add Client", command=self.add_client)
        self.add_client_button.pack(pady=10)

    def load_clients(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def add_client(self):
        self.add_client_window = tk.Toplevel(self.root)
        self.add_client_window.title("Add Client")

        self.name_label = ttk.Label(self.add_client_window, text="Name")
        self.name_label.pack(pady=5)
        self.name_entry = ttk.Entry(self.add_client_window)
        self.name_entry.pack(pady=5)

        self.contact_label = ttk.Label(self.add_client_window, text="Contact")
        self.contact_label.pack(pady=5)
        self.contact_entry = ttk.Entry(self.add_client_window)
        self.contact_entry.pack(pady=5)

        self.email_label = ttk.Label(self.add_client_window, text="Email")
        self.email_label.pack(pady=5)
        self.email_entry = ttk.Entry(self.add_client_window)
        self.email_entry.pack(pady=5)

        self.save_button = ttk.Button(self.add_client_window, text="Save", command=self.save_client)
        self.save_button.pack(pady=20)

    def save_client(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        if not name:
            self.message_label.config(text="Name is required")
            return

        try:
            conn = sqlite3.connect('financier.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clients (name, contact, email) VALUES (?, ?, ?)", (name, contact, email))
            conn.commit()
            conn.close()

            self.add_client_window.destroy()
            self.load_clients()
        except sqlite3.IntegrityError:
            self.message_label.config(text="An error occurred while saving the client")
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
        self.tree.delete(*self.tree.get_children())
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

        self.message_label = ttk.Label(self.add_loan_window, text="", foreground="red")
        self.message_label.pack(pady=5)

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
            amount = float(amount)
            interest_rate = float(interest_rate)
        except ValueError:
            self.message_label.config(text="Amount and Interest Rate must be numeric")
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