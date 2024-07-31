from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector
from mysql.connector import Error
import math
from datetime import *
from tkcalendar import *
from dateutil.relativedelta import relativedelta
from saveUpdateDelete import saveUpdateDeleteClass
from getDate import get_date



class payDailyClass(saveUpdateDeleteClass,get_date):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title("Pay Monthly")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========================
        # All Variables


        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_TransactionId=IntVar()
        self.var_AccountId=IntVar()
        self.var_CustomerName=StringVar()
        self.var_PaidTime=IntVar()
        self.var_PaidDate=IntVar()
        self.var_PaidAmount=IntVar()
        
        
        today = date.today()

        #========searchFrame=================

        SearchFrame=LabelFrame(self.root,text="View Person",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=320,y=20,width=800,height=70)

        #========options(drop down box)=================

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","TransactionId","AccountId"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=80,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=290,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=500,y=9,width=150,height=30)

        #========title=================

        title=Label(self.root,text="Transaction Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=30,y=100,width=1300)

        #========contents=================

        #========column_1=================

        lbl_accid=Label(self.root,text="Account ID",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=150)
        lbl_cusname=Label(self.root,text="Customer Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=200)
        lbl_customermobile=Label(self.root,text="Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=250)
        """lbl_paiddate=Label(self.root,text="Paid Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=300)"""
        

        

        txt_accid=Entry(self.root,textvariable=self.var_AccountId,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=150)
        txt_cusname=Entry(self.root,textvariable=self.var_CustomerName,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=200)
        txt_customermobile=Entry(self.root,textvariable=self.var_PaidAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=250)
        """self.txt_paidDate=DateEntry(self.root,selectmode='day', year=today.year, day=today.day, month=today.month, textvariable=self.var_PaidDate,font=("goudy old style",15,"bold"),bg="lightblue",state='readonly')
        self.txt_paidDate.place(x=220,y=300)"""
        

        btn_Getname=Button(self.root,text="Get Name",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2",command=self.get_name).place(x=100,y=370,width=150,height=30)
        btn_Pay=Button(self.root,text="Pay",font=("goudy old style",15),bg="green",fg="white",cursor="hand2",command=self.Pay).place(x=260,y=370,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=420,y=370,width=150,height=30)
        
        """btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=420,y=230,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=580,y=230,width=150,height=30)
        btn_cal_int=Button(self.root,text="Calculate",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.calculate).place(x=740,y=230,width=150,height=30)
        btn_cal_int=Button(self.root,text="Calculates",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=900,y=230,width=150,height=30)"""
        


        #========customer details=================

        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=565,relwidth=1,height=130)
        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)
        self.CustomerTable=ttk.Treeview(cus_frame,columns=("TransactionId","AccountId","CustomerName","PaidTime","PaidDate","PaidAmount"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)


        
        #================headings to show on screen==========
        self.CustomerTable.heading("TransactionId",text="TransactionId")
        self.CustomerTable.heading("AccountId",text="AccountId")
        self.CustomerTable.heading("CustomerName",text="Customer Name")
        self.CustomerTable.heading("PaidTime",text="Paid Time")
        self.CustomerTable.heading("PaidDate",text="Paid Date")
        self.CustomerTable.heading("PaidAmount",text="Paid Amount")
        self.CustomerTable["show"]="headings"
        

        #================headings width setting==========
        self.CustomerTable.column("TransactionId",width=180)
        self.CustomerTable.column("AccountId",width=180)
        self.CustomerTable.column("CustomerName",width=180)
        self.CustomerTable.column("PaidTime",width=180)
        self.CustomerTable.column("PaidDate",width=180)
        self.CustomerTable.column("PaidAmount",width=180)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data) 

        self.show()
        
    def Pay(self):
        try:
            #unique_int =lambda : self.calculate_current_unique_int()
            now = datetime.now()
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            minute = now.minute
            second = now.second
            current_date = now.strftime('%Y-%m-%d')
            current_time = now.strftime('%H:%M:%S')

            # Extract and format the current date and time
            self.var_TransactionId.set((day * 1000000 + hour * 10000 + minute * 100 + second))
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
                        messagebox.showerror("Error",f"Account Id should be required",parent=self.root)
                    if self.var_PaidAmount.get()=="":
                        messagebox.showerror("Error",f"PaidAmount  should be required",parent=self.root)
                    else:
                        cursor.execute("Insert into DailyTransactions (TransactionId,AccountId, CustomerName, PaidTime, PaidDatePaid, PaidAmount) values(%s,%s,%s,%s,%s,%s)",(
                                    self.var_TransactionId.get(),
                                    self.var_AccountId.get(),
                                    self.var_CustomerName.get(),
                                    current_time,
                                    current_date,
                                    self.var_PaidAmount.get()
                                        
                            ))
                        cursor.execute("""UPDATE Daily SET TotalAmountPaid = TotalAmountPaid + %s, DaysPaid = DaysPaid + 1 , TotalBalance = PrincipleAmount - TotalAmountPaid where AccountId = %s"""%(
                                    self.var_PaidAmount.get(),
                                    self.var_AccountId.get()
           
                            ))
                    con.commit()
                    messagebox.showinfo("Successfully paid",parent=self.root)
                    self.show()

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)


        except Exception as e:
            messagebox.showerror("Error",f"{str(e)}",parent=self.root)

    #================creating show function==========
    def get_name(self):
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
                    cursor.execute("""select CustomerName from Daily where AccountId=%s"""%(self.var_AccountId.get()))
                    rows=cursor.fetchall()
                    self.var_CustomerName.set(rows[0][0])
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)
    
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
                    cursor.execute("select * from DailyTransactions")
                    rows=cursor.fetchall()
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
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
        self.var_TransactionId.set(row[0]),
        self.var_AccountId.set(row[1]),
        self.var_CustomerName.set(row[2]),
        self.var_PaidTime.set(row[3]),
        self.var_PaidDate.set(row[4]),
        self.var_PaidAmount.set(row[5])
        """TransactionId AccountId CustomerName PaidTime PaidDate PaidAmount """
        





    """def calculate_current_unique_int(self):
        # Get the current date and time
        now = datetime.now()

        # Extract date and time components
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second

        # Combine components into a single integer
        unique_int = int(day * 1000000 + hour * 10000 + minute * 100 + second)
        print(unique_int)
        
        return unique_int"""

