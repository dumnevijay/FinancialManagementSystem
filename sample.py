from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector
from mysql.connector import Error
import math
import datetime
from dateutil.relativedelta import relativedelta
from saveUpdateDelete import saveUpdateDeleteClass


class sample(saveUpdateDeleteClass):
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

        self.var_AccountId=StringVar()
        self.var_CustomerName=StringVar()
        self.var_CustomerMobile=StringVar()
        self.var_SuretyName=StringVar()
        self.var_PrincipleAmount=StringVar()
        self.var_Months=StringVar()
        self.var_TotalAmount=StringVar()
        self.var_IssueDate=StringVar()
        self.var_LastDate=StringVar()
        self.var_EMI=StringVar()
        self.var_PayingAmount=StringVar()
        self.var_BalanceAmount=StringVar()
        self.var_TotalAmountPaid=StringVar()
        self.var_Balance=StringVar()
        self.var_TotalMonthsPaid=StringVar()
        self.var_PaperCharges=StringVar()
        self.var_ExtraPay=StringVar()
        self.var_TotalExtra=StringVar()
        self.var_OriginalAmount=StringVar()
        self.var_PenalityAmount=StringVar()
        self.var_TotalProfit=StringVar()
        self.var_TotalLoss=StringVar()
        self.var_Status=StringVar()
        self.var_Proofs=StringVar()
        self.var_Interest=StringVar()

        #========searchFrame=================

        SearchFrame=LabelFrame(self.root,text="View Person",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=320,y=20,width=800,height=70)

        #========options(drop down box)=================

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","AccountId","CustomerName","CustomerMobile"),state="readonly",justify=CENTER,font=("goudy old style",15))
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
        lbl_principleamount=Label(self.root,text="Principle Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=350)
        lbl_months=Label(self.root,text="Months",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=400)
        lbl_totalamount=Label(self.root,text="Total Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=450)
        lbl_totalmonthspaid=Label(self.root,text="Total Months Paid",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=500)

        txt_accid=Entry(self.root,textvariable=self.var_AccountId,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=150)
        txt_cusname=Entry(self.root,textvariable=self.var_CustomerName,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=200)
        txt_customermobile=Entry(self.root,textvariable=self.var_CustomerMobile,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=250)
        txt_suretyname=Entry(self.root,textvariable=self.var_SuretyName,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=300)
        txt_principleamount=Entry(self.root,textvariable=self.var_PrincipleAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=350)
        txt_months=Entry(self.root,textvariable=self.var_Months,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=400)
        txt_totalamount=Entry(self.root,textvariable=self.var_TotalAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=450)
        txt_totalmonthspaid=Entry(self.root,textvariable=self.var_TotalMonthsPaid,font=("goudy old style",15,"bold"),bg="lightblue").place(x=220,y=500)

        #========column_2=================

        lbl_issuedate=Label(self.root,text="Issue Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=150)
        lbl_lastdate=Label(self.root,text="Last Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=200)
        lbl_EMI=Label(self.root,text="EMI",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=250)
        lbl_payingamount=Label(self.root,text="Paying Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=300)
        lbl_balanceamount=Label(self.root,text="Balance Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=350)
        lbl_totalamountpaid=Label(self.root,text="Total Amount Paid",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=400)
        lbl_balance=Label(self.root,text="Balance",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=450)
        lbl_status=Label(self.root,text="Status",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=455,y=500)
              
        txt_issuedate=Entry(self.root,textvariable=self.var_IssueDate,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=150)
        txt_lastdate=Entry(self.root,textvariable=self.var_LastDate,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=200)
        txt_EMI=Entry(self.root,textvariable=self.var_EMI,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=250)
        txt_payingamount=Entry(self.root,textvariable=self.var_PayingAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=300)
        txt_balanceamount=Entry(self.root,textvariable=self.var_BalanceAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=350)
        txt_totalamountpaid=Entry(self.root,textvariable=self.var_TotalAmountPaid,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=400)
        txt_balance=Entry(self.root,textvariable=self.var_Balance,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=450)
        txt_status=Entry(self.root,textvariable=self.var_Status,font=("goudy old style",15,"bold"),bg="lightblue").place(x=620,y=500)


        #========column_3=================

        lbl_papercharges=Label(self.root,text="Paper Charges",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=150)
        lbl_extrapay=Label(self.root,text="Extra Pay",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=200)
        lbl_totalextra=Label(self.root,text="Total Extra",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=250)
        lbl_originalamount=Label(self.root,text="Original Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=300)
        lbl_penalityamount=Label(self.root,text="Penality Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=350)
        lbl_totalprofit=Label(self.root,text="Total Profit",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=400)
        lbl_totallosss=Label(self.root,text="Total Loss",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=450)
        lbl_interest=Label(self.root,text="Interest",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=840,y=500)
    
    
        txt_papercharges=Entry(self.root,textvariable=self.var_PaperCharges,font=("goudy old style",15,"bold"),bg="lightblue",state='readonly').place(x=995,y=150)
        txt_extrapay=Entry(self.root,textvariable=self.var_ExtraPay,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=200)
        txt_totalextra=Entry(self.root,textvariable=self.var_TotalExtra,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=250)
        txt_originalamount=Entry(self.root,textvariable=self.var_OriginalAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=300)
        txt_penalityamount=Entry(self.root,textvariable=self.var_PenalityAmount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=350)
        txt_totalprofit=Entry(self.root,textvariable=self.var_TotalProfit,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=400)
        txt_totallosss=Entry(self.root,textvariable=self.var_TotalLoss,font=("goudy old style",15,"bold"),bg="lightblue").place(x=995,y=450)
        txt_interest=Entry(self.root,textvariable=self.var_Interest,font=("goudy old style",15,"bold"),bg="lightblue",state='readonly').place(x=995,y=500)
        
        
    

        #========address field=================
        '''
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=300)
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightblue")
        self.txt_address.place(x=200,y=310,width=200,height=100) '''
        
        #========buttons of update on database=================

        btn_save=Button(self.root,text="Save",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2",command=self.save).place(x=200,y=535,width=150,height=30)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="green",fg="white",cursor="hand2",command=self.update).place(x=370,y=535,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=540,y=535,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=730,y=535,width=150,height=30)
        btn_cal_int=Button(self.root,text="Interest",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.calculate_interest).place(x=895,y=535,width=150,height=30)
        btn_cal_emi=Button(self.root,text="Cal EMI",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.calculate_emi).place(x=1050,y=535,width=150,height=30)


        #========customer details=================

        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=565,relwidth=1,height=130)
        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)
        self.CustomerTable=ttk.Treeview(cus_frame,columns=("AccountId","CustomerName","CustomerMobile","SuretyName","PrincipleAmount","Months","TotalAmount","IssueDate","LastDate","EMI","PayingAmount","BalanceAmount","TotalAmountPaid","Balance","TotalMonthsPaid","PaperCharges","ExtraPay","TotalExtra","OriginalAmount","PenalityAmount","TotalProfit","TotalLoss","Status","Proofs"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
        self.CustomerTable.heading("Months",text="Months")
        self.CustomerTable.heading("TotalAmount",text="TotalAmount")
        self.CustomerTable.heading("IssueDate",text="IssueDate")
        self.CustomerTable.heading("LastDate",text="Last Date")
        self.CustomerTable.heading("EMI",text="PayingAmount")
        self.CustomerTable.heading("PayingAmount",text="EMI")
        self.CustomerTable.heading("BalanceAmount",text="BalanceAmount")
        self.CustomerTable.heading("TotalAmountPaid",text="TotalAmountPaid")
        self.CustomerTable.heading("Balance",text="Balance")
        self.CustomerTable.heading("TotalMonthsPaid",text="TotalMonthsPaid")
        self.CustomerTable.heading("PaperCharges",text="PaperCharges")
        self.CustomerTable.heading("ExtraPay",text="ExtraPay")
        self.CustomerTable.heading("TotalExtra",text="TotalExtra")
        self.CustomerTable.heading("OriginalAmount",text="OriginalAmount")
        self.CustomerTable.heading("PenalityAmount",text="PenalityAmount")
        self.CustomerTable.heading("TotalProfit",text="TotalProfit")
        self.CustomerTable.heading("TotalLoss",text="TotalLoss")
        self.CustomerTable.heading("Status",text="Status")
        self.CustomerTable.heading("Proofs",text="Proofs")
        self.CustomerTable["show"]="headings"


        #================headings width setting==========
        self.CustomerTable.column("AccountId",width=70)
        self.CustomerTable.column("CustomerName",width=180)
        self.CustomerTable.column("CustomerMobile",width=80)
        self.CustomerTable.column("SuretyName",width=180)
        self.CustomerTable.column("PrincipleAmount",width=110)
        self.CustomerTable.column("Months",width=110)
        self.CustomerTable.column("TotalAmount",width=90)
        self.CustomerTable.column("IssueDate",width=100)
        self.CustomerTable.column("LastDate",width=100)
        self.CustomerTable.column("EMI",width=150)
        self.CustomerTable.column("PayingAmount",width=80)
        self.CustomerTable.column("BalanceAmount",width=100)
        self.CustomerTable.column("TotalAmountPaid",width=200)
        self.CustomerTable.column("Balance",width=200)
        self.CustomerTable.column("TotalMonthsPaid",width=200)
        self.CustomerTable.column("PaperCharges",width=200)
        self.CustomerTable.column("ExtraPay",width=200)
        self.CustomerTable.column("TotalExtra",width=200)
        self.CustomerTable.column("OriginalAmount",width=200)
        self.CustomerTable.column("PenalityAmount",width=200)
        self.CustomerTable.column("TotalProfit",width=200)
        self.CustomerTable.column("TotalLoss",width=200)
        self.CustomerTable.column("Status",width=200)
        self.CustomerTable.column("Proofs",width=200)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    """def saveUpdateDelete(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = saveUpdateDeleteClass(self.new_win)"""

    """def save(self):
        super().save() 

    def show(self):
        super().show() 

    def search(self):
        super().search() 
    
    def clear(self):
        super().clear() 
    
    def monthly_details(self):
        super().monthly_details() 

    def get_data(self,ev):
        super().get_data(ev) 

    def update(self):
        super().update() 

    def delete(self): 
        super().delete() 

    def calculate_interest(self):
        super().calculate_interest(self)"""
        
   

if __name__ == "__main__":
    root = Tk()
    #root.attributes('-fullscreen',True)
    obj = sample(root)
    root.mainloop()