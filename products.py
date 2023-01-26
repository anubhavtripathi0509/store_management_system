from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Product_Win:
    def __init__(self, root):
        self.root=root
        self.root.title("Store Management System")
        self.root.geometry("1295x550+232+228")  #geometry(width,height,x-axis,y-axis)


        ########################## variables ###############################
        self.var_ref=StringVar()
        x=random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_product_name=StringVar()
        self.var_price=StringVar()
        self.var_uom=StringVar()


        # Title
        lbl_title=Label(self.root, text="MANAGE PRODUCTS", font=("times new roman", 18,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2=Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\logo.jpg")
        img2=img2.resize((100, 40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=4, width=100, height=40)

        # Label Frame
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, font=("arial", 12,"bold"), text="Product Details", padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)


        ################################################# Labels and Entries#########################################################
        #Product Reference
        lbl_product_ref=Label(labelframeleft,text="Product Ref", font=("arial", 12,"bold"), padx=2, pady=6)
        lbl_product_ref.grid(row=0, column=0, sticky=W)
        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_ref, width=22, font=("arial", 13,"bold"), state="readonly")
        entry_ref.grid(row=0,column=1)

        # Product Name
        pname=Label(labelframeleft,text="Name", font=("arial", 12,"bold"), padx=2, pady=6)
        pname.grid(row=1, column=0, sticky=W)
        txtpname=ttk.Entry(labelframeleft, textvariable=self.var_product_name, width=22, font=("arial", 13,"bold"))
        txtpname.grid(row=1,column=1)

        # UOM Combobox
        lbl_uom=Label(labelframeleft,text="UOM", font=("arial", 12,"bold"), padx=2, pady=6)
        lbl_uom.grid(row=3, column=0, sticky=W)
        combo_uom=ttk.Combobox(labelframeleft, textvariable=self.var_uom, font=("arial", 12,"bold"), width=27, state="readonly")
        combo_uom["value"]=("kg", "each")
        combo_uom.current(0)
        combo_uom.grid(row=3, column=1)

        # Product Price
        product_price=Label(labelframeleft,text="Price", font=("arial", 12,"bold"), padx=2, pady=6)
        product_price.grid(row=2, column=0, sticky=W)
        txtprice=ttk.Entry(labelframeleft, textvariable=self.var_price, width=22, font=("arial", 13,"bold"))
        txtprice.grid(row=2,column=1)


        ############################## Buttons ############################################
        btn_frame= Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnAdd.grid(row=0, column=0, padx=1, pady=2)

        btnUpdate=Button(btn_frame, text="Update", command=self.update, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnUpdate.grid(row=0, column=1, padx=1, pady=2)

        btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnDelete.grid(row=0, column=2, padx=1, pady=2)

        btnReset=Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnReset.grid(row=0, column=3, padx=1, pady=2)


        ############################### Tabel Frame search system ###########################################
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, font=("arial", 12,"bold"), text="View Details And Search System", padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy=Label(table_frame,text="Search By: ", font=("arial", 12,"bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12,"bold"), width=24, state="readonly")
        combo_search["value"]=("Name", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13,"bold"))
        txtSearch.grid(row=0,column=2, padx=2)


        # Button
        btnSearch=Button(table_frame, text="Search", command=self.search, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnSearch.grid(row=0, column=3, padx=1, pady=2)

        btnShowAll=Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 12,"bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnShowAll.grid(row=0, column=4, padx=1, pady=2)

        ##################################### Show Data Table ############################################
        details_table=LabelFrame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Product_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "uom", "price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Product_Details_Table.xview)
        scroll_y.config(command=self.Product_Details_Table.yview)
        self.Product_Details_Table.heading("ref", text="Refer No")
        self.Product_Details_Table.heading("name", text="Product Name")
        self.Product_Details_Table.heading("uom", text="UOM")
        self.Product_Details_Table.heading("price", text="Price")

        self.Product_Details_Table["show"]="headings"
        self.Product_Details_Table.column("ref", width=100)
        self.Product_Details_Table.pack(fill=BOTH, expand=1)
        self.Product_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    
    
    def add_data(self):
        if self.var_price.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into products values(%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_product_name.get(),
                    self.var_uom.get(),
                    self.var_price.get()                    
                ))
                conn.commit()
                self.fetch_data
                conn.close()

                messagebox.showinfo("Success", "product has been added", parent=self.root)
            
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)
    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from products")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Product_Details_Table.delete(*self.Product_Details_Table.get_children())
            for i in rows:
                self.Product_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row=self.Product_Details_Table.focus()
        content=self.Product_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_product_name.set(row[1]),
        self.var_uom.set(row[2]),
        self.var_price.set(row[3])
        
            

    def update(self):
        if self.var_price.get()=="":
            messagebox.showerror("Error", "Please enter price of product", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Update products set Name=%s,UOM=%s,Price=%s where Ref=%s", (
                    self.var_product_name.get(),
                    self.var_uom.get(),
                    self.var_price.get(),                    
                    self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Product details has been updated succesfully", parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Store Management System", "Do you want to delete this product", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
            my_cursor=conn.cursor()
            query="delete from products where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()



    def reset(self):
        # self.var_ref.set(""),
        self.var_product_name.set(""),
        self.var_price.set(""),
        # self.var_uom.set("")   
                
        x=random.randint(1000, 9999)   #After reset generating random reference number
        self.var_ref.set(str(x))



    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from products where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Product_Details_Table.delete(*self.Product_Details_Table.get_children())
            for i in rows:
                self.Product_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()




if __name__=='__main__':
    root=Tk()
    obj=Product_Win(root)
    root.mainloop()