from tkinter import *
import tkinter.messagebox

class window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('700x500+250+101')
        self.frame = Frame(self.master,bg ='#231441')
        self.frame.grid(padx=1)
        self.master.resizable(False, False)

        #==========================first frame==================#
        self.first_frame = Frame(self.frame)
        self.first_frame.grid(row=0,column=0,padx=20)
        self.text1 = Label(self.first_frame, text='Hospital Management System', bg='#231441', fg='white',font=('arial','14','bold'),bd=10)
        self.text1.grid()
        #===========================second frame=================#
        self.sec_frame = Frame(self.frame, width=650, height=430, bd=7, relief='ridge')
        self.sec_frame.grid(row=1, column=0, padx=20)
        self.sec_frame.grid_propagate(0)
        self.login_frame1 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame1.grid(row=1, column=0,pady=15,)
        self.login_frame2 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame2.grid(row=2, column=0, padx=12, pady=5)
        self.login_frame3 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame3.grid(row=3, column=0, pady=100)
        #=====================================================================================================#
        self.username = StringVar()
        self.password = StringVar()

        self.lb_username = Label(self.login_frame1, text='Username', font=('arial',11,'bold'), bd=12)
        self.lb_username.grid(row=0, column=0)
        self.txt_username = Entry(self.login_frame1, text='Username', width=25, font=('arial', 12), textvariable = self.username)
        self.txt_username.grid(row=0, column=1, padx=10)
        self.lb_password = Label(self.login_frame1, text='Password', font=('arial', 11, 'bold'), bd=12)
        self.lb_password.grid(row=1, column=0)
        self.txt_Password = Entry(self.login_frame1, text='Password', width=25, font=('arial', 12), textvariable = self.password)
        self.txt_Password.grid(row=1, column=1, padx=10)
        # =====================================================================================================#

        self.login_btn = Button(self.login_frame2, text='Login',width=18,font=('arial',12,'bold'),command=self.login)
        self.login_btn.grid(row=0, column=0)
        self.reset_btn = Button(self.login_frame2, text='Reset',width=18,font=('arial',12,'bold'),command=self.reset)
        self.reset_btn.grid(row=0, column=1)
        self.exit_btn = Button(self.login_frame2, text='Exit',width=18,font=('arial',12,'bold'),command=self.exitt)
        self.exit_btn.grid(row=0, column=2)

        self.registration_btn = Button(self.login_frame3,width=20,text = 'Hospital Management', state = DISABLED, font=('arial',10,'bold'),command = self.Registration_window)
        self.registration_btn.grid(row=0, column=0)
        self.pharmacy_btn = Button(self.login_frame3, width=20,text = 'Patient Registration', state = DISABLED, font=('arial',10,'bold'),command = self.Pharmacy_window)
        self.pharmacy_btn.grid(row=0, column=1)

        # =====================================================================================================#

    def reset(self):
        self.registration_btn.config(state=DISABLED)
        self.pharmacy_btn.config(state=DISABLED)
        self.username.set("")
        self.password.set("")
        self.txt_username.focus()

    def exitt(self):
        self.ask_exit = tkinter.messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit')
        if self.ask_exit > 0:
            self.master.destroy()
            return

    def login(self):
        user = (self.username.get())
        pas = (self.password.get())
        if (user == str()) and (pas == str()):
            self.registration_btn.config(state=NORMAL)
            self.pharmacy_btn.config(state=NORMAL)
        else:
            tkinter.messagebox.showerror('Login Page', 'Invalid login, try again')
            self.registration_btn.config(state=DISABLED)
            self.pharmacy_btn.config(state=DISABLED)
            self.username.set("")
            self.password.set("")
            self.txt_username.focus()



        # ============+=========================================================================================#

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

    def Pharmacy_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window3(self.newWindow)

class window2:
    def __init__(self, master):
        self.master = master
        self.master.title('Patient System')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