# Example usage
    

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
                        cursor.execute("select * from DailyTransactions where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            cursor.execute("""update DailyTransactions set CustomerName='%s', CustomerMobile='%s', SuretyName='%s', PrincipleAmount=%s, BorrowAmount=%s, IssueDate=%s, LastDate=%s, DaysRunning=%s, DaysPaid=%s, DaysBalance=%s, DailyTransactionsPay=%s, Due=%s, ExtraPay=%s, TotalAmountPaid=%s, TotalBalance=%s, PaperCharges=%s, PenalityAmount=%s, Rate=%s, OriginalAmount=%s, TotalProfit=%s, TotalLoss=%s, PresentBalance=%s, Status='%s', Proofs='%s' where AccountId=%s"""%(
                                        self.var_CustomerName.get(),
                                        self.var_CustomerMobile.get(),
                                        self.var_SuretyName.get(),
                                        self.var_PrincipleAmount.get(),
                                        self.var_BorrowAmount.get(),
                                        self.txt_issuedate.get_date(),
                                        self.txt_lastdate.get_date(),
                                        self.var_DaysRunning.get(),
                                        self.var_DaysPaid.get(),
                                        self.var_DaysBalance.get(),
                                        self.var_DailyPay.get(),
                                        self.var_Due.get(),
                                        self.var_ExtraPay.get(),
                                        self.var_TotalAmountPaid.get(),
                                        self.var_TotalBalance.get(),
                                        self.var_PaperCharges.get(),
                                        self.var_PenalityAmount.get(),
                                        self.var_Rate.get(),
                                        self.var_OriginalAmountTotal.get(),
                                        self.var_TotalProfit.get(),
                                        self.var_TotalLoss.get(),
                                        self.var_PresentBalance.get(),
                                        self.var_Status.get(),
                                        self.var_Proofs.get(),
                                        self.var_AccountId.get()
                            ))
                            con.commit()
                            messagebox.showinfo("Customer Details Updated Successfully",parent=self.root)
                            self.show()

                except Exception as e:
                    print(e)
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
                        cursor.execute("select * from DailyTransactions where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to Delter the Customer",parent=self.root)
                            if op==True:
                                cursor.execute("delete from DailyTransactions where AccountId=%s",(self.var_AccountId.get(),))
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
        self.var_PaidTime.set("")
        self.var_PaidDate.set("")
        self.var_PaidAmount.set("")
        
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
                        cursor.execute("select * from DailyTransactions where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
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



        
    def calculate(self):
        try:
            PrincipleAmount=float(self.var_PrincipleAmount.get())
            DaysRunning=float(self.var_DaysRunning.get())
            DaysPaid=float(self.var_DaysPaid.get())
            DaysBalance=float(self.var_DaysBalance.get())
            DailyPay=float(self.var_DailyPay.get())
            Due=float(self.var_Due.get())
            ExtraPay=float(self.var_ExtraPay.get())
            TotalAmountPaid=float(self.var_TotalAmountPaid.get())
            TotalBalance=float(self.var_TotalBalance.get())
            PenalityAmount=float(self.var_PenalityAmount.get())
            Rate=float(self.var_Rate.get())
            OriginalAmountTotal=float(self.var_OriginalAmountTotal.get())
            TotalProfit=float(self.var_TotalProfit.get())
            TotalLoss=float(self.var_TotalLoss.get())
            
            PaperCharges=float(self.var_PaperCharges.get()) * 0.01
            BorrowAmount=float( PrincipleAmount - ( PrincipleAmount * 0.1 ) )
            noOfDays =  int((self.txt_lastdate.get_date() - self.txt_issuedate.get_date()).days)
            self.var_DaysRunning.set(noOfDays)
            # calulating no of days
            self.var_PaperCharges.set(PaperCharges)
            self.var_BorrowAmount.set(BorrowAmount)
            newTotalAmountPaid = ( ( DaysPaid * ( PrincipleAmount / DaysRunning ) ) + ExtraPay )
            self.var_TotalAmountPaid.set(newTotalAmountPaid)
            self.var_TotalBalance.set(PrincipleAmount-newTotalAmountPaid)
            self.var_TotalProfit.set( ( ( ( PrincipleAmount - BorrowAmount ) / 100 ) *DaysPaid ) + PaperCharges+PenalityAmount)
            newOriginalAmount = ( ( BorrowAmount / 100 ) * DaysPaid)
            self.var_OriginalAmountTotal.set(newOriginalAmount)
            self.var_TotalLoss.set(BorrowAmount - newOriginalAmount)
        except Exception as e:
            # Handle case where the input is not a valid number
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    


 

if __name__ == "__main__":
    root = Tk()
    #root.attributes('-fullscreen',True)
    obj = payDailyClass(root)
    root.mainloop()