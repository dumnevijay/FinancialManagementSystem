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

            create_main_table_query = """
            CREATE TABLE IF NOT EXISTS Main (
                AccountId INT AUTO_INCREMENT,
                CustomerName VARCHAR(100),
                CustomerMobile VARCHAR(100),
                SuretyName VARCHAR(100),
                PrincipleAmount VARCHAR(100),
                Months VARCHAR(100),
                TotalAmount VARCHAR(100),
                IssueDate VARCHAR(100),
                LastDate VARCHAR(100),
                EMI VARCHAR(100),
                PayingAmount VARCHAR(100),
                BalanceAmount VARCHAR(100),
                TotalAmountPaid VARCHAR(100),
                Balance VARCHAR(100),
                TotalMonthsPaid VARCHAR(100),
                PaperCharges VARCHAR(100),
                ExtraPay VARCHAR(100),
                TotalExtra VARCHAR(100),
                OriginalAmount VARCHAR(100),
                PenalityAmount VARCHAR(100),
                TotalProfit VARCHAR(100),
                TotalLoss VARCHAR(100),
                Status VARCHAR(100),
                Proofs VARCHAR(100),
                Interest VARCHAR(100),
                PRIMARY KEY (AccountId)
            )
            """
            create_daily_table_query = """
            CREATE TABLE IF NOT EXISTS DailyTable (
                AccountId INT AUTO_INCREMENT,
                CustomerName VARCHAR(100),
                CustomerMobile VARCHAR(100),
                SuretyName VARCHAR(100),
                PrincipleAmount VARCHAR(100),
                BorrowAmount VARCHAR(100),
                IssueDate VARCHAR(100),
                LastDate VARCHAR(100),
                DaysRunning VARCHAR(100),
                DaysPaid VARCHAR(100),
                DaysBalance VARCHAR(100),
                DailyPay VARCHAR(100),
                Due VARCHAR(100),
                ExtraPay VARCHAR(100),
                TotalAmountPaid VARCHAR(100),
                TotalBalance VARCHAR(100),
                PaperCharges VARCHAR(100),
                PenalityAmount VARCHAR(100),
                Rate VARCHAR(100),
                OriginalAmount VARCHAR(100),
                TotalProfit VARCHAR(100),
                TotalLoss VARCHAR(100),
                Status VARCHAR(100),
                Proofs VARCHAR(100),
                PRIMARY KEY (AccountId)
            )
            """

            cursor.execute(create_table_query)
            cursor.execute(create_transaction_table_query)
            cursor.execute(create_main_table_query)
            cursor.execute(create_daily_table_query)


            
    except Error as e:
        messagebox.showerror(f"Error: 'database error {e}'")
    
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Call the function to create the database
create_db()