#=================================================window 3========================================
class window3:
    def __init__(self, master2):
        self.master2 = master2
        self.master2.title('Patient Registration Page')
        self.master2.geometry('1200x700+200+0')
        self.p_frame = Frame(self.master2, bg ='#231441')
        self.p_frame.grid()
        self.master2.resizable(False, True)
        #=================================Variable declaration===============================#
        self.VrefNo = StringVar()
        self.VfName = StringVar()
        self.VlName = StringVar()
        self.VtelNo = StringVar()
        self.Vaddr = StringVar()
        self.VpCode = StringVar()
        #======================================================================================#

        # ====================================Frame=============================================#
        self.p_login_frame1 = Frame(self.p_frame)
        self.p_login_frame1.grid()
        self.text1 = Label(self.p_login_frame1, text = 'Patient Registration System', bg = '#231441',fg='white',font=('arial','14','bold'), bd=20)
        self.text1.grid()
        self.p_login_frame2 = Frame(self.p_frame, width=1100, height=500, bd=8, relief='ridge')
        self.p_login_frame2.grid(row=1, column=0)
                    #-------------inner frame-----------#
        self.inner1_frame2 = LabelFrame(self.p_login_frame2, width=300, height=500, bd=5)
        self.inner1_frame2.grid(row=0, column=0)
        self.inner2_frame2 = Frame(self.p_login_frame2, width=800, height=500, bd=5)
        self.inner2_frame2.grid(row=0, column=1)
                                 #-------------sub_inner1 frame---------#
        self.sub_inn_frame1 = LabelFrame(self.inner1_frame2, text='Customer Name', width=300, height=500, relief='ridge')
        self.sub_inn_frame1.grid()
        self.sub_inn_frame1.grid_propagate(0)
                                # -------------sub_inner2 frame---------#
        self.sub_inn_frame2 = LabelFrame(self.inner2_frame2, width=800, height=500, text='Information')
        self.sub_inn_frame2.grid()
        self.sub_inn_frame2.grid_propagate(0)
        # =======================================================================================#
        #sub inner frame datails
        self.display_details = Label(self.sub_inn_frame2, font=('arial','9','bold'),text='Reference No').grid(row =0, column=0, pady=10)
        self.display_details = Label(self.sub_inn_frame2, font=('arial','9','bold'),text='First Name').grid(row=0,column=1, pady=10)
        self.display_details = Label(self.sub_inn_frame2, font=('arial', '9', 'bold'), text='Last Name').grid(row=0,column=2,pady=10)
        self.display_details = Label(self.sub_inn_frame2, font=('arial', '9', 'bold'), text='Address').grid(row=0,column=3,pady=10)
        self.display_details = Label(self.sub_inn_frame2, font=('arial', '9', 'bold'), text='Postcode').grid(row=0,column=4,pady=10)
        self.display_details = Label(self.sub_inn_frame2, font=('arial', '9', 'bold'), text='Telephone No').grid(row=0,column=5,pady=10)

        self.textReceiptRN = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptRN.grid(row=1, column=0)

        self.textReceiptFN = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptFN.grid(row=1, column=1)

        self.textReceiptSN = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptSN.grid(row=1, column=2)

        self.textReceiptA = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptA.grid(row=1, column=3)

        self.textReceiptP = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptP.grid(row=1, column=4)

        self.textReceiptTN = Text(self.sub_inn_frame2, font=('arial','9',''), width=18, height=25, bg='white', state='disabled')
        self.textReceiptTN.grid(row=1, column=5)







        #=======================#
        self.refNo = Label(self.sub_inn_frame1, text = 'Reference No.', font=('arial', 10))
        self.refNo.grid(row=0, column=0, pady=10, sticky=W)
        self.refNo_entry =Entry(self.sub_inn_frame1, font=('arial', 10), bd=4, insertwidth=2, textvariable=self.VrefNo)
        self.refNo_entry.grid(row=0, column=1, padx=10)

        self.fName = Label(self.sub_inn_frame1, text = 'First Name.', font=('arial', 10))
        self.fName.grid(row=1, column=0, sticky=W,pady=10)
        self.fName_entry =Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,textvariable=self.VfName)
        self.fName_entry.grid(row=1, column=1, padx=10)

        self.lName = Label(self.sub_inn_frame1, text = 'Surname.', font=('arial', 10))
        self.lName.grid(row=2, column=0, sticky=W,pady=10)
        self.lName_entry =Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,textvariable=self.VlName)
        self.lName_entry.grid(row=2, column=1, padx=10)

        self.addr = Label(self.sub_inn_frame1, text = 'Address.', font=('arial', 10))
        self.addr.grid(row=3, column=0, sticky=W,pady=10)
        self.addr_entry =Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,textvariable=self.Vaddr)
        self.addr_entry.grid(row=3, column=1, padx=10)

        self.pCode = Label(self.sub_inn_frame1, text = 'Postcode', font=('arial', 10))
        self.pCode.grid(row=4, column=0, sticky=W, pady=10)
        self.pCode_entry =Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,textvariable=self.VpCode)
        self.pCode_entry.grid(row=4, column=1, padx=10)

        self.telNo = Label(self.sub_inn_frame1, text ='Telephone No.', font=('arial', 10))
        self.telNo.grid(row=5, column=0, sticky=W,pady=10)
        self.telNo_entry =Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,textvariable=self.VtelNo)
        self.telNo_entry.grid(row=5, column=1, padx=10)
            #-------------------------------------------------#
        self.submitbtn1 = Button(self.sub_inn_frame1, text='Submit',font=('arial',10,'bold'),
                                 width=10,command= self.submit).grid(column=0, sticky=SW, pady=170, row=6)
        self.submitbtn2 = Button(self.sub_inn_frame1, text='Reset',font=('arial', 10, 'bold'),
                                 width=10, command= self.reset).grid(column=1,sticky=SE,pady=170,row=6)
        #===================================Function Declaration====================================#

    def submit(self):
        patien_Vref = self.VrefNo.get()
        patien_fName = self.VfName.get()
        patien_lName = self.VlName.get()
        patien_addr = self.Vaddr.get()
        patien_pCode = self.VpCode.get()
        patien_telNO = self.VtelNo.get()

        self.textReceiptRN.config(state = 'normal')
        self.textReceiptRN.insert(END, self.VrefNo.get())
        self.textReceiptRN.insert(END, "\n")
        self.textReceiptRN.config(state='disabled')
        self.textReceiptRN.bind("<Button>", lambda event: self.textReceiptRN.focus_set())

        self.textReceiptFN.config(state = 'normal')
        self.textReceiptFN.insert(END, self.VfName.get())
        self.textReceiptFN.insert(END, "\n")
        self.textReceiptFN.config(state='disabled')
        self.textReceiptFN.bind("<Button>", lambda event: self.textReceiptFN.focus_set())

        self.textReceiptSN.config(state='normal')
        self.textReceiptSN.insert(END, self.VlName.get())
        self.textReceiptSN.insert(END, "\n")
        self.textReceiptSN.config(state='disabled')
        self.textReceiptSN.bind("<Button>", lambda event: self.textReceiptSN.focus_set())

        self.textReceiptA.config(state='normal')
        self.textReceiptA.insert(END, self.Vaddr.get())
        self.textReceiptA.insert(END, "\n")
        self.textReceiptA.config(state='disabled')
        self.textReceiptA.bind("<Button>", lambda event: self.textReceiptA.focus_set())

        self.textReceiptP.config(state='normal')
        self.textReceiptP.insert(END, self.VpCode.get())
        self.textReceiptP.insert(END, "\n")
        self.textReceiptP.config(state='disabled')
        self.textReceiptP.bind("<Button>", lambda event: self.textReceiptP.focus_set())

        self.textReceiptTN.config(state='normal')
        self.textReceiptTN.insert(END, self.VtelNo.get())
        self.textReceiptTN.insert(END, "\n")
        self.textReceiptTN.config(state='disabled')
        self.textReceiptTN.bind("<Button>", lambda event: self.textReceiptTN.focus_set())

        #yList = [patien_Vref,patien_fName,patien_lName,patien_addr,patien_pCode,patien_telNO]
        #for a in myList:
            #self.textReceipt.config(state='normal')
            #self.textReceipt.insert(END,"\t\t" + a)
            #self.textReceipt.insert(END, "\n")
            #self.textReceipt.config(state='disabled')
            #self.textReceipt.bind("<Button>", lambda event: self.textReceipt.focus_set())
    def reset(self):
        self.refNo_entry.delete(0, END)
        self.fName_entry.delete(0, END)
        self.lName_entry.delete(0, END)
        self.addr_entry.delete(0, END)
        self.pCode_entry.delete(0, END)
        self.telNo_entry.delete(0, END);





root = Tk()
window1(root)

root.mainloop()
