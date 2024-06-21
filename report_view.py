import tkinter as tk
from tkinter import ttk
import sqlite3

class ReportView:
    def __init__(self, root):
        self.root = root
        self.root.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.report_type_label = ttk.Label(self.frame, text="Select Report Type:")
        self.report_type_label.pack(pady=5)

        self.report_type = tk.StringVar()
        self.report_type_combobox = ttk.Combobox(self.frame, textvariable=self.report_type)
        self.report_type_combobox['values'] = ('Monthly', 'Yearly', 'Client Summary', 'Overall Performance')
        self.report_type_combobox.current(0)
        self.report_type_combobox.pack(pady=5)

        self.generate_button = ttk.Button(self.frame, text="Generate Report", command=self.generate_report)
        self.generate_button.pack(pady=10)

        self.report_text = tk.Text(self.frame, wrap='word', height=20, width=80)
        self.report_text.pack(pady=5, fill="both", expand=True)

    def generate_report(self):
        report_type = self.report_type.get()
        self.report_text.delete(1.0, tk.END)

        if report_type == 'Monthly':
            self.generate_monthly_report()
        elif report_type == 'Yearly':
            self.generate_yearly_report()
        elif report_type == 'Client Summary':
            self.generate_client_summary_report()
        elif report_type == 'Overall Performance':
            self.generate_overall_performance_report()

    def generate_monthly_report(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT strftime('%Y-%m', startDate) as month, SUM(amount * interestRate / 100) as profit
        FROM loans
        GROUP BY month
        """)
        rows = cursor.fetchall()
        report = "Monthly Report:\n"
        for row in rows:
            report += f"Month: {row[0]}, Profit: {row[1]:.2f}\n"
        self.report_text.insert(tk.END, report)
        conn.close()

    def generate_yearly_report(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT strftime('%Y', startDate) as year, SUM(amount * interestRate / 100) as profit
        FROM loans
        GROUP BY year
        """)
        rows = cursor.fetchall()
        report = "Yearly Report:\n"
        for row in rows:
            report += f"Year: {row[0]}, Profit: {row[1]:.2f}\n"
        self.report_text.insert(tk.END, report)
        conn.close()

    def generate_client_summary_report(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT clients.name, SUM(loans.amount * loans.interestRate / 100) as profit
        FROM loans
        JOIN clients ON loans.clientId = clients.id
        GROUP BY clients.name
        """)
        rows = cursor.fetchall()
        report = "Client Summary Report:\n"
        for row in rows:
            report += f"Client: {row[0]}, Profit: {row[1]:.2f}\n"
        self.report_text.insert(tk.END, report)
        conn.close()

    def generate_overall_performance_report(self):
        conn = sqlite3.connect('financier.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT SUM(amount * interestRate / 100) as profit
        FROM loans
        """)
        row = cursor.fetchone()
        report = "Overall Performance Report:\n"
        report += f"Total Profit: {row[0]:.2f}\n"
        self.report_text.insert(tk.END, report)
        conn.close()
