from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from store import StoreManagementSystem
# from register import register_window


class login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Store Management System")
        self.root.geometry("1550x800+0+0")

        # Image
        img1=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\login1.jpg")
        # img1=img1.resize((1550, 140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root, bg="white")
        frame.place(x=810, y=170, width=320, height=450)

        get_str=Label(frame, text="Login here!", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=50)

        #label
        username_lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username_lbl.place(x=100, y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)


        password_lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=100, y=225)

        self.txtpassword=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)


        #button
        loginbtn=Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black", bg="white", activeforeground="black", activebackground="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn=Button(frame, command=self.register_details, text="Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="white")
        registerbtn.place(x=10, y=350, width=160)

        forgetbtn=Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="white")
        forgetbtn.place(x=20, y=370, width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error", "All fields required")
        else:
            
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
                my_cursor = conn.cursor()
                query=("Select * from management.register where username=%s and password=%s")
                value=(self.txtuser.get(), self.txtpassword.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchall()
                details=list(row)
                
                # u_split=[i[1] for i in details]
                # p_split=[i[2] for i in details]
                # messagebox.showinfo("Info", f"{details}")
                if details[0]==None:
                    messagebox.showerror("Invalid", "Invalid Username and Password")
                else:
                    messagebox.showinfo("Success", "You've successfully Loged In!")
                    self.new_window=Toplevel(self.root)
                    self.app=StoreManagementSystem(self.new_window)
                conn.commit()
                conn.close()
                
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)
                

    def register_details(self):
        from register import register_window
        self.new_window=Toplevel(self.root)
        self.app=register_window(self.new_window)



if __name__=='__main__':
    root=Tk()
    obj=login_window(root)
    root.mainloop()