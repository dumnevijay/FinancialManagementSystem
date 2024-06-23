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
                RepayDate TEXT,
                Proofs TEXT,
                Address TEXT,
                PRIMARY KEY (ID)
            )
            """
            cursor.execute(create_table_query)
            
    except Error as e:
        messagebox.showerror(f"Error: 'database error {e}'")
    
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Call the function to create the database
create_db()
