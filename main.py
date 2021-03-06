from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
from functools import partial

import functions

class ConnectorDB():

    def change_win(cls,window, color):
        root = Tk()
        application = ConnectorDB(root, window, color)
        if window=='Customers':
            root.geometry("990x667")
        elif window=='Brands':
            root.geometry("990x590")
        elif window=='Categories':
            root.geometry("1013x590")
        elif window=='Subcategories':
            root.geometry("1040x590")
        elif window=='Orders':
            root.geometry("999x633")
        elif window=='Products':
            root.geometry("1028x633")
        elif window=='OrderItems':
            root.geometry("1009x590")
        root.mainloop()

    def __init__(self,root, window, color):

        self.root = root
        self.window = window
        self.color = color
        titlespace = ""
        self.root.title("Electronic Store Database")
        self.root.geometry("990x667")
        self.root.resizable(width=False, height=False)
        MainFrame = Frame(self.root, bd=10, width=1300, height=700, relief=RIDGE, bg=self.color)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1300, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=1300, height=400, padx=2, bg=self.color, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        # Buttons tabels
        LeftFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg=self.color, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        # Data window
        MidFrame = Frame(TopFrame3, bd=5, width=1300, height=400, padx=2, bg=self.color, relief=RIDGE)
        MidFrame.pack(side=LEFT)
        MidFrame1 = Frame(MidFrame, bd=5, width=1300, height=180, padx=12, pady=9, relief=RIDGE)
        MidFrame1.pack(side=TOP)

        # Operation buttons
        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg=self.color, relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        #=================================================================================================
        CustomerID=StringVar()
        FirstName=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Gender=StringVar()
        Mobile=StringVar()

        BrandID=StringVar()
        BrandName=StringVar()

        CategoryID=StringVar()
        CategoryName=StringVar()

        SubcategoryID=StringVar()
        SubcategoryName=StringVar()
        Category=StringVar()

        OrderID=StringVar()
        Customer=StringVar()
        OrderStatus=StringVar()
        OrderDate=StringVar()
        ShippedDate=StringVar()

        ProductID=StringVar()
        ProductName=StringVar()
        ListPrice = StringVar()
        ProductBrand=StringVar()
        ProductCategory=StringVar()

        OrderItemID = StringVar()
        ProductItemID = StringVar()
        Quantity = StringVar()

        #=================================================================================================
        def seq(window, color):
            root.destroy()
            self.change_win(window, color)

        def Reset():
            if self.window=='Customers':
                self.entCustomerID.delete(0, END)
                self.entFirstName.delete(0, END)
                self.entSurname.delete(0, END)
                self.entAddress.delete(0, END)
                Gender.set("")
                self.entMobile.delete(0, END)
            elif self.window=='Brands':
                self.entBrandID.delete(0, END)
                self.entBrandName.delete(0, END)
            elif self.window=='Categories':
                self.entCategoryID.delete(0, END)
                self.entCategoryName.delete(0, END)
            elif self.window=='Subcategories':
                self.entSubcategoryID.delete(0, END)
                self.entSubcategoryName.delete(0, END)
                Category.set("")
            elif self.window=='Orders':
                self.entOrderID.delete(0, END)
                entCustomer.set("")
                entOrderStatus.set("")
                self.entOrderDate.delete(0, END)
                self.entShippedDate.delete(0, END)
            elif self.window=='Products':
                self.entProductID.delete(0, END)
                self.entProductName.delete(0, END)
                self.entListPrice.delete(0, END)
                ProductBrand.set("")
                ProductCategory.set("")
            elif self.window == 'OrderItems':
                ProductBrand.set("")
                ProductCategory.set("")
                self.entQuantity.delete(0, END)

        def addData():
            if self.window == 'Customers':
                if CustomerID.get() =="" or FirstName.get()=="" or Surname.get()=="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute("insert into Customers values(%s,%s,%s,%s,%s,%s)",(

                    CustomerID.get(),
                    FirstName.get(),
                    Surname.get(),
                    Address.get(),
                    Gender.get(),
                    Mobile.get(),
                    ))
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == 'Brands':
                if BrandID.get() =="" or BrandName.get()=="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute("insert into Brands values(%s,%s)", (

                        BrandID.get(),
                        BrandName.get(),
                    ))
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == 'Categories':
                if CategoryID.get() =="" or CategoryName.get()=="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute("insert into Categories values(%s,%s)", (

                        CategoryID.get(),
                        CategoryName.get(),
                    ))
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == 'Subcategories':
                if SubcategoryID.get() =="" or SubcategoryName.get()=="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute("insert into Subcategories(SubcategoryID, SubcategoryName, CategoryID) select %s, %s, CategoryID from Categories where CategoryName=%s limit 1", (
                        SubcategoryID.get(),
                        SubcategoryName.get(),
                        Category.get(),
                    ))
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == "Orders":
                if OrderID.get() =="" or OrderStatus.get() =="" or OrderDate.get() =="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                cur.execute(
                    "insert into Orders(OrderID, OrderStatus, OrderDate, ShippedDate, CustomerID) select %s, %s, %s, %s, CustomerID from Customers where Surname=%s limit 1",
                    (
                        OrderID.get(),
                        OrderStatus.get(),
                        OrderDate.get(),
                        ShippedDate.get(),
                        Customer.get(),
                    ))
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == "Products":
                if ProductID.get() =="" or ProductName.get() =="" or ListPrice.get() =="":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute(
                        "INSERT INTO Products(ProductID, ProductName, ListPrice, BrandID, CategoryID) VALUES (%s,%s,%s, (SELECT BrandID FROM Brands WHERE BrandName = %s LIMIT 1) , (SELECT CategoryID FROM Categories WHERE CategoryName = %s LIMIT 1))",
                        (
                            ProductID.get(),
                            ProductName.get(),
                            ListPrice.get(),
                            ProductBrand.get(),
                            ProductCategory.get(),
                    )
                    )
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

            elif self.window == 'OrderItems':
                if Quantity.get() == "":
                    tkinter.messagebox.showerror("MySQL Conntector", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                             database='electronic_store')
                    cur = sqlCon.cursor()
                    cur.execute(
                        "INSERT INTO OrderItems(OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
                        (
                            OrderItemID.get(),
                            ProductItemID.get(),
                            Quantity.get(),
                        )
                    )
                    sqlCon.commit()
                    functions.DisplayData(window, self.data_records)
                    sqlCon.close()
                    tkinter.messagebox.showinfo("MySQL Connector", "Record Entered Successfully")

        def Delete():
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                     database='electronic_store')
            cur = sqlCon.cursor()
            if self.window == 'Customers':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Customers where CustomerID=%s",CustomerID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'Brands':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Brands where BrandID=%s",BrandID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'Categories':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Categories where CategoryID=%s",CategoryID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'Subcategories':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Subcategories where SubcategoryID=%s",SubcategoryID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'Orders':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Orders where OrderID=%s", OrderID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'Products':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from Products where ProductID=%s", ProductID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

            elif self.window == 'OrderItems':
                sqlCon = pymysql.connect(host="localhost", user="root", password="rooter",
                                         database='electronic_store')
                cur = sqlCon.cursor()
                cur.execute("delete from OrderItems where OrderItemID=%s", OrderItemID.get())
                sqlCon.commit()
                functions.DisplayData(window, self.data_records)
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connector", "Record Delete Successfully")

        def Info(ev):
            viewInfo = self.data_records.focus()
            learnerData = self.data_records.item(viewInfo)
            row = learnerData['values']
            if self.window == 'Customers':
                CustomerID.set(row[0]),
                FirstName.set(row[1]),
                Surname.set(row[2]),
                Address.set(row[3]),
                Gender.set(row[4]),
                Mobile.set(row[5]),

            elif self.window == 'Brands':
                BrandID.set(row[0]),
                BrandName.set(row[1]),

            elif self.window == 'Categories':
                CategoryID.set(row[0]),
                CategoryName.set(row[1]),

            elif self.window == 'Subcategories':
                SubcategoryID.set(row[0]),
                SubcategoryName.set(row[1]),
                CategoryID.set(row[2]),

            elif self.window == 'Orders':
                OrderID.set(row[0]),
                CustomerID.set(row[1]),
                OrderStatus.set(row[2]),
                OrderDate.set(row[3]),
                ShippedDate.set(row[4]),

            elif self.window == 'Products':
                ProductID.set(row[0]),
                ProductName.set(row[1]),
                ListPrice.set(row[2]),
                ProductBrand.set(row[3]),
                ProductCategory.set(row[4]),

            elif self.window == 'OrderItems':
                OrderItemID.set(row[0]),
                ProductItemID.set(row[1]),
                Quantity.set(row[2]),

        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            if self.window == 'Customers':
                cur.execute("update Customers set FirstName=%s, Surname=%s, Address=%s, Gender=%s, Mobile=%s where CustomerID=%s",(

                    FirstName.get(),
                    Surname.get(),
                    Address.get(),
                    Gender.get(),
                    Mobile.get(),
                    CustomerID.get()
                ))
            elif self.window == 'Brands':
                cur.execute("update Brands set BrandName=%s where BrandID=%s",
                    (
                        BrandName.get(),
                        BrandID.get()
                    ))
            elif self.window == 'Categories':
                cur.execute(
                    "update Categories set CategoryName=%s where CategoryID=%s",
                    (
                        CategoryName.get(),
                        CategoryID.get()
                    ))
            elif self.window == 'Subcategories':
                cur.execute(
                    "insert into Subcategories(SubcategoryID, SubcategoryName, CategoryID) select %s, %s, CategoryID from Categories where CategoryName=%s limit 1",
                    (
                        SubcategoryID.get(),
                        SubcategoryName.get(),
                        Category.get(),
                    ))
            elif self.window == 'Orders':
                cur.execute(
                    "insert into Orders(OrderID, OrderStatus, OrderDate, ShippedDate, CustomerID) select %s, %s, %s, %s, CustomerID from Customers where Surname=%s limit 1",
                    (
                        OrderID.get(),
                        OrderStatus.get(),
                        OrderDate.get(),
                        ShippedDate.get(),
                        Customer.get(),
                    ))

            elif self.window == 'Products':
                cur.execute(
                    "INSERT INTO Products(ProductID, ProductName, ListPrice, BrandID, CategoryID) VALUES (%s,%s,%s, (SELECT BrandID FROM Brands WHERE BrandName = %s LIMIT 1) , (SELECT CategoryID FROM Categories WHERE CategoryName = %s LIMIT 1))",
                    (
                        ProductID.get(),
                        ProductName.get(),
                        ListPrice.get(),
                        ProductBrand.get(),
                        ProductCategory.get(),
                    )
                )

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connector", "Record Updated Successfully")
            functions.DisplayData(window, self.data_records)

        #=================================================================================================
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text="MySQL Electronic Store", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=50)

        if self.window == 'Customers':
            self.lblCustomerID = Label(MidFrame1, font=('arial', 12, 'bold'), text="CustomerID", bd=7)
            self.lblCustomerID.grid(row=1, column=0, sticky=W, padx=5)
            self.entCustomerID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=CustomerID)
            self.entCustomerID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblFirstName = Label(MidFrame1, font=('arial', 12, 'bold'), text="FirstName", bd=7)
            self.lblFirstName.grid(row=2, column=0, sticky=W, padx=5)
            self.entFirstName = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=FirstName)
            self.entFirstName.grid(row=2, column=1, sticky=W, padx=5)

            self.lblSurname = Label(MidFrame1, font=('arial', 12, 'bold'), text="Surname", bd=7)
            self.lblSurname.grid(row=3, column=0, sticky=W, padx=5)
            self.entSurname = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Surname)
            self.entSurname.grid(row=3, column=1, sticky=W, padx=5)

            self.lblAddress = Label(MidFrame1, font=('arial', 12, 'bold'), text="Address", bd=7)
            self.lblAddress.grid(row=4, column=0, sticky=W, padx=5)
            self.entAddress = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Address)
            self.entAddress.grid(row=4, column=1, sticky=W, padx=5)

            self.lblGender = Label(MidFrame1, font=('arial', 12, 'bold'), text="Gender", bd=5)
            self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
            self.cboGender = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly', textvariable=Gender)
            self.cboGender['values']= (' ', 'Female', 'Male')
            self.cboGender.current(0)
            self.cboGender.grid(row=5, column=1)

            self.lblMobile = Label(MidFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=7)
            self.lblMobile.grid(row=6, column=0, sticky=W, padx=5)
            self.entMobile = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Mobile)
            self.entMobile.grid(row=6, column=1, sticky=W, padx=5)

        elif self.window=='Brands':
            self.lblBrandID = Label(MidFrame1, font=('arial', 12, 'bold'), text="BrandID", bd=7)
            self.lblBrandID.grid(row=1, column=0, sticky=W, padx=5)
            self.entBrandID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                       textvariable=BrandID)
            self.entBrandID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblBrandName = Label(MidFrame1, font=('arial', 12, 'bold'), text="BrandName", bd=7)
            self.lblBrandName.grid(row=2, column=0, sticky=W, padx=5)
            self.entBrandName = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=BrandName)
            self.entBrandName.grid(row=2, column=1, sticky=W, padx=5)

        elif self.window=='Categories':
            self.lblCategoryID = Label(MidFrame1, font=('arial', 12, 'bold'), text="CategoryID", bd=7)
            self.lblCategoryID.grid(row=1, column=0, sticky=W, padx=5)
            self.entCategoryID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=CategoryID)
            self.entCategoryID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblCategoryName = Label(MidFrame1, font=('arial', 12, 'bold'), text="CategoryName", bd=7)
            self.lblCategoryName.grid(row=2, column=0, sticky=W, padx=5)
            self.entCategoryName = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=CategoryName)
            self.entCategoryName.grid(row=2, column=1, sticky=W, padx=5)

        elif self.window=='Subcategories':
            self.lblSubcategoryID = Label(MidFrame1, font=('arial', 12, 'bold'), text="SubcategoryID", bd=7)
            self.lblSubcategoryID.grid(row=1, column=0, sticky=W, padx=5)
            self.entSubcategoryID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=SubcategoryID)
            self.entSubcategoryID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblSubcategoryName = Label(MidFrame1, font=('arial', 12, 'bold'), text="SubcategoryName", bd=7)
            self.lblSubcategoryName.grid(row=2, column=0, sticky=W, padx=5)
            self.entSubcategoryName = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=SubcategoryName)
            self.entSubcategoryName.grid(row=2, column=1, sticky=W, padx=5)

            self.lblCategory = Label(MidFrame1, font=('arial', 12, 'bold'), text="Category", bd=5)
            self.lblCategory.grid(row=3, column=0, sticky=W, padx=5)
            self.cboCategory = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                          textvariable=Category)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(CategoryName) as my_col from Categories")
            category_list = functions.Separate(cur.fetchall())
            self.cboCategory['values'] = category_list
            self.cboCategory.current(0)
            self.cboCategory.grid(row=3, column=1)

        elif self.window=='Orders':
            self.lblOrderID = Label(MidFrame1, font=('arial', 12, 'bold'), text="OrderID", bd=7)
            self.lblOrderID.grid(row=1, column=0, sticky=W, padx=5)
            self.entOrderID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=OrderID)
            self.entOrderID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblCustomer = Label(MidFrame1, font=('arial', 12, 'bold'), text="Customer", bd=7)
            self.lblCustomer.grid(row=2, column=0, sticky=W, padx=5)
            self.cboCustomer = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                         textvariable=Customer)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(Surname) as my_col from Customers")
            customer_list = functions.Separate(cur.fetchall())
            self.cboCustomer['values'] = customer_list
            self.cboCustomer.current(0)
            self.cboCustomer.grid(row=2, column=1)

            self.lblOrderStatus = Label(MidFrame1, font=('arial', 12, 'bold'), text="OrderStatus", bd=5)
            self.lblOrderStatus.grid(row=3, column=0, sticky=W, padx=5)
            self.cboOrderStatus = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                            textvariable=OrderStatus)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            self.cboOrderStatus['values']= (' ', 'Delivered', 'Confirmed', 'Cancelled', 'Shipped')
            self.cboOrderStatus.current(0)
            self.cboOrderStatus.grid(row=3, column=1)

            self.lblOrderDate = Label(MidFrame1, font=('arial', 12, 'bold'), text="OrderDate", bd=7)
            self.lblOrderDate.grid(row=4, column=0, sticky=W, padx=5)
            self.entOrderDate = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                            textvariable=OrderDate)
            self.entOrderDate.grid(row=4, column=1, sticky=W, padx=5)

            self.lblShippedDate = Label(MidFrame1, font=('arial', 12, 'bold'), text="ShippedDate", bd=7)
            self.lblShippedDate.grid(row=5, column=0, sticky=W, padx=5)
            self.entShippedDate = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=ShippedDate)
            self.entShippedDate.grid(row=5, column=1, sticky=W, padx=5)

        elif self.window == 'Products':
            self.lblProductID = Label(MidFrame1, font=('arial', 12, 'bold'), text="ProductID", bd=7)
            self.lblProductID.grid(row=1, column=0, sticky=W, padx=5)
            self.entProductID = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=ProductID)
            self.entProductID.grid(row=1, column=1, sticky=W, padx=5)

            self.lblProductName = Label(MidFrame1, font=('arial', 12, 'bold'), text="ProductName", bd=7)
            self.lblProductName.grid(row=2, column=0, sticky=W, padx=5)
            self.entProductName = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=ProductName)
            self.entProductName.grid(row=2, column=1, sticky=W, padx=5)

            self.lblListPrice = Label(MidFrame1, font=('arial', 12, 'bold'), text="ListPrice", bd=7)
            self.lblListPrice.grid(row=3, column=0, sticky=W, padx=5)
            self.entListPrice = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                    textvariable=ListPrice)
            self.entListPrice.grid(row=3, column=1, sticky=W, padx=5)

            self.lblProductBrand = Label(MidFrame1, font=('arial', 12, 'bold'), text="ProductBrand", bd=7)
            self.lblProductBrand.grid(row=4, column=0, sticky=W, padx=5)
            self.cboProductBrand = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                            textvariable=ProductBrand)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(BrandName) as my_col from Brands")
            brands_list = functions.Separate(cur.fetchall())
            self.cboProductBrand['values'] = brands_list
            self.cboProductBrand.current(0)
            self.cboProductBrand.grid(row=4, column=1)

            self.lblProductCategory = Label(MidFrame1, font=('arial', 12, 'bold'), text="ProductCategory", bd=7)
            self.lblProductCategory.grid(row=5, column=0, sticky=W, padx=5)
            self.cboProductCategory = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                                textvariable=ProductCategory)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(CategoryName) as my_col from Categories")
            category_list = functions.Separate(cur.fetchall())
            self.cboProductCategory['values'] = category_list
            self.cboProductCategory.current(0)
            self.cboProductCategory.grid(row=5, column=1)

        elif self.window == 'OrderItems':
            self.lblOrderItemID = Label(MidFrame1, font=('arial', 12, 'bold'), text="OrderItemID", bd=7)
            self.lblOrderItemID.grid(row=0, column=0, sticky=W, padx=5)
            self.cboOrderItemID = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                                   textvariable=OrderItemID)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(OrderID) as my_col from Orders")
            order_list = functions.Separate(cur.fetchall())
            self.cboOrderItemID['values'] = order_list
            self.cboOrderItemID.current(0)
            self.cboOrderItemID.grid(row=0, column=1)

            self.lblProductItemID = Label(MidFrame1, font=('arial', 12, 'bold'), text="ProductItemID", bd=7)
            self.lblProductItemID.grid(row=1, column=0, sticky=W, padx=5)
            self.cboProductItemID = ttk.Combobox(MidFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                               textvariable=ProductItemID)
            sqlCon = pymysql.connect(host="localhost", user="root", password="rooter", database='electronic_store')
            cur = sqlCon.cursor()
            cur.execute("select group_concat(ProductID) as my_col from Products")
            products_list = functions.Separate(cur.fetchall())
            self.cboProductItemID['values'] = products_list
            self.cboProductItemID.current(0)
            self.cboProductItemID.grid(row=1, column=1)

            self.lblQuantity = Label(MidFrame1, font=('arial', 12, 'bold'), text="Quantity", bd=7)
            self.lblQuantity.grid(row=3, column=0, sticky=W, padx=5)
            self.entQuantity = Entry(MidFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=Quantity)
            self.entQuantity.grid(row=3, column=1, sticky=W, padx=5)

        #========================================Table Treeview===================================================
        scroll_y= Scrollbar(MidFrame, orient=VERTICAL)
        if self.window=='Customers':
            self.data_records=ttk.Treeview(MidFrame, height=14, columns=("CustomerID", "FirstName", "Surname", "Address", "Gender", "Mobile"),
                                               xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('CustomerID', text='CustomerID')
            self.data_records.heading('FirstName', text='FirstName')
            self.data_records.heading('Surname', text='Surname')
            self.data_records.heading('Address', text='Address')
            self.data_records.heading('Gender', text='Gender')
            self.data_records.heading('Mobile', text='Mobile')

            self.data_records['show']='headings'

            self.data_records.column('CustomerID', width=75)
            self.data_records.column('FirstName', width=80)
            self.data_records.column('Surname', width=90)
            self.data_records.column('Address', width=100)
            self.data_records.column('Gender', width=70)
            self.data_records.column('Mobile', width=70)

        elif self.window=='Brands':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
            "BrandID", "BrandName"),xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('BrandID', text='BrandID')
            self.data_records.heading('BrandName', text='BrandName')
            self.data_records['show'] = 'headings'
            self.data_records.column('BrandID', width=100)
            self.data_records.column('BrandName', width=100)

        elif self.window=='Categories':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
            "CategoryID", "CategoryName"),xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('CategoryID', text='CategoryID')
            self.data_records.heading('CategoryName', text='CategoryName')
            self.data_records['show'] = 'headings'
            self.data_records.column('CategoryID', width=100)
            self.data_records.column('CategoryName', width=100)

        elif self.window=='Subcategories':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
            "SubcategoryID", "SubcategoryName", "CategoryID"),xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('SubcategoryID', text='SubcategoryID')
            self.data_records.heading('SubcategoryName', text='SubcategoryName')
            self.data_records.heading('CategoryID', text='Category')
            self.data_records['show'] = 'headings'
            self.data_records.column('SubcategoryID', width=100)
            self.data_records.column('SubcategoryName', width=100)
            self.data_records.column('CategoryID', width=100)

        elif self.window=='Orders':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
                "OrderID", "CustomerID", "OrderStatus", "OrderDate", "ShippedDate"), xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('OrderID', text='OrderID')
            self.data_records.heading('CustomerID', text='CustomerID')
            self.data_records.heading('OrderStatus', text='OrderStatus')
            self.data_records.heading('OrderDate', text='OrderDate')
            self.data_records.heading('ShippedDate', text='ShippedDate')

            self.data_records['show'] = 'headings'
            self.data_records.column('OrderID',width=100)
            self.data_records.column('CustomerID', width=100)
            self.data_records.column('OrderStatus', width=100)
            self.data_records.column('OrderDate', width=100)
            self.data_records.column('ShippedDate', width=100)

        elif self.window=='Products':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
                "ProductID", "ProductName", "ProductCategory", "ProductBrand", "ListPrice"), xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('ProductID', text='ProductID')
            self.data_records.heading('ProductName', text='ProductName')
            self.data_records.heading('ProductCategory', text='ProductCategory')
            self.data_records.heading('ProductBrand', text='ProductBrand')
            self.data_records.heading('ListPrice', text='ListPrice')

            self.data_records['show'] = 'headings'
            self.data_records.column('ProductID', width=100)
            self.data_records.column('ProductName', width=100)
            self.data_records.column('ProductCategory', width=100)
            self.data_records.column('ProductBrand', width=100)
            self.data_records.column('ListPrice', width=100)

        elif self.window == 'OrderItems':
            self.data_records = ttk.Treeview(MidFrame, height=14, columns=(
                "OrderItemID", "ProductItemID", "Quantity"), xscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            self.data_records.heading('OrderItemID', text='OrderItemID')
            self.data_records.heading('ProductItemID', text='ProductItemID')
            self.data_records.heading('Quantity', text='Quantity')

            self.data_records['show'] = 'headings'
            self.data_records.column('OrderItemID', width=100)
            self.data_records.column('ProductItemID', width=100)
            self.data_records.column('Quantity', width=100)


        self.data_records.pack(fill=BOTH, expand=1)
        self.data_records.bind("<ButtonRelease-1>", Info)
        functions.DisplayData(window, self.data_records)

        #===============================================================
        # Tabels buttons
        self.btnCustomers = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Customers", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "Customers", 'DodgerBlue')).grid(row=0, column=0, padx=1)
        self.btnProducts = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Products", bd=4, pady=1, padx=24,width=8, height=2, command=partial(seq, "Products", 'SkyBlue2')).grid(row=1, column=0, padx=1)
        self.btnOrders = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Orders", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "Orders", 'OliveDrab1')).grid(row=2, column=0, padx=1)
        self.btnOrderItems = Button(LeftFrame1, font=('arial', 16, 'bold'), text="OrderItems", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "OrderItems", 'OliveDrab1')).grid(row=3, column=0, padx=1)
        self.btnBrands = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Brands", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "Brands", 'SkyBlue2')).grid(row=4, column=0, padx=1)
        self.btnCategories = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Categories", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "Categories", 'Pale green')).grid(row=5, column=0, padx=1)
        self.btnSubcategories = Button(LeftFrame1, font=('arial', 16, 'bold'), text="Subcategories", bd=4, pady=1, padx=24, width=8,height=2, command=partial(seq, "Subcategories", 'Indian red')).grid(row=6, column=0, padx=1)

        # Operation butttons
        self.btnAddNew=Button(RightFrame1a, font=('arial', 16, 'bold'), text="AddNew", bd=4, pady=1, padx=24, width=8, height=2, command=addData).grid(row=0, column=0, padx=1)
        self.btnDisplay=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24, width=8, height=2, command=partial(functions.DisplayData, window, self.data_records)).grid(row=1, column=0, padx=1)
        self.btnUpdate=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8, height=2, command=update).grid(row=2, column=0, padx=1)
        self.btnDelete=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8, height=2, command=Delete).grid(row=3, column=0, padx=1)
        self.btnSearch=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8, height=2).grid(row=4, column=0, padx=1)
        self.btnReset=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8, height=2, command=Reset).grid(row=5, column=0, padx=1)
        self.btnExit=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8, height=2, command=partial(functions.iExit, root)).grid(row=6, column=0, padx=1)


if __name__=='__main__':
    root = Tk()
    window="Customers"
    color='DodgerBlue'
    application = ConnectorDB(root, window, color)
    root.mainloop()