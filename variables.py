from tkinter import *

class Variables():
    def __init__(self, root):

        #=========================
        # All Variables

        self.var_searchby=StringVar(root)
        self.var_searchtxt=StringVar(root)

        self.var_AccountId=StringVar(root)
        self.var_CustomerName=StringVar(root)
        self.var_CustomerMobile=StringVar(root)
        self.var_SuretyName=StringVar(root)
        self.var_PrincipleAmount=StringVar(root)
        self.var_Months=StringVar(root)
        self.var_TotalAmount=StringVar(root)
        self.var_IssueDate=StringVar(root)
        self.var_LastDate=StringVar(root)
        self.var_EMI=StringVar(root)
        self.var_PayingAmount=StringVar(root)
        self.var_BalanceAmount=StringVar(root)
        self.var_TotalAmountPaid=StringVar(root)
        self.var_Balance=StringVar(root)
        self.var_TotalMonthsPaid=StringVar(root)
        self.var_PaperCharges=StringVar(root)
        self.var_ExtraPay=StringVar(root)
        self.var_TotalExtra=StringVar(root)
        self.var_OriginalAmount=StringVar(root)
        self.var_PenalityAmount=StringVar(root)
        self.var_TotalProfit=StringVar(root)
        self.var_TotalLoss=StringVar(root)
        self.var_Status=StringVar(root)
        self.var_Proofs=StringVar(root)
        self.var_Interest=StringVar(root)

        #========customer details=================

        """cus_frame=Frame(self.root,bd=3,relief=RIDGE)
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

        self.show()"""
        
   

