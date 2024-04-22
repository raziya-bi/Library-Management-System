from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x900+0+0")

        # ======================= Variable ========================

        self.member_type_var = StringVar()
        self.prn_no_var = StringVar()
        self.title_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.post_id_var = StringVar()  
        self.mobile_var = StringVar()
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.author_var = StringVar()
        self.date_borrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.days_on_book_var = StringVar()
        self.late_return_fine_var = StringVar()
        self.date_over_due_var = StringVar()
        self.final_price_var = StringVar()

        label_title = Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM" , bg = "powder blue", fg = "green", bd = 12, relief = RIDGE, font = ("times new roman",25,"bold"),padx=2,pady=4)
        label_title.pack(side = TOP, fill = X )

        frame = Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg = "powder blue")
        frame.place(x=0, y=65, width = 1534, height = 400)

        #====================  Data Frame Left ==================== 

        DataFrameLeft = LabelFrame(frame,text = "  Library Membership Information  " , bg = "powder blue", fg = "green", bd = 15, relief = RIDGE, font = ("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=1, y=10, width = 750 , height = 350)
        
        label_member = Label(DataFrameLeft, bg="powder blue", fg="black", text="Member_Type", font=("times new roman", 10, "bold"), padx=24, pady=10)
        label_member.grid(row=0, column = 0, sticky = W)
    
        combo_member = ttk.Combobox(DataFrameLeft, state = "readonly" , textvariable=self.member_type_var, font = ("arial",8,"bold"),width = 24)
        combo_member["value"] = ("Admin Staff", "Student","Lecturer" )
        combo_member.grid(row = 0, column = 1 )
        
        label_PRN = Label(DataFrameLeft, bg="powder blue", fg="black", text = "PRN_No.", font=("times new roman", 10, "bold"), padx=24, pady=7)
        label_PRN.grid(row=1, column = 0, sticky = W)
        txtPRN_No = Entry(DataFrameLeft, font = ("arail",8,"bold"),textvariable=self.prn_no_var, width = 27)
        txtPRN_No.grid(row=1,column=1)
        
        label_id_no = Label(DataFrameLeft, bg="powder blue", fg="black", text = "ID No.", font=("times new roman", 10, "bold"), padx=24, pady=7)
        label_id_no.grid(row=2, column =0, sticky = W)
        txt_id_no = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.title_var, width = 27)
        txt_id_no.grid(row=2,column=1)

        label_first_name = Label(DataFrameLeft, bg="powder blue", fg="black", text="First_Name", font=("times new roman", 10, "bold"), padx=24, pady=7)
        label_first_name.grid(row=3, column = 0, sticky = W)
        txt_first_name = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.first_name_var , width = 27)
        txt_first_name.grid(row=3,column=1)

        label_last_name = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Last_Name", font = ("times new roman",10,"bold"),padx = 24, pady = 7)
        label_last_name.grid(row=4, column = 0, sticky = W)
        txt_last_name = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.last_name_var, width = 27)
        txt_last_name.grid(row=4,column=1)

        label_address1 = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Address_1", font = ("times new roman",10,"bold"),padx = 24, pady = 7)
        label_address1.grid(row=5, column = 0 , sticky = W)
        txt_address1 = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.address1_var, width = 27 )
        txt_address1 .grid(row=5,column=1)

        label_address2 = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Address_2", font = ("times new roman",10,"bold"),padx = 24, pady = 7)
        label_address2 .grid(row=6, column =0 , sticky = W)
        txt_address2 = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.address2_var , width = 27)
        txt_address2 .grid(row=6,column=1)

        label_post_code = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Post Code", font = ("times new roman",10,"bold"),padx = 24, pady = 7)
        label_post_code.grid(row=7, column = 0, sticky = W)
        txt_post_code= Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.post_id_var , width = 27)
        txt_post_code.grid(row=7,column = 1)

        label_mobile = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Mobile", font = ("times new roman",10,"bold"),padx = 24, pady = 7)
        label_mobile.grid(row=8, column = 0, sticky = W)
        txt_mobile = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.mobile_var , width = 27)
        txt_mobile.grid(row=8,column=1)

        label_book_id = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Book_ID", font = ("times new roman",10,"bold"),padx = 30, pady = 7)
        label_book_id.grid(row=0, column = 2, sticky = W)
        txt_book_id = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.book_id_var , width = 40)
        txt_book_id.grid(row=0,column=3)

        label_book_title = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Book_Title", font = ("times new roman",10,"bold"),padx = 30, pady = 7)
        label_book_title.grid(row=1, column = 2, sticky = W)
        txt_book_title= Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.book_title_var , width = 40)
        txt_book_title.grid(row=1,column=3)

        label_author_name = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Author Name", font = ("times new roman",10,"bold"),padx = 30, pady = 7)
        label_author_name.grid(row=2, column = 2, sticky = W)
        txt_author_name = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.author_var , width = 40)
        txt_author_name.grid(row=2,column=3)

        label_date_borrowed = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Date_Borrowed", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_date_borrowed.grid(row=3, column = 2, sticky = W)
        txt_date_borrowed = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.date_borrowed_var , width = 40)
        txt_date_borrowed.grid(row=3,column=3)

        label_due_date = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Due Date", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_due_date.grid(row=4, column = 2, sticky = W)
        txt_due_date = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.date_due_var , width = 40)
        txt_due_date.grid(row=4,column=3)

        label_Days_on_Book_on_book = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Days_on_Book", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_Days_on_Book_on_book.grid(row=5, column = 2, sticky = W)
        txt_Days_on_Book_on_book = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.days_on_book_var , width = 40)
        txt_Days_on_Book_on_book.grid(row=5,column=3)

        label_late_return_fine = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Late_Return_Fine", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_late_return_fine.grid(row=6, column = 2, sticky = W)
        txt_late_return_fine = Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.late_return_fine_var, width = 40)
        txt_late_return_fine.grid(row=6,column=3)

        label_date_overdue = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Date_Over_Due", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_date_overdue.grid(row=7, column = 2, sticky = W)
        txt_date_overdue = Entry(DataFrameLeft,font = ("arail",8,"bold"), textvariable=self.date_over_due_var , width = 40)
        txt_date_overdue.grid(row=7,column=3)

        label_actual_price = Label(DataFrameLeft, bg = "powder blue", fg="black", text= "Actual Price", font = ("times new roman",10,"bold"),padx = 30, pady = 5)
        label_actual_price.grid(row=8, column =2 , sticky = W)
        txt_actual_price= Entry(DataFrameLeft,font = ("arail",8,"bold"),textvariable=self.final_price_var , width = 40)
        txt_actual_price.grid(row=8,column=3)

        # ==================== Data Frame Right ==================== 

        DataFrameRight = LabelFrame(frame,text = "  Book Details  " , bg = "powder blue", fg = "green", bd = 15, relief = RIDGE, font = ("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x= 770, y=10, width = 700, height = 350)

        self.txtbox = Text(DataFrameRight, font = ("arail", 10,"bold"), width = 41  , height = 18, padx=6, pady = 6)
        self.txtbox.grid(row=0, column=2)

        list_scroll_bar = Scrollbar(DataFrameRight)
        list_scroll_bar.grid(row=0, column=1, sticky = "ns")

        Listbooks = ["Clean Code", "Pragmatic Programmer", "Design Patterns", "Effective Java", "Coding Interview", "JavaScript",
                     "Python Crash", "Head First Design", "Introduction to Algorithms", "Code Complete", "Refactoring", 
                     "Programming Pearls", "Mythical Man-Month", "Structure and Interpretation", "Clean Architecture", "Algorithms", 
                     "C Programming", "Domain-Driven Design", "Test-Driven Development", "Operating System Concepts" ]
        
        def SelectBook(event = ""):
            value = str(List_box.get(List_box.curselection()))
            x = value

            # ================ Book Info ============================
            if (x == "Clean Code"):
                self.book_id_var.set("BKID5454")
                self.book_title_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs.50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 788")

            elif (x == "Pragmatic Programmer"):
                self.book_id_var.set("BKID5455")
                self.book_title_var.set("The Pragmatic Programmer")
                self.author_var.set("Andrew Hunt, David Thomas")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 950")

            elif (x == "Design Patterns"):
                self.book_id_var.set("BKID5456")
                self.book_title_var.set("Design Patterns")
                self.author_var.set("Erich Gamma, Richard Helm, Ralph Johnson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1100")


            elif (x == "Effective Java"):
                self.book_id_var.set("BKID5457")
                self.book_title_var.set("Effective Java")
                self.author_var.set("Joshua Bloch")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1200")

            elif (x == "Coding Interview"):
                self.book_id_var.set("BKID5458")
                self.book_title_var.set("Cracking the Coding Interview")
                self.author_var.set("Gayle Laakmann McDowell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1050")

            elif (x == "JavaScript"):
                self.book_id_var.set("BKID5459")
                self.book_title_var.set("JavaScript: The Good Parts")
                self.author_var.set("Douglas Crockford")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 950")

            elif (x == "Python Crash"):
                self.book_id_var.set("BKID5460")
                self.book_title_var.set("Python Crash Course")
                self.author_var.set("Eric Matthes")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 800")

            elif (x == "Head First Design"):
                self.book_id_var.set("BKID5461")
                self.book_title_var.set("Head First Design Patterns")
                self.author_var.set("Eric Freeman, Elisabeth Robson, Bert Bates")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1200")

            elif (x == "Introduction to Algorithms"):
                self.book_id_var.set("BKID5462")
                self.book_title_var.set("Introduction to Algorithms")
                self.author_var.set("Thomas H. Cormen, Charles E. Leiserson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1500")

            elif (x == "Code Complete"):
                self.book_id_var.set("BKID5463")
                self.book_title_var.set("Code Complete of Software Construction")
                self.author_var.set("Steve McConnell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1600")

            elif (x == "Refactoring"):
                self.book_id_var.set("BKID5464")
                self.book_title_var.set("Refactoring")
                self.author_var.set("Martin Fowler")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1700")

            elif (x == "Programming Pearls"):
                self.book_id_var.set("BKID5465")
                self.book_title_var.set("Programming Pearls")
                self.author_var.set("Jon Bentley")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1400")

            elif (x == "Mythical Man-Month"):
                self.book_id_var.set("BKID5466")
                self.book_title_var.set("The Mythical Man-Month")
                self.author_var.set("Fred Brooks")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1500")

            elif (x == "Structure and Interpretation"):
                self.book_id_var.set("BKID5467")
                self.book_title_var.set("Structure & Interpretation")
                self.author_var.set("Harold Abelson, Gerald Jay Sussman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1800")

            elif (x == "Clean Architecture"):
                self.book_id_var.set("BKID5468")
                self.book_title_var.set("Clean Architecture")
                self.author_var.set("Robert C. Martin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1600")

            elif (x == "Algorithms"):
                self.book_id_var.set("BKID5469")
                self.book_title_var.set("Algorithms")
                self.author_var.set("Robert Sedgewick, Kevin Wayne")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1700")

            elif (x == "C Programming"):
                self.book_id_var.set("BKID5470")
                self.book_title_var.set("C Programming Language")
                self.author_var.set("Brian W. Kernighan, Dennis M. Ritchie")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1500")

            elif (x == "Domain-Driven Design"):
                self.book_id_var.set("BKID5471")
                self.book_title_var.set("Domain-Driven Design")
                self.author_var.set("Eric Evans")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1800")

            elif (x == "Test-Driven Development"):
                self.book_id_var.set("BKID5472")
                self.book_title_var.set("Test-Driven Development")
                self.author_var.set("Kent Beck")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1600")

            elif (x == "Operating System Concepts"):
                self.book_id_var.set("BKID5473")
                self.book_title_var.set("Operating System Concepts")
                self.author_var.set("Abraham Silberschatz, Greg Gagne")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book_var.set(15)
                self.late_return_fine_var.set("Rs. 50")
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs. 1700")

        # ================== Book Info =============================

        List_box = Listbox(DataFrameRight, font = ("arail",10,"bold"), width = 46, height = 17)
        List_box.bind("<<ListboxSelect>>", SelectBook)
        List_box.grid(row = 0, column =0, padx = 6)
        list_scroll_bar.config(command = List_box.yview)

        for item in Listbooks:
            List_box.insert(END,item)

        # ==================== Buttons Frames ==================== 

        frame_button = Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg = "powder blue")
        frame_button.place(x=0, y=460, width = 1534, height = 70)

        button_add_data = Button(frame_button, command=self.add_data, text = "Add Data", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 0)

        button_add_data = Button(frame_button,command = self.show_data, text = "Show Data", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 1)

        button_add_data = Button(frame_button, command = self.update, text = "Update Data", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 2)

        button_add_data = Button(frame_button, command = self.delete, text = "Delete", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 3)

        button_add_data = Button(frame_button, command = self.reset, text = "Reset", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 4)

        button_add_data = Button(frame_button, command = self.exit, text = "Exit", font = ("arail",10,"bold"), width = 29, height = 2, bg = "blue", fg = "white")
        button_add_data.grid(row =0, column = 5)

        # ==================== Information Frame ==================== 

        frame_details = Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg = "powder blue")
        frame_details.place(x=0, y=525, width = 1534, height = 265)

        table_frame = Frame(frame_details, bd = 6, relief = RIDGE, bg = "powder blue")
        table_frame.place(x=0, y=5, width = 1480, height = 230)

        x_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)    
        y_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, column =("Member_Type","PRN_No.","Title", "First_Name", "Last_Name", "Address_1", "Address_2" , 
                                                               "Post_ID", "Mobile", "Book_ID", "Book_Title", "Author", "Date_Borrowed", "Date_Due", "Days_on_Book",
                                                                 "Late_Return_Fine", "Date_Over_Due", "Final_Price"),xscrollcommand = x_scroll.set, yscrollcommand =y_scroll)
        
        x_scroll.pack(side=BOTTOM, fill = X)
        y_scroll.pack(side=RIGHT, fill= Y)

        x_scroll.config(command=self.library_table.xview)
        y_scroll.config(command=self.library_table.yview)

        self.library_table.heading( "Member_Type", text = "Member_Type")
        self.library_table.heading( "PRN_No." , text = "PRN_No.")
        self.library_table.heading( "Title", text = "Title")
        self.library_table.heading( "First_Name", text = "First_Name")
        self.library_table.heading( "Last_Name", text = "Last_Name")
        self.library_table.heading( "Address_1", text = "Address_1")
        self.library_table.heading( "Address_2", text = "Address_2")
        self.library_table.heading( "Post_ID", text = "Post_ID")
        self.library_table.heading( "Mobile", text = "Mobile")
        self.library_table.heading( "Book_ID", text = "Book_ID")
        self.library_table.heading( "Book_Title", text = "Book_Title")
        self.library_table.heading( "Author", text = "Author")
        self.library_table.heading( "Date_Borrowed", text = "Date_Borrowed")
        self.library_table.heading( "Date_Due", text = "Date_Due")
        self.library_table.heading( "Days_on_Book", text = "Days_on_Book")
        self.library_table.heading( "Late_Return_Fine", text = "Late_Return_Fine")
        self.library_table.heading( "Date_Over_Due", text = "Date_Over_Due")
        self.library_table.heading( "Final_Price", text = "Final_Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member_Type", width=100)
        self.library_table.column("PRN_No.", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("First_Name", width=100)
        self.library_table.column("Last_Name", width=100)
        self.library_table.column("Address_1", width=100)
        self.library_table.column("Address_2", width=100)
        self.library_table.column("Post_ID", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("Book_ID", width=100)
        self.library_table.column("Book_Title", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Date_Borrowed", width=100)
        self.library_table.column("Date_Due", width=100)
        self.library_table.column("Days_on_Book", width=100)
        self.library_table.column("Late_Return_Fine", width=100)
        self.library_table.column("Date_Over_Due", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        connection = mysql.connector.connect(host="localhost", username = "root" , password = "729492" , database = "library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("INSERT into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( 
                                                                                                                    self.member_type_var.get(),
                                                                                                                    self.prn_no_var.get(),
                                                                                                                    self.title_var.get(),
                                                                                                                    self.first_name_var.get(),
                                                                                                                    self.last_name_var.get(),
                                                                                                                    self.address1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.post_id_var.get(),
                                                                                                                    self.mobile_var.get(),
                                                                                                                    self.book_id_var.get(),
                                                                                                                    self.book_title_var.get(),
                                                                                                                    self.author_var.get(),
                                                                                                                    self.date_borrowed_var.get(),
                                                                                                                    self.date_due_var.get(),
                                                                                                                    self.days_on_book_var.get(),
                                                                                                                    self.late_return_fine_var.get(),
                                                                                                                    self.date_over_due_var.get(),
                                                                                                                    self.final_price_var.get()
                                                                                                                ) )

        connection.commit()
        self.fetch_data()
        connection.close()

        messagebox.showinfo("Success", "Member has been successfully added!")


    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username = "root" , password = "729492" , database = "library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("Select * from library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())

            for i in rows:
                self.library_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_type_var.set(row[0])
        self.prn_no_var.set(row[1])
        self.title_var.set(row[2])
        self.first_name_var.set(row[3])
        self.last_name_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.post_id_var.set(row[7])
        self.mobile_var.set(row[8])
        self.book_id_var.set(row[9])
        self.book_title_var.set(row[10])
        self.author_var.set(row[11])
        self.date_borrowed_var.set(row[12])
        self.date_due_var.set(row[13])
        self.days_on_book_var.set(row[14])
        self.late_return_fine_var.set(row[15])
        self.date_over_due_var.set(row[16])
        self.final_price_var.set(row[17])


    def show_data(self):
        self.txtbox.insert(END, "Member_Type\t\t" + self.member_type_var.get() + "\n")
        self.txtbox.insert(END, "PRN_No\t\t" + self.prn_no_var.get() + "\n")
        self.txtbox.insert(END, "ID\t\t" + self.title_var.get() + "\n")
        self.txtbox.insert(END, "First_Name\t\t" + self.first_name_var.get() + "\n")
        self.txtbox.insert(END, "Last_Name\t\t" + self.last_name_var.get() + "\n")
        self.txtbox.insert(END, "Address_1\t\t" + self.address1_var.get() + "\n")
        self.txtbox.insert(END, "Address_2\t\t" + self.address2_var.get() + "\n")
        self.txtbox.insert(END, "Post_ID\t\t" + self.post_id_var.get() + "\n")
        self.txtbox.insert(END, "Mobile\t\t" + self.mobile_var.get() + "\n")
        self.txtbox.insert(END, "Book_ID\t\t" + self.book_id_var.get() + "\n")
        self.txtbox.insert(END, "Book_Title\t\t" + self.book_title_var.get() + "\n")
        self.txtbox.insert(END, "Author\t\t" + self.author_var.get() + "\n")
        self.txtbox.insert(END, "Date_Borrowed\t\t" + self.date_borrowed_var.get() + "\n")
        self.txtbox.insert(END, "Date_Due\t\t" + self.date_due_var.get() + "\n")
        self.txtbox.insert(END, "Days_on_Book\t\t" + self.days_on_book_var.get() + "\n")
        self.txtbox.insert(END, "Late_Return_Fine\t\t" + self.late_return_fine_var.get() + "\n")
        self.txtbox.insert(END, "Date_Over_Due\t\t" + self.date_over_due_var.get() + "\n")
        self.txtbox.insert(END, "Final_Price\t\t" + self.final_price_var.get() + "\n")

    def update(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="729492", database="library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("UPDATE library SET `Member Type` = %s, `ID` = %s, `First Name` = %s, `Last Name` = %s, `Address 1` = %s, `Address 2` = %s, `Post ID` = %s, `Mobile` = %s, `Book ID` = %s, `Book Title` = %s, `Author` = %s, `Date Borrowed` = %s, `Date Due` = %s, `Days on Book` = %s, `Late Return Fine` = %s, `Date Over Due` = %s, `Final Price` = %s WHERE `PRN No` = %s", (
                                                                                                                                                                                                                                                                                                                                                                                                self.member_type_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.title_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.first_name_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.last_name_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.address1_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.address2_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.post_id_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.mobile_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.book_id_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.book_title_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.author_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.date_borrowed_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.date_due_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.days_on_book_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.late_return_fine_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.date_over_due_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.final_price_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                self.prn_no_var.get()
                                                                                                                                                                                                                                                                                                                                                                                            ))

        connection.commit()
        self.fetch_data()
        self.reset()
        connection.close()
        messagebox.showinfo("Success", "Member has been updated")


    def delete(self):
        if self.prn_no_var.get()=="" or self.title_var.get() == "":
            messagebox.showerror("Error", "First Select the Member")
        else:
            connection = mysql.connector.connect(host="localhost", username = "root" , password = "729492" , database = "library_management_system")
            my_cursor = connection.cursor()
            query = "DELETE FROM library WHERE `PRN No` = %s"
            value = (self.prn_no_var.get(),)
            my_cursor.execute(query, value)

            connection.commit()
            self.fetch_data()
            self.reset()
            connection.close()
            messagebox.showinfo("Success","Member has been deleted")

    def reset(self):
        self.member_type_var.set("")
        self.prn_no_var.set("")
        self.title_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.post_id_var.set("")
        self.mobile_var.set("")
        self.book_id_var.set("")
        self.book_title_var.set("")
        self.author_var.set("")
        self.date_borrowed_var.set("")
        self.date_due_var.set("")
        self.days_on_book_var.set("")
        self.late_return_fine_var.set("")
        self.date_over_due_var.set("")
        self.final_price_var.set("")
        self.txtbox.delete("1.0", END)

    def exit(self):
        exit = tkinter.messagebox.askquestion("Library Management System", "Do you want to exit?")
        if exit == 'yes':
            self.root.destroy()
            return

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop() # It makes the window stay- so that it does not close