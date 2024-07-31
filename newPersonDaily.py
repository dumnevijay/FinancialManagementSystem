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
from pay_daily import payDailyClass


class sample(saveUpdateDeleteClass,get_date):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title("Financier Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========================
        # All Variables


        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_AccountId=IntVar()
        self.var_CustomerName=StringVar()
        self.var_CustomerMobile=StringVar()
        self.var_SuretyName=StringVar()
        self.var_PrincipleAmount=IntVar()
        self.var_BorrowAmount=IntVar()
        self.var_IssueDate=StringVar()
        self.var_LastDate=StringVar()
        self.var_DaysRunning=IntVar()
        self.var_DaysPaid=IntVar()
        self.var_DaysBalance=IntVar()
        self.var_DailyPay=IntVar()
        self.var_Due=IntVar()
        self.var_ExtraPay=IntVar()
        self.var_TotalAmountPaid=IntVar()
        self.var_TotalBalance=IntVar()
        self.var_PaperCharges=IntVar()
        self.var_PenalityAmount=IntVar()
        self.var_Rate=IntVar()
        self.var_OriginalAmountTotal=IntVar()
        self.var_TotalProfit=IntVar()
        self.var_TotalLoss=IntVar()
        self.var_Status=StringVar()
        self.var_PresentBalance=IntVar()
        self.var_Proofs=StringVar()

        today = date.today()

        #========searchFrame=================

        SearchFrame=LabelFrame(self.root,text="View Person",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=320,y=20,width=800,height=70)

        #========options(drop down box)=================

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","AccountId","CustomerName","CustomerMobile","SuretyName"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=80,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=290,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=500,y=9,width=150,height=30)

        #========title=================

        title=Label(self.root,text="Person Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=30,y=100,width=1300)

        #========contents=================

        #========column_1=================

        lbl_accid=Label(self.root,text="Account ID",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=150)
        lbl_cusname=Label(self.root,text="Customer Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=200)
        lbl_customermobile=Label(self.root,text="Customer Mobile",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=250)
        lbl_suretyname=Label(self.root,text="Surety Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=300)
        lbl_issuedate=Label(self.root,text="Issue Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=350)
        lbl_lastdate=Label(self.root,text="Last Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=400)
        lbl_principleamount=Label(self.root,text="Principle Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=450)
        lbl_barrowamount=Label(self.root,text="Barrow Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=500)

        

        txt_accid=Entry(self.root,textvariable=self.var_AccountId,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=150)
        txt_cusname=Entry(self.root,textvariable=self.var_CustomerName,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=200)
        txt_customermobile=Entry(self.root,textvariable=self.var_CustomerMobile,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=250)
        txt_suretyname=Entry(self.root,textvariable=self.var_SuretyName,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=300)
        self.txt_issuedate=DateEntry(self.root,selectmode='day', year=today.year, day=today.day, month=today.month, textvariable=self.var_IssueDate,font=("goudy old style",15,"bold"),bg="lightblue")
        self.txt_issuedate.place(x=220,y=350)
        """self.txt_lastdate=DateEntry(self.root,selectmode='day', year=today.year, day=today.day, month=today.month, textvariable=self.var_LastDate,font=("goudy old style",15,"bold"),bg="lightblue")
        self.txt_lastdate.place(x=220,y=400)"""
        txt_lastdate=Entry(self.root,textvariable=self.var_LastDate,font=("goudy old style",15,"bold"),bg="lightblue",state='readonly').place(x=220,y=400)
        txt_principleamount=Entry(self.root,textvariable=self.var_PrincipleAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=450)
        txt_barrowamount=Entry(self.root,textvariable=self.var_BorrowAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=500)

        #========column_2=================

        lbl_daysrunning=Label(self.root,text="Days Running",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=150)
        lbl_dayspaid=Label(self.root,text="Days Paid",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=200)
        lbl_daysbalance=Label(self.root,text="Days Balance",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=250)
        lbl_due=Label(self.root,text="Due",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=300)
        lbl_dailypay=Label(self.root,text="Daily Pay",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=350)
        lbl_extrapay=Label(self.root,text="Extra Pay",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=400)
        lbl_totalamountpaid=Label(self.root,text="Total Amount Paid",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=450)
        lbl_balance=Label(self.root,text="Total Balance",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=500)
        
              
        txt_daysrunning=Entry(self.root,textvariable=self.var_DaysRunning,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=150)
        txt_dayspaid=Entry(self.root,textvariable=self.var_DaysPaid,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=200)
        txt_daysbalance=Entry(self.root,textvariable=self.var_DaysBalance,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=250)
        txt_due=Entry(self.root,textvariable=self.var_Due,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=300)
        txt_dailypay=Entry(self.root,textvariable=self.var_DailyPay,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=350)
        txt_extrapay=Entry(self.root,textvariable=self.var_ExtraPay,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=400)
        txt_totalamountpaid=Entry(self.root,textvariable=self.var_TotalAmountPaid,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=450)
        txt_balance=Entry(self.root,textvariable=self.var_TotalBalance,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=500)


        #========column_3=================

        lbl_papercharges=Label(self.root,text="Paper Charges",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=150)
        lbl_penalityamount=Label(self.root,text="Penality Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=190)
        lbl_Rate=Label(self.root,text="Rate ",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=230)
        lbl_originalamount=Label(self.root,text="Original Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=275)
        lbl_PresentBalance=Label(self.root,text="Present Balance",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=320)
        lbl_totalprofit=Label(self.root,text="Total Profit",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=360)
        lbl_totallosss=Label(self.root,text="Total Loss",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=410)
        lbl_status=Label(self.root,text="Status",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=460)
        lbl_proofs=Label(self.root,text="Proofs",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=500)
    
    
        txt_papercharges=Entry(self.root,textvariable=self.var_PaperCharges,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=150)
        txt_penalityamount=Entry(self.root,textvariable=self.var_PenalityAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=190)
        txt_rate=Entry(self.root,textvariable=self.var_Rate,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=230)
        txt_originalamount=Entry(self.root,textvariable=self.var_OriginalAmountTotal,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=275)
        txt_PresentBalance=Entry(self.root,textvariable=self.var_PresentBalance,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=320)
        txt_totalprofit=Entry(self.root,textvariable=self.var_TotalProfit,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=360)
        txt_totallosss=Entry(self.root,textvariable=self.var_TotalLoss,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=410)
        txt_status=Entry(self.root,textvariable=self.var_Status,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=460)
        txt_proofs=Entry(self.root,textvariable=self.var_Proofs,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=500)
        
        
    

        #========address field=================
        '''
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=300)
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightblue")
        self.txt_address.place(x=200,y=310,width=200,height=100) '''
        
        #========buttons of update on database=================

        btn_save=Button(self.root,text="Save",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2",command=self.save).place(x=100,y=535,width=150,height=30)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="green",fg="white",cursor="hand2",command=self.update).place(x=260,y=535,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=420,y=535,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=580,y=535,width=150,height=30)
        btn_cal_int=Button(self.root,text="Calculate Days",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.calculate_days).place(x=740,y=535,width=150,height=30)
        btn_cal_int=Button(self.root,text="Calculates",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=900,y=535,width=150,height=30)
        btn_dailypay=Button(self.root,text="Daily Pay",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.dailyPay).place(x=1065,y=535,width=150,height=30)
        btn_dailypay=Button(self.root,text="Refresh",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.personshow).place(x=1220,y=535,width=100,height=30)
        


        #========customer details=================

        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=565,relwidth=1,height=130)
        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)
        self.CustomerTable=ttk.Treeview(cus_frame,columns=("AccountId","CustomerName","CustomerMobile","SuretyName","PrincipleAmount","BorrowAmount","IssueDate","LastDate","DaysRunning","DaysPaid","DaysBalance","DailyPay","Due","ExtraPay","TotalAmountPaid","TotalBalance","PaperCharges","PenalityAmount","Rate","OriginalAmountTotal","TotalProfit","TotalLoss","PresentBalance","Status","Proofs"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)


        #================headings to show on screen==========
        self.CustomerTable.heading("AccountId",text="AccountId")
        self.CustomerTable.heading("CustomerName",text="Customer Name")
        self.CustomerTable.heading("CustomerMobile",text="CustomerMobile")
        self.CustomerTable.heading("SuretyName",text="Surety Name")
        self.CustomerTable.heading("PrincipleAmount",text="PrincipleAmount")
        self.CustomerTable.heading("BorrowAmount",text="Borrow Amount")
        self.CustomerTable.heading("IssueDate",text="IssueDate")
        self.CustomerTable.heading("LastDate",text="Last Date")
        self.CustomerTable.heading("DaysRunning",text="Days Running")
        self.CustomerTable.heading("DaysPaid",text="Days Paid")
        self.CustomerTable.heading("DaysBalance",text="Days Balance")
        self.CustomerTable.heading("DailyPay",text="Daily Pay")
        self.CustomerTable.heading("Due",text="TotalAmountPaid")
        self.CustomerTable.heading("ExtraPay",text="Extra Pay")
        self.CustomerTable.heading("TotalAmountPaid",text="Total Amount Paid")
        self.CustomerTable.heading("TotalBalance",text="Total Balance")
        self.CustomerTable.heading("PaperCharges",text="Paper Charges")
        self.CustomerTable.heading("PenalityAmount",text="Penality Amount")
        self.CustomerTable.heading("Rate",text="Rate")
        self.CustomerTable.heading("OriginalAmountTotal",text="Original Amount")
        self.CustomerTable.heading("TotalProfit",text="Total Profit")
        self.CustomerTable.heading("TotalLoss",text="Total Loss")
        self.CustomerTable.heading("PresentBalance",text="PresentBalance")
        self.CustomerTable.heading("Status",text="Status")
        self.CustomerTable.heading("Proofs",text="Proofs")
        self.CustomerTable["show"]="headings"
        

        #================headings width setting==========
        self.CustomerTable.column("AccountId",width=70)
        self.CustomerTable.column("CustomerName",width=180)
        self.CustomerTable.column("CustomerMobile",width=80)
        self.CustomerTable.column("SuretyName",width=180)
        self.CustomerTable.column("PrincipleAmount",width=110)
        self.CustomerTable.column("BorrowAmount",width=110)
        self.CustomerTable.column("IssueDate",width=100)
        self.CustomerTable.column("LastDate",width=100)
        self.CustomerTable.column("DaysRunning",width=150)
        self.CustomerTable.column("DaysPaid",width=80)
        self.CustomerTable.column("DaysBalance",width=100)
        self.CustomerTable.column("DailyPay",width=100)
        self.CustomerTable.column("Due",width=100)
        self.CustomerTable.column("ExtraPay",width=100)
        self.CustomerTable.column("TotalAmountPaid",width=90)
        self.CustomerTable.column("TotalBalance",width=100)
        self.CustomerTable.column("PaperCharges",width=100)
        self.CustomerTable.column("PenalityAmount",width=100)
        self.CustomerTable.column("Rate",width=100)
        self.CustomerTable.column("OriginalAmountTotal",width=100)
        self.CustomerTable.column("TotalProfit",width=100)
        self.CustomerTable.column("TotalLoss",width=100)
        self.CustomerTable.column("PresentBalance",width=100)
        self.CustomerTable.column("Status",width=100)
        self.CustomerTable.column("Proofs",width=100)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)

        self.personshow()
        
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
                        messagebox.showerror("Error",f"Account Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Daily where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","This Customer Id already assigned, try a different one",parent=self.root)
                        else:
                            cursor.execute("Insert into Daily (AccountId, CustomerName, CustomerMobile, SuretyName, PrincipleAmount, BorrowAmount, IssueDate, LastDate, DaysRunning, DaysPaid, DaysBalance, DailyPay, Due, ExtraPay, TotalAmountPaid, TotalBalance, PaperCharges, PenalityAmount, Rate, OriginalAmount, TotalProfit, TotalLoss, PresentBalance, Status, Proofs) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_AccountId.get(),
                                        self.var_CustomerName.get(),
                                        self.var_CustomerMobile.get(),
                                        self.var_SuretyName.get(),
                                        self.var_PrincipleAmount.get(),
                                        self.var_BorrowAmount.get(),
                                        self.txt_issuedate.get_date(),
                                        self.var_LastDate.get(),
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
                                        self.var_Proofs.get()
                                        
                            ))
                            con.commit()
                            messagebox.showinfo("Successfully added new Customer",parent=self.root)
                            self.show()

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)


        except Exception as e:
            messagebox.showerror("Error",f"{str(e)}",parent=self.root)

    #================creating show function==========
    def personshow(self):
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
                    cursor.execute("select * from Daily")
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
        self.var_AccountId.set(row[0]),
        self.var_CustomerName.set(row[1]),
        self.var_CustomerMobile.set(row[2]),
        self.var_SuretyName.set(row[3]),
        self.var_PrincipleAmount.set(row[4]),
        self.var_BorrowAmount.set(row[5]),
        self.var_IssueDate.set(row[6]),
        self.var_LastDate.set(row[7]),
        self.var_DaysRunning.set(row[8]),
        self.var_DaysPaid.set(row[9]),
        self.var_DaysBalance.set(row[10]),
        self.var_DailyPay.set(row[11]),
        self.var_Due.set(row[12]),
        self.var_ExtraPay.set(row[13]),
        self.var_TotalAmountPaid.set(row[14]),
        self.var_TotalBalance.set(row[15]),
        self.var_PaperCharges.set(row[16]),
        self.var_PenalityAmount.set(row[17]),
        self.var_Rate.set(row[18]),
        self.var_OriginalAmountTotal.set(row[19]),
        self.var_TotalProfit.set(row[20]),
        self.var_TotalLoss.set(row[21]),
        self.var_PresentBalance.set(row[22]),
        self.var_Status.set(row[23]),
        self.var_Proofs.set(row[24])
        



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
                        cursor.execute("select * from Daily where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            cursor.execute("""update Daily set CustomerName='%s', CustomerMobile='%s', SuretyName='%s', PrincipleAmount=%s, BorrowAmount=%s, IssueDate=%s, LastDate=%s, DaysRunning=%s, DaysPaid=%s, DaysBalance=%s, DailyPay=%s, Due=%s, ExtraPay=%s, TotalAmountPaid=%s, TotalBalance=%s, PaperCharges=%s, PenalityAmount=%s, Rate=%s, OriginalAmount=%s, TotalProfit=%s, TotalLoss=%s, PresentBalance=%s, Status='%s', Proofs='%s' where AccountId=%s"""%(
                                        self.var_CustomerName.get(),
                                        self.var_CustomerMobile.get(),
                                        self.var_SuretyName.get(),
                                        self.var_PrincipleAmount.get(),
                                        self.var_BorrowAmount.get(),
                                        self.txt_issuedate.get_date(),
                                        self.var_LastDate.get(),
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
                            self.personshow()

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
                        cursor.execute("select * from Daily where AccountId=%s",(self.var_AccountId.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to Delter the Customer",parent=self.root)
                            if op==True:
                                cursor.execute("delete from Daily where AccountId=%s",(self.var_AccountId.get(),))
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
        self.var_BorrowAmount.set("")
        self.var_IssueDate.set("")
        self.var_LastDate.set("")
        self.var_DaysRunning.set("")
        self.var_DaysPaid.set("")
        self.var_DaysBalance.set("")
        self.var_DailyPay.set("")
        self.var_Due.set("")
        self.var_ExtraPay.set("")
        self.var_TotalAmountPaid.set("")
        self.var_TotalBalance.set("")
        self.var_PaperCharges.set("")
        self.var_PenalityAmount.set("")
        self.var_Rate.set("")
        self.var_OriginalAmountTotal.set("")
        self.var_TotalProfit.set("")
        self.var_TotalLoss.set("")
        self.var_Status.set("")
        self.var_PresentBalance.set("")
        self.var_Proofs.set("")
        self.personshow()

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
                        cursor.execute("select * from Daily where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
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

    def calculate_days(self):
        try:
            # calulating no of days
            current_date = datetime.now().date()
            future_date = current_date + timedelta(days=self.var_DaysRunning.get())
            self.var_LastDate.set(future_date.strftime('%d-%m-%Y'))
    
        
        except Exception as e:
            # Handle case where the input is not a valid number
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    def calculate_papercharges(self):
        try:
            PrincipleAmount=float(self.var_PrincipleAmount.get())
            PaperCharges=PrincipleAmount * 0.01
            self.var_PaperCharges.set(PaperCharges)
            BorrowAmount=float( PrincipleAmount - ( PrincipleAmount * 0.1 ) )
            self.var_BorrowAmount.set(BorrowAmount)
            
        
        except Exception as e:
            # Handle case where the input is not a valid number
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)
    def calculates(self):
        try:
            PrincipleAmount=float(self.var_PrincipleAmount.get())
            PaperCharges=PrincipleAmount * 0.01
            self.var_PaperCharges.set(PaperCharges)
            BorrowAmount=float( PrincipleAmount - ( PrincipleAmount * 0.1 ) )
            self.var_BorrowAmount.set(BorrowAmount)
            
        
        except Exception as e:
            # Handle case where the input is not a valid number
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    def dailyPay(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = payDailyClass(self.new_win)
 

if __name__ == "__main__":
    root = Tk()
    #root.attributes('-fullscreen',True)
    obj = sample(root)
    root.mainloop()