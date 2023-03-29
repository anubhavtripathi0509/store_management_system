from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime as dt
from docxtpl import DocxTemplate


class Order_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Management System")
        # geometry(width,height,x-axis,y-axis)
        self.root.geometry("1295x550+232+228")

        ########################## variables ###############################
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cname = StringVar()
        self.var_product_name = StringVar()
        self.var_price = DoubleVar()
        self.var_uom = StringVar()
        self.var_quan = DoubleVar()

        self.var_total = DoubleVar()
        # self.var_total.set(round(float(self.var_price.get())*float(self.var_quan.get()),2))

        self.var_overalltotal = StringVar()
        self.var_date = StringVar()
        y = dt.datetime.now()
        self.var_date.set(str(y))

        # Title
        lbl_title = Label(self.root, text="ORDER DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"C:\Users\Anubhav Trithahi\Desktop\management system\images\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=4, width=100, height=40)

        # Label Frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, font=(
            "arial", 12, "bold"), text="Order Details", padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        ################################################# Labels and Entries#########################################################
        # Order Reference
        lbl_order_ref = Label(labelframeleft, text="Order Ref", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_order_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # Fetch data button
        btnFetchData = Button(labelframeleft, text="Fetch Data", command=self.fetch_data_down, font=(
            "arial", 8, "bold"), bg="black", fg="gold", width=7, cursor="hand2")
        btnFetchData.place(x=350, y=4)

        # Date
        date = Label(labelframeleft, text="Date", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        date.grid(row=1, column=0, sticky=W)
        txtdate = ttk.Entry(
            labelframeleft, textvariable=self.var_date, width=22, font=("arial", 13, "bold"), state="readonly")
        txtdate.grid(row=1, column=1)

        # Customer Name
        cname = Label(labelframeleft, text="Customer Name",font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=2, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cname, width=22, font=("arial", 13, "bold"))
        txtcname.grid(row=2, column=1)

        # Product Name
        pname = Label(labelframeleft, text="Product Name",
                      font=("arial", 12, "bold"), padx=2, pady=6)
        pname.grid(row=3, column=0, sticky=W)
        txtpname = ttk.Entry(labelframeleft, textvariable=self.var_product_name, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        txtpname.grid(row=3, column=1)

        # Product Price
        product_price = Label(labelframeleft, text="Product Per Price", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        product_price.grid(row=4, column=0, sticky=W)
        txtprice = ttk.Entry(labelframeleft, textvariable=self.var_price, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        txtprice.grid(row=4, column=1)

        # UOM Combobox
        lbl_uom = Label(labelframeleft, text="UOM", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_uom.grid(row=5, column=0, sticky=W)
        combo_uom = ttk.Combobox(labelframeleft, textvariable=self.var_uom, font=(
            "arial", 12, "bold"), width=20, state="readonly")
        combo_uom["value"] = ("kg", "each")
        combo_uom.current(0)
        combo_uom.grid(row=5, column=1)

        # Quantity
        quantity = Label(labelframeleft, text="Quantity",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        quantity.grid(row=6, column=0, sticky=W)
        txtquantity = ttk.Entry(
            labelframeleft, textvariable=self.var_quan, width=22, font=("arial", 13, "bold"))
        txtquantity.grid(row=6, column=1)

        # Total
        total = Label(labelframeleft, text="Total", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        total.grid(row=7, column=0, sticky=W)
        txttotal = ttk.Entry(labelframeleft, textvariable=self.var_total, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        txttotal.grid(row=7, column=1)

        # Finall Total
        overalltotal = Label(labelframeleft, text="Bill Total", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        overalltotal.grid(row=8, column=0, sticky=W)
        txtoveralltotal = ttk.Entry(labelframeleft, textvariable=self.var_overalltotal, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        txtoveralltotal.grid(row=8, column=1)

        # Bill Button
        btnBill = Button(labelframeleft, command=self.generate_invoice, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnBill.grid(row=9, column=0, padx=1, pady=2, sticky=W)

        # Total Button
        btnTotal = Button(labelframeleft, text="Total", command=self.total, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnTotal.grid(row=9, column=1, padx=1, pady=2, sticky=W)

        ############################## Buttons ############################################
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnAdd.grid(row=0, column=0, padx=1, pady=2)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnUpdate.grid(row=0, column=1, padx=1, pady=2)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnDelete.grid(row=0, column=2, padx=1, pady=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnReset.grid(row=0, column=3, padx=1, pady=2)

        ############################### Tabel Frame search system Up ###########################################
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, font=(
            "arial", 12, "bold"), text="View Details And Search System", padx=2)
        table_frame.place(x=435, y=50, width=860, height=230)

        lblSearchBy = Label(table_frame, text="Search By: ", font=(
            "arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Customer_Name", "Ref", "Date")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(
            table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        # Button
        btnSearch = Button(table_frame, text="Search", command=self.search_up, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnSearch.grid(row=0, column=3, padx=1, pady=2)

        btnShowAll = Button(table_frame, text="Show All", command=self.fetch_data_up, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnShowAll.grid(row=0, column=4, padx=1, pady=2)

        ##################################### Show Data Table Up ############################################
        details_table = LabelFrame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=150)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Product_Details_Table = ttk.Treeview(details_table, column=("Ref", "Date", "Customer_Name", "product_name", "price_per_unit", "uom", "quantity", "Total"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Product_Details_Table.xview)
        scroll_y.config(command=self.Product_Details_Table.yview)
        self.Product_Details_Table.heading("Ref", text="Refer No")
        self.Product_Details_Table.heading("Date", text="Date")
        self.Product_Details_Table.heading("Customer_Name", text="Customer Name")
        self.Product_Details_Table.heading("product_name", text="Product Name")
        self.Product_Details_Table.heading("price_per_unit", text="Price Per Unit")
        self.Product_Details_Table.heading("uom", text="UOM")
        self.Product_Details_Table.heading("quantity", text="Quantity")
        self.Product_Details_Table.heading("Total", text="Total")

        self.Product_Details_Table["show"] = "headings"
        self.Product_Details_Table.column("Ref", width=100)
        self.Product_Details_Table.column("Date", width=100)
        self.Product_Details_Table.column("Customer_Name", width=100)
        self.Product_Details_Table.column("product_name", width=100)
        self.Product_Details_Table.column("price_per_unit", width=100)
        self.Product_Details_Table.column("uom", width=100)
        self.Product_Details_Table.column("quantity", width=100)
        self.Product_Details_Table.column("Total", width=100)
        self.Product_Details_Table.pack(fill=BOTH, expand=1)
        self.Product_Details_Table.bind("<ButtonRelease-1>", self.get_cursor_up)
        self.fetch_data_up()

        ############################### Tabel Frame search system Down ###########################################
        table_frame_down = LabelFrame(self.root, bd=2, relief=RIDGE, font=(
            "arial", 12, "bold"), text="View Details And Search System", padx=2)
        table_frame_down.place(x=435, y=280, width=860, height=260)

        lblSearchBy_down = Label(table_frame_down, text="Search By: ", font=(
            "arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy_down.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var_down = StringVar()
        combo_search_down = ttk.Combobox(table_frame_down, textvariable=self.search_var_down, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_search_down["value"] = ("Name", "Ref")
        combo_search_down.current(0)
        combo_search_down.grid(row=0, column=1)

        self.txt_search_down = StringVar()
        txtSearch_down = ttk.Entry(
            table_frame_down, textvariable=self.txt_search_down, width=24, font=("arial", 13, "bold"))
        txtSearch_down.grid(row=0, column=2, padx=2)

        # Button
        btnSearch_down = Button(table_frame_down, text="Search", command=self.search_down, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnSearch_down.grid(row=0, column=3, padx=1, pady=2)

        btnShowAll_down = Button(table_frame_down, text="Show All", command=self.fetch_data_down, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnShowAll_down.grid(row=0, column=4, padx=1, pady=2)

        ##################################### Show Data Table DOWN ############################################
        details_table_down = LabelFrame(table_frame_down, bd=2, relief=RIDGE)
        details_table_down.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table_down, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table_down, orient=VERTICAL)

        self.Product_Details_Table_Down = ttk.Treeview(details_table_down, column=("ref", "name", "uom", "price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Product_Details_Table_Down.xview)
        scroll_y.config(command=self.Product_Details_Table_Down.yview)
        self.Product_Details_Table_Down.heading("ref", text="Refer No")
        self.Product_Details_Table_Down.heading("name", text="Product Name")
        self.Product_Details_Table_Down.heading("uom", text="UOM")
        self.Product_Details_Table_Down.heading("price", text="Price")

        self.Product_Details_Table_Down["show"] = "headings"
        self.Product_Details_Table_Down.column("ref", width=100)
        self.Product_Details_Table_Down.pack(fill=BOTH, expand=1)
        self.Product_Details_Table_Down.bind("<ButtonRelease-1>", self.get_cursor_down)
        self.fetch_data_down()

    # def fetch_data(self):
    #     if self.var_product_name.get()=="":
    #         messagebox.showerror("Error", "Please enter Product Name", parent=self.root)
    #     else:
    #         conn=mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
    #         my_cursor=conn.cursor()
    #         query=("Select * from products where Name=%s")
    #         value=(self.var_product_name.get(),)
    #         my_cursor.execute(query, value)
    #         row=my_cursor.fetchone()

    #         if row==None:
    #             messagebox.showerror("Error", "This product not found", parent=self.root)
    #         else:
    #             conn.commit()
    #             conn.close()

    #             showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
    #             showDataframe.place(x=455, y=55, width=300, height=180)

    #             lblName=Label(showDataframe, text="Name: ", font=("arial", 12, "bold"))
    #             lblName.place(x=0, y=0)

    def add_data(self):
        if self.var_quan.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into management.order (`Ref`, `Date`, `Customer_Name`, `product_name`, `price_per_unit`, `uom`, `quantity`, `Total`) values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_date.get(),
                    self.var_cname.get(),
                    self.var_product_name.get(),
                    self.var_price.get(),
                    self.var_uom.get(),
                    self.var_quan.get(),
                    self.var_total.get()
                ))
                conn.commit()
                self.fetch_data_up
                conn.close()

                messagebox.showinfo("Success", "order has been added", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)

    def update(self):
        try:
            if self.var_quan.get() == "":
                messagebox.showerror("Error", "Please enter quantity of order", parent=self.root)
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("Update management.order set Date=%s,Customer_Name=%s,product_name=%s,price_per_unit=%s,uom=%s,quantity=%s,total=%s where Ref=%s", (
                    self.var_date.get(),
                    self.var_cname.get(),
                    self.var_product_name.get(),
                    self.var_price.get(),
                    self.var_uom.get(),
                    self.var_quan.get(),
                    self.var_total.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data_up()
                conn.close()
                messagebox.showinfo(
                    "Update", "Order details has been updated succesfully", parent=self.root)
        except Exception as es:
            messagebox.showwarning(
                "Warning", f"Some thing went wrong: {str(es)}", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Store Management System", "Do you want to delete this order", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
            my_cursor = conn.cursor()
            query = "delete from management.order where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data_up()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        # self.var_date.set(""),
        self.var_cname.set(""),
        self.var_product_name.set(""),
        self.var_price.set(""),
        # self.var_uom.set(""),
        self.var_quan.set(""),
        self.var_total.set(""),
        self.var_overalltotal.set("")
        # After reset generating random reference number
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        # After reset generating date
        y = dt.datetime.now()
        self.var_date.set(str(y))

    def fetch_data_up(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM management.order;")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Product_Details_Table.delete(
                *self.Product_Details_Table.get_children())
            for i in rows:
                self.Product_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def fetch_data_down(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from products")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Product_Details_Table_Down.delete(
                *self.Product_Details_Table_Down.get_children())
            for i in rows:
                self.Product_Details_Table_Down.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor_up(self, event=""):
        cursor_row = self.Product_Details_Table.focus()
        content = self.Product_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_date.set(row[1])
        self.var_cname.set(row[2]),
        self.var_product_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_uom.set(row[5]),
        self.var_quan.set(row[6]),
        self.var_total.set(row[7])


    def get_cursor_down(self, event=""):
        cursor_row = self.Product_Details_Table_Down.focus()
        content = self.Product_Details_Table_Down.item(cursor_row)
        row = content["values"]

        # self.var_ref.set(row[0]),
        self.var_product_name.set(row[1]),
        self.var_uom.set(row[2]),
        self.var_price.set(row[3])

    def search_up(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from management.order where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Product_Details_Table.delete(
                *self.Product_Details_Table.get_children())
            for i in rows:
                self.Product_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def search_down(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from products where " + str(self.search_var_down.get()) + " LIKE '%" + str(self.txt_search_down.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Product_Details_Table_Down.delete(
                *self.Product_Details_Table_Down.get_children())
            for i in rows:
                self.Product_Details_Table_Down.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        self.var_total.set(round(float(self.var_price.get(),)* float(self.var_quan.get()), 2))
        self.var_overalltotal.set(round(float()))

        conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
        my_cursor = conn.cursor()
        query = ("SELECT sum(Total) from management.order where Customer_Name=%s")
        value = (self.var_cname.get(), )
        my_cursor.execute(query, value)
        row = my_cursor.fetchall()
        otvalue = list(row)
        if otvalue[0] is None:
            messagebox.showerror("Error", "Bill is empty", parent=self.root)
        else:
            self.var_overalltotal.set(row[0])
            conn.commit()
        conn.close()


    
    
    # ######################################## Bill Section #########################################################
    

    def generate_invoice(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="AnubhaV&0509", database="management")
            my_cursor = conn.cursor()
            query=("select quantity,product_name,price_per_unit,total from management.order where Customer_Name=%s")
            value = (self.var_cname.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchall()
            invoice_list = list(row)

            doc = DocxTemplate("invoice_template.docx")
            name = self.var_cname.get()
            subtotal = self.var_overalltotal.get()
            salestax = 0.0
            total = subtotal
            # messagebox.showinfo("Info",f"{subtotal}", parent=self.root)
    
            doc.render({"name":name, 
                "invoice_list": invoice_list,
                "subtotal":subtotal,
                "salestax":str(salestax*100)+"%",
                "total":total})
    
            doc_name = "new_invoice" + name + dt.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
            doc.save(doc_name)
    
            messagebox.showinfo("Invoice Complete", "Invoice Complete", parent=self.root)

        except Exception as es:
            messagebox.showwarning(
                "Warning", f"Some thing went wrong: {str(es)}", parent=self.root)
    
        



if __name__ == '__main__':
    root = Tk()
    obj = Order_Win(root)
    root.mainloop()
