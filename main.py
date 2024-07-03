from tkinter import *
from PIL import ImageTk,Image
from addPerson import addNewPerson
from individual import individualClass
from datetime import datetime


class FinancierApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Financier Management System")
        self.root.config(bg="white")
        
        #=============Title====================
        #self.icon_title=PhotoImage(file="images\logo.png")
        title = Label(self.root,text="Financier Management System",font=("times new roman",40,"bold"),bg='black',fg='white').place(x=0,y=0,relwidth=1,height=70)

        #=============btn_logout====================
        btn_logout = Button(self.root, text="LogOut", font=('time new roman', 15, "bold"),bg='yellow',cursor='hand2').place(x=1150,y=12,height=45,width=130)

        #=============Clock====================
        self.labl_clock = Label(self.root,font=("times new roman",15),bg='lightblue',fg='white')
        self.labl_clock.place(x=0,y=70,relwidth=1,height=30)



        #=============left_menu====================
        self.left_Menu_Logo=Image.open("images\MenuLogo.png")
        self.left_Menu_Logo = self.left_Menu_Logo.resize((200,200),Image.Resampling.LANCZOS)
        self.left_Menu_Logo = ImageTk.PhotoImage(self.left_Menu_Logo)
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="skyblue")
        LeftMenu.place(x=0,y=102,width=200,height=600)
        lbl_menulogo = Label(LeftMenu,image=self.left_Menu_Logo)
        lbl_menulogo.pack(side=TOP,fill=X)



        #=============Menu name on left side====================
        lbl_menu = Label(LeftMenu,text="Menu", font=('time new roman', 20),bg='lightgreen').pack(side=TOP,fill=X)


        #=============buttons on left side====================
        lbl_add_person = Button(LeftMenu,text="Add Person",command=self.addPerson,font=('time new roman', 15,"bold"),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        lbl_individual = Button(LeftMenu,text="Individual",command=self.individual,font=('time new roman', 15,"bold"),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        lbl_partner = Button(LeftMenu,text="Partner",font=('time new roman', 15,"bold"),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        lbl_unpaid = Button(LeftMenu,text="Unpaid",font=('time new roman', 15,"bold"),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        lbl_monthly = Button(LeftMenu,text="Monthly Report",font=('time new roman', 15,"bold"),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)

        #=============contents====================
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=300,y=120,height=150,width=300)
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=650,y=120,height=150,width=300)
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=1000,y=120,height=150,width=300)
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=300,y=280,height=150,width=300)
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=650,y=280,height=150,width=300)
        self.labl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.labl_employee.place(x=1000,y=280,height=150,width=300)

        #=============fotter====================
        lbl_footer = Label(self.root,text="FMS Financier Management System |  Developed by VIJAY & GEETHA \nFor any Technical Issue Contact : 1234567890",font=("times new roman",12),bg='#4d636d',fg='white').pack(side=BOTTOM,fill=X)

    def update_clock(self):
         #=============clock====================
        # Get the current date
        current_date = datetime.now()
        # Format the date as a string
        date_string = current_date.strftime("%d-%m-%Y")
        time_string = current_date.strftime("%H:%M:%S %p")
        self.labl_clock.config(text=f"Date : {date_string}  Time : {time_string}")
        self.labl_clock.after(1000, update_clock)

        

        


    #====================calling employee class with object ======================================
    def addPerson(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = addNewPerson(self.new_win)

    def individual(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = individualClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = FinancierApp(root)
    update_clock(self)
    root.mainloop()





