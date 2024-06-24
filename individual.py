from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector
from mysql.connector import Error


class addNewPerson:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+30+10")
        self.root.title("Financier Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========================
        # All Variables

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cus_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_surety_name=StringVar()
        self.var_phone_no=StringVar()
        self.var_alter_no=StringVar()
        self.var_acc_type=StringVar()
        self.var_amount=StringVar()
        self.var_months=StringVar()
        self.var_issuedate=StringVar()
        self.var_lastdate=StringVar()
        self.var_proofs=StringVar()
        

        #========searchFrame=================

        SearchFrame=LabelFrame(self.root,text="View Person",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=350,y=20,width=600,height=70)

        #========options(drop down box)=================

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","ID","CustomerName","PhoneNumber"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=410,y=9,width=150,height=30)

        #========title=================

        title=Label(self.root,text="Person Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1200)

        #========contents=================

        #========column_1=================

        lbl_cusid=Label(self.root,text="Cus ID",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=150)
        lbl_cusname=Label(self.root,text="Customer Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=200)
        lbl_suretyname=Label(self.root,text="Surety Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=250)

        txt_cusid=Entry(self.root,textvariable=self.var_cus_id,font=("goudy old style",15,"bold"),bg="lightblue").place(x=200,y=150)
        txt_cusname=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightblue").place(x=200,y=200)
        txt_suretyname=Entry(self.root,textvariable=self.var_surety_name,font=("goudy old style",15,"bold"),bg="lightblue").place(x=200,y=250)


        #========column_2=================

        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=435,y=150)
        lbl_phoneno=Label(self.root,text="Phone no",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=435,y=200)
        lbl_atlerno=Label(self.root,text="Atlernate no",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=435,y=250)
        lbl_atlerno=Label(self.root,text="Issue Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=435,y=300)
        lbl_proofs=Label(self.root,text="Id Proofs",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=435,y=350)

        cmb_search=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("goudy old style",13))
        cmb_search.place(x=555,y=150)
        cmb_search.current(0)
        txt_phoneno=Entry(self.root,textvariable=self.var_phone_no,font=("goudy old style",15,"bold"),bg="lightblue").place(x=555,y=200)
        txt_alterno=Entry(self.root,textvariable=self.var_alter_no,font=("goudy old style",15,"bold"),bg="lightblue").place(x=555,y=250)
        txt_issuedate=Entry(self.root,textvariable=self.var_issuedate,font=("goudy old style",15,"bold"),bg="lightblue").place(x=555,y=300)
        txt_proofs=Entry(self.root,textvariable=self.var_proofs,font=("goudy old style",15,"bold"),bg="lightblue").place(x=555,y=350)
        
        #========column_3=================

        lbl_acctype=Label(self.root,text="Account Type",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=775,y=150)
        lbl_amount=Label(self.root,text="Amount",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=775,y=200)
        lbl_months=Label(self.root,text="Months",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=775,y=250)
        lbl_Lastdate=Label(self.root,text="Last Date",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=775,y=300)

        
        cmb_acctype=ttk.Combobox(self.root,textvariable=self.var_acc_type,values=("Select","Daily","Monthly","Yearly"),state="readonly",justify=CENTER,font=("goudy old style",13))
        cmb_acctype.place(x=925,y=150)
        cmb_acctype.current(0)
        txt_amount=Entry(self.root,textvariable=self.var_amount,font=("goudy old style",15,"bold"),bg="lightblue").place(x=925,y=200)
        txt_months=Entry(self.root,textvariable=self.var_months,font=("goudy old style",15,"bold"),bg="lightblue").place(x=925,y=250)
        txt_Lastdate=Entry(self.root,textvariable=self.var_lastdate,font=("goudy old style",15,"bold"),bg="lightblue").place(x=925,y=300)


        #========address field=================

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=50,y=300)
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightblue")
        self.txt_address.place(x=200,y=310,width=200,height=100)
        
        #========buttons of update on database=================

        btn_save=Button(self.root,text="Save",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2",command=self.save).place(x=150,y=430,width=150,height=30)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="green",fg="white",cursor="hand2",command=self.update).place(x=320,y=430,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=490,y=430,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=660,y=430,width=150,height=30)


        #========customer details=================

        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=480,relwidth=1,height=205)
        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)
        self.CustomerTable=ttk.Treeview(cus_frame,columns=("ID","CustomerName","Gender","SuretyName","PhoneNumber","AlternateNumber","AccountType","Amount","Months","IssueDate","LastDate","Proofs","Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)


        #================headings to show on screen==========
        self.CustomerTable.heading("ID",text="ID")
        self.CustomerTable.heading("CustomerName",text="Customer Name")
        self.CustomerTable.heading("Gender",text="Gender")
        self.CustomerTable.heading("SuretyName",text="Surety Name")
        self.CustomerTable.heading("PhoneNumber",text="Phone Number")
        self.CustomerTable.heading("AlternateNumber",text="Alternate Number")
        self.CustomerTable.heading("AccountType",text="Account Type")
        self.CustomerTable.heading("Amount",text="Amount")
        self.CustomerTable.heading("Months",text="Months")
        self.CustomerTable.heading("IssueDate",text="Issue Date")
        self.CustomerTable.heading("LastDate",text="Last Date")
        self.CustomerTable.heading("Proofs",text="Proofs")
        self.CustomerTable.heading("Address",text="Address")
        self.CustomerTable["show"]="headings"
        


        #================headings width setting==========
        self.CustomerTable.column("ID",width=70)
        self.CustomerTable.column("CustomerName",width=180)
        self.CustomerTable.column("Gender",width=80)
        self.CustomerTable.column("SuretyName",width=180)
        self.CustomerTable.column("PhoneNumber",width=110)
        self.CustomerTable.column("AlternateNumber",width=110)
        self.CustomerTable.column("AccountType",width=90)
        self.CustomerTable.column("Amount",width=150)
        self.CustomerTable.column("Months",width=80)
        self.CustomerTable.column("IssueDate",width=100)
        self.CustomerTable.column("LastDate",width=100)
        self.CustomerTable.column("Proofs",width=100)
        self.CustomerTable.column("Address",width=200)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()


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
                    if self.var_cus_id.get()=="":
                        messagebox.showerror("Error",f"Customer Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Customers where ID=%s",(self.var_cus_id.get(),))
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","This Customer Id already assigned, try a different one",parent=self.root)
                        else:
                            cursor.execute("Insert into Customers (ID,CustomerName,Gender,SuretyName,PhoneNumber,AlternateNumber,AccountType,Amount,Months,IssueDate,LastDate,Proofs,Address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                            self.var_cus_id.get(),
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_surety_name.get(),
                                            self.var_phone_no.get(),
                                            self.var_alter_no.get(),
                                            self.var_acc_type.get(),
                                            self.var_amount.get(),
                                            self.var_months.get(),
                                            self.var_issuedate.get(),
                                            self.var_lastdate.get(),
                                            self.var_proofs.get(),
                                            self.txt_address.get('1.0',END)

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
                    cursor.execute("select * from Customers")
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
        self.var_cus_id.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_surety_name.set(row[3])
        self.var_phone_no.set(row[4])
        self.var_alter_no.set(row[5])
        self.var_acc_type.set(row[6])
        self.var_amount.set(row[7])
        self.var_months.set(row[8])
        self.var_issuedate.set(row[9])
        self.var_lastdate.set(row[10])
        self.var_proofs.set(row[11])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[12])



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
                    if self.var_cus_id.get()=="":
                        messagebox.showerror("Error",f"Customer Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Customers where ID=%s",(self.var_cus_id.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            cursor.execute('update Customers set CustomerName=%s,Gender=%s,SuretyName=%s,PhoneNumber=%s,AlternateNumber=%s,AccountType=%s,Amount=%s,Months=%s,IssueDate=%s,LastDate=%s,Proofs=%s,Address=%s where ID=%s',(
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_surety_name.get(),
                                            self.var_phone_no.get(),
                                            self.var_alter_no.get(),
                                            self.var_acc_type.get(),
                                            self.var_amount.get(),
                                            self.var_months.get(),
                                            self.var_issuedate.get(),
                                            self.var_lastdate.get(),
                                            self.var_proofs.get(),
                                            self.txt_address.get('1.0',END),
                                            self.var_cus_id.get()

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
                    if self.var_cus_id.get()=="":
                        messagebox.showerror("Error",f"Customer Id should be required",parent=self.root)
                    else:
                        cursor.execute("select * from Customers where ID=%s",(self.var_cus_id.get(),))
                        row=cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Customer Id Please try correct one",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to Delter the Customer",parent=self.root)
                            if op==True:
                                cursor.execute("delete from Customers where ID=%s",(self.var_cus_id.get(),))
                                con.commit()
                                messagebox.showinfo("Delete","Customer Details Deleted Successfully",parent=self.root)
                                self.clear()

                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    #================creating show function==========
    def clear(self):
        self.var_cus_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_surety_name.set("")
        self.var_phone_no.set("")
        self.var_alter_no.set("")
        self.var_acc_type.set("Select")
        self.var_amount.set("")
        self.var_months.set("")
        self.var_issuedate.set("")
        self.var_lastdate.set("")
        self.var_proofs.set("")
        self.txt_address.delete('1.0',END)
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
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
                        cursor.execute("select * from Customers where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
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


if __name__ == "__main__":
    root = Tk()
    obj = addNewPerson(root)
    root.mainloop()