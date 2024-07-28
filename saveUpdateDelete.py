from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector
from mysql.connector import Error
import math
import datetime
from dateutil.relativedelta import relativedelta


class saveUpdateDeleteClass:
    """def __init__(self, root):
        self.root = root"""
        

#================creating save function==========
    def save(self):
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:

                    # Execute the query
                    if self.var_AccountId.get()=="":
                        messagebox.showerror("Error",f"Customer Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Main where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","This Customer Id already assigned, try a different one",parent=self.root)
                        else:
                            cursor.execute("Insert into Main (AccountId,CustomerName,CustomerMobile,SuretyName,PrincipleAmount,Months,TotalAmount,IssueDate,LastDate,EMI,PayingAmount,BalanceAmount,TotalAmountPaid,Balance,TotalMonthsPaid,PaperCharges,ExtraPay,TotalExtra,OriginalAmount,PenalityAmount,TotalProfit,TotalLoss,Status,Proofs,Interest) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_AccountId.get(),
                                        self.var_CustomerName.get(),
                                        self.var_CustomerMobile.get(),
                                        self.var_SuretyName.get(),
                                        self.var_PrincipleAmount.get(),
                                        self.var_Months.get(),
                                        self.var_TotalAmount.get(),
                                        self.var_IssueDate.get(),
                                        self.var_LastDate.get(),
                                        self.var_EMI.get(),
                                        self.var_PayingAmount.get(),
                                        self.var_BalanceAmount.get(),
                                        self.var_TotalAmountPaid.get(),
                                        self.var_Balance.get(),
                                        self.var_TotalMonthsPaid.get(),
                                        self.var_PaperCharges.get(),
                                        self.var_ExtraPay.get(),
                                        self.var_TotalExtra.get(),
                                        self.var_OriginalAmount.get(),
                                        self.var_PenalityAmount.get(),
                                        self.var_TotalProfit.get(),
                                        self.var_TotalLoss.get(),
                                        self.var_Status.get(),
                                        self.var_Proofs.get(),
                                        self.var_Interest.get()
                                        

                            ))
                            con.commit()
                            messagebox.showinfo("Successfully added new Customer",parent=self.root)
                            self.show()

                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)


        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    #================creating show function==========
    def show(self):
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:

                    # Execute the query
                    cursor.execute("select * from Main")
                    rows=cursor.fetchall()
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)
    #================Calculation function==========
    def monthly_details(self):
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:

                    # Execute the query
                    cursor.execute("select * from Main")
                    rows=cursor.fetchall()
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    '''amount = int(input("Amount:-"))
                    months = int(input("Months:-"))
                    interest = amount*months*0.03
                    total_amount = int(amount+interest)
                    emi = math.ceil(total_amount/months)
                    print(amount,total_amount, months,emi)
                    issue_date = datetime.date.today()
                    last_emi_date = relativedelta(months=months)
                    print(issue_date,issue_date+last_emi_date)
                    paper_charges = int(amount*0.01)
                    print(paper_charges)'''
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    #===========creating get_dat  function when were we click on below table show reflect on above==========

    def get_data(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        self.var_AccountId.set(row[0]),
        self.var_CustomerName.set(row[1]),
        self.var_CustomerMobile.set(row[2]),
        self.var_SuretyName.set(row[3]),
        self.var_PrincipleAmount.set(row[4]),
        self.var_Months.set(row[5]),
        self.var_TotalAmount.set(row[6]),
        self.var_IssueDate.set(row[7]),
        self.var_LastDate.set(row[8]),
        self.var_EMI.set(row[9]),
        self.var_PayingAmount.set(row[10]),
        self.var_BalanceAmount.set(row[11]),
        self.var_TotalAmountPaid.set(row[12]),
        self.var_Balance.set(row[13]),
        self.var_TotalMonthsPaid.set(row[14]),
        self.var_PaperCharges.set(row[15]),
        self.var_ExtraPay.set(row[16]),
        self.var_TotalExtra.set(row[17]),
        self.var_OriginalAmount.set(row[18]),
        self.var_PenalityAmount.set(row[19]),
        self.var_TotalProfit.set(row[20]),
        self.var_TotalLoss.set(row[21]),
        self.var_Status.set(row[22])
        self.var_Proofs.set(row[22])



    #================creating update function==========
    def update(self):
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:

                    # Execute the query
                    if self.var_AccountId.get()=="":
                        messagebox.showerror("Error",f"Customer ID should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Main where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            cursor.execute('update Main set AccountId=%s,CustomerName=%s,CustomerMobile=%s,SuretyName=%s,PrincipleAmount=%s,Months=%s,TotalAmount=%s,IssueDate=%s,LastDate=%s,EMI=%s,PayingAmount=%s,BalanceAmount=%s,TotalAmountPaid=%s,Balance=%s,TotalMonthsPaid=%s,PaperCharges=%s,ExtraPay=%s,TotalExtra=%s,OriginalAmount=%s,PenalityAmount=%s,TotalProfit=%s,TotalLoss=%s,Status=%s,Proofs=%s where AccountId=%s',(
                                        self.var_AccountId.get(),
                                        self.var_CustomerName.get(),
                                        self.var_CustomerMobile.get(),
                                        self.var_SuretyName.get(),
                                        self.var_PrincipleAmount.get(),
                                        self.var_Months.get(),
                                        self.var_TotalAmount.get(),
                                        self.var_IssueDate.get(),
                                        self.var_LastDate.get(),
                                        self.var_EMI.get(),
                                        self.var_PayingAmount.get(),
                                        self.var_BalanceAmount.get(),
                                        self.var_TotalAmountPaid.get(),
                                        self.var_Balance.get(),
                                        self.var_TotalMonthsPaid.get(),
                                        self.var_PaperCharges.get(),
                                        self.var_ExtraPay.get(),
                                        self.var_TotalExtra.get(),
                                        self.var_OriginalAmount.get(),
                                        self.var_PenalityAmount.get(),
                                        self.var_TotalProfit.get(),
                                        self.var_TotalLoss.get(),
                                        self.var_Status.get(),
                                        self.var_Proofs.get()

                            ))
                            con.commit()
                            messagebox.showinfo("Customer Details Updated Successfully",parent=self.root)
                            self.show()

                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)
    
    #===========cdelete function==========
    def delete(self):   
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:

                    # Execute the query
                    if self.var_AccountId.get()=="":
                        messagebox.showerror("Error",f"Customer Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Main where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to Delter the Customer",parent=self.root)
                            if op==True:
                                cursor.execute("delete from Main where AccountId=%s",(self.var_AccountId.get(),))
                                con.commit()
                                messagebox.showinfo("Delete","Customer Details Deleted Successfully",parent=self.root)
                                self.clear()

                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    #================creating show function==========
    def clear(self):
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_AccountId.set("")
        self.var_CustomerName.set("")
        self.var_CustomerMobile.set("")
        self.var_SuretyName.set("")
        self.var_PrincipleAmount.set("")
        self.var_Months.set("")
        self.var_TotalAmount.set("")
        self.var_IssueDate.set("")
        self.var_LastDate.set("")
        self.var_EMI.set("")
        self.var_PayingAmount.set("")
        self.var_BalanceAmount.set("")
        self.var_TotalAmountPaid.set("")
        self.var_Balance.set("")
        self.var_TotalMonthsPaid.set("")
        self.var_PaperCharges.set("")
        self.var_ExtraPay.set("")
        self.var_TotalExtra.set("")
        self.var_OriginalAmount.set("")
        self.var_PenalityAmount.set("")
        self.var_TotalProfit.set("")
        self.var_TotalLoss.set("")
        self.var_Status.set("")
        self.var_Proofs.set("")
        self.show()

    def search(self):
        try:
            # Connect to MySQL server
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dumnevijay@20',
                database="fms"
            )
            if con.is_connected():
                
                # Create a cursor object
                cursor = con.cursor()
                try:
                    # Execute the query
                    if self.var_searchby.get()=="Select":
                        messagebox.showerror("Error","Select the Search By option",parent=self.root)
                    elif self.var_searchby.get()=="":
                        messagebox.showerror("Error","Search Input should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Main where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                        rows=cursor.fetchall()
                        if len(rows)!=0:
                            self.CustomerTable.delete(*self.CustomerTable.get_children())
                            for row in rows:
                                self.CustomerTable.insert('',END,values=row)
                        else:
                            messagebox.showerror("Error","No record found",parent=self.root)
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)                   
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)           

    def calculate_interest(self, *args):
        try:
            months = float(self.var_Months.get())
            principleAmount = float(self.var_PrincipleAmount.get()) 
            interest = (principleAmount+(principleAmount * months * 0.03))
            self.var_TotalAmount.set(f"{interest:.2f}")
            self.calculate_paper_charges()
        except ValueError:
            # Handle case where the input is not a valid number
            self.var_Interest.set("")

    def calculate_paper_charges(self, *args):
        try:
            principleAmount = float(self.var_PrincipleAmount.get())
            interest = (principleAmount * 0.01)
            self.var_PaperCharges.set(f"{interest:.2f}")
        except ValueError:
            # Handle case where the input is not a valid number
            self.var_PaperCharges.set("")
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    def calculate_emi(self, *args):
        try:
            months = float(self.var_Months.get())
            TotalAmount = float(self.var_TotalAmount.get())
            interest = (TotalAmount // months)
            self.var_EMI.set(f"{interest:.2f}")
        except ValueError:
            # Handle case where the input is not a valid number
            self.var_PaperCharges.set("")
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)


"""if __name__ == "__main__":
    root = Tk()
    #root.attributes('-fullscreen',True)
    obj = saveUpdateDeleteClass(root)
    root.mainloop()"""