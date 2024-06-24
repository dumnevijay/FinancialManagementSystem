import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def create_db():
    try:
        # Connect to MySQL server
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='dumnevijay@20'
        )
        if con.is_connected():
            
            # Create a cursor object
            cursor = con.cursor()
            
            # Execute the query
            cursor.execute("CREATE DATABASE IF NOT EXISTS fms")
            cursor.execute("use fms")

            #============creating the table====================

            create_table_query = """
            CREATE TABLE IF NOT EXISTS Customers (
                ID INT AUTO_INCREMENT,
                CustomerName TEXT,
                Gender TEXT,
                SuretyName TEXT,
                PhoneNumber TEXT,
                AlternateNumber TEXT,
                AccountType TEXT,
                Amount TEXT,
                Months TEXT,
                IssueDate TEXT,
                LastDate TEXT,
                Proofs TEXT,
                Address TEXT,
                PRIMARY KEY (ID)
            )
            """
            create_transaction_table_query = """
            CREATE TABLE IF NOT EXISTS Transactions (
                SerialNo INT AUTO_INCREMENT,
                CustomerName TEXT,
                SuretyName TEXT,
                PrincipleAmounat TEXT,
                BarrowAmount TEXT,
                IssueDateEMI TEXT,
                LastDateEMI TEXT,
                DaysRunning TEXT,
                DaysPaid TEXT,
                DaysBalance TEXT,
                Due TEXT,
                PresentBalance TEXT,
                ExtraPay TEXT,
                TotalPaidAmount TEXT,
                TotalBalance TEXT,
                PaperCharges TEXT,
                PenaltyAmount TEXT,
                Rate TEXT,
                OriginalAmountTotal TEXT,
                Profit TEXT,
                Loss TEXT,
                Status TEXT,
                PRIMARY KEY (SerialNo)
            )
            """
            cursor.execute(create_table_query)
            cursor.execute(create_transaction_table_query)
            
    except Error as e:
        messagebox.showerror(f"Error: 'database error {e}'")
    
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Call the function to create the database
create_db()
