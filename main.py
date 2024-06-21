import tkinter as tk
from tkinter import ttk
from client_view import ClientView
from loan_view import LoanView
from report_view import ReportView
from database import initialize_db

class FinancierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financier Management System")

        self.tabControl = ttk.Notebook(self.root)

        self.tab_clients = ttk.Frame(self.tabControl)
        self.tab_loans = ttk.Frame(self.tabControl)
        self.tab_reports = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_clients, text='Clients')
        self.tabControl.add(self.tab_loans, text='Loans')
        self.tabControl.add(self.tab_reports, text='Reports')

        self.tabControl.pack(expand=1, fill="both")

        self.client_view = ClientView(self.tab_clients)
        self.loan_view = LoanView(self.tab_loans)
        self.report_view = ReportView(self.tab_reports)

if __name__ == '__main__':
    initialize_db()
    root = tk.Tk()
    app = FinancierApp(root)
    root.mainloop()
