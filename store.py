from tkinter import *
from PIL import Image,ImageTk 
from customer import Cust_Win
from products import Product_Win

class StoreManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Store Management System")
        self.root.geometry("1550x800+0+0")


        # First Image
        img1=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\store.jpg")
        img1=img1.resize((1550, 140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # Logo
        img2=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\logo.jpg")
        img2=img2.resize((230, 140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # Title
        lbl_title=Label(self.root, text="STORE MANAGEMENT SYSTEM", font=("times new roman", 40,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # Main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # Menu
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # Button frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)
        
        cust_btn=Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14,"bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        newOrder_btn=Button(btn_frame, text="NEW ORDER",width=22, font=("times new roman", 14,"bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        newOrder_btn.grid(row=1, column=0, pady=1)

        manageProducts_btn=Button(btn_frame, text="MANAGE PRODUCTS", command=self.product_details, width=22, font=("times new roman", 14,"bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        manageProducts_btn.grid(row=2, column=0, pady=1)

        report_btn=Button(btn_frame, text="REPORT",width=22, font=("times new roman", 14,"bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn=Button(btn_frame, text="LOGOUT",width=22, font=("times new roman", 14,"bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)



        # Right Side Image
        img3=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\store3.jpg")
        img3=img3.resize((1310, 590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)

        # Down Images
        img4=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\store4.jpeg")
        img4=img4.resize((230, 210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)

        img5=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\store2.jpeg")
        img5=img5.resize((230, 190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    
    def product_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Product_Win(self.new_window)



if __name__=='__main__':
    root=Tk()
    obj=StoreManagementSystem(root)
    root.mainloop()