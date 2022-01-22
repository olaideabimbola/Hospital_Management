from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector





class window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('700x500+250+101')
        self.master.resizable(False, False)

        # ==========================first frame==================#
        self.first_frame = Frame(self.master)
        self.first_frame.grid(row=0, column=0, padx=20)
        self.text1 = Label(self.first_frame, text='Hospital Management System', bg='#231441', fg='white',
                           font=('arial', '14', 'bold'), bd=10)
        self.text1.grid()
        # ===========================second frame=================#
        self.sec_frame = Frame(self.master, width=650, height=430, bd=7, relief='ridge')
        self.sec_frame.grid(row=1, column=0, padx=20)
        self.sec_frame.grid_propagate(0)
        self.login_frame1 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame1.grid(row=1, column=0, pady=15, )
        self.login_frame2 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame2.grid(row=2, column=0, padx=12, pady=5)
        self.login_frame3 = Frame(self.sec_frame, bd=10, relief='ridge')
        self.login_frame3.grid(row=3, column=0, pady=100)
        # =====================================================================================================#
        self.username = StringVar()
        self.password = StringVar()

        self.lb_username = Label(self.login_frame1, text='Username', font=('arial', 11, 'bold'), bd=12)
        self.lb_username.grid(row=0, column=0)
        self.txt_username = Entry(self.login_frame1, text='Username', width=25, font=('arial', 12),
                                  textvariable=self.username)
        self.txt_username.grid(row=0, column=1, padx=10)
        self.lb_password = Label(self.login_frame1, text='Password', font=('arial', 11, 'bold'), bd=12)
        self.lb_password.grid(row=1, column=0)
        self.txt_Password = Entry(self.login_frame1, text='Password', width=25, font=('arial', 12),
                                  textvariable=self.password)
        self.txt_Password.grid(row=1, column=1, padx=10)
        # =====================================================================================================#

        self.login_btn = Button(self.login_frame2, text='Login', width=18, font=('arial', 12, 'bold'),
                                command=self.login)
        self.login_btn.grid(row=0, column=0)
        self.reset_btn = Button(self.login_frame2, text='Reset', width=18, font=('arial', 12, 'bold'),
                                command=self.reset)
        self.reset_btn.grid(row=0, column=1)
        self.exit_btn = Button(self.login_frame2, text='Exit', width=18, font=('arial', 12, 'bold'), command=self.exitt)
        self.exit_btn.grid(row=0, column=2)

        self.registration_btn = Button(self.login_frame3, width=20, text='Hospital Management', state=DISABLED,
                                       font=('arial', 10, 'bold'), command=self.Registration_window)
        self.registration_btn.grid(row=0, column=0)
        self.pharmacy_btn = Button(self.login_frame3, width=20, text='Patient Registration', state=DISABLED,
                                   font=('arial', 10, 'bold'), command=self.Pharmacy_window)
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
        self.newWindow = Toplevel()
        self.app = window3(self.newWindow)


# =================================================window 3========================================
class window3:
    def __init__(self, master2):
        self.master2 = master2
        self.master2.title('Patient Registration Page')
        self.master2.geometry('1200x700+200+0')
        self.p_frame = Frame(self.master2, bg='#231441')
        self.p_frame.grid()
        self.master2.resizable(False, True)
        # =================================Variable declaration===============================#
        self.VrefNo = StringVar()
        self.VfName = StringVar()
        self.VlName = StringVar()
        self.VtelNo = StringVar()
        self.Vaddr = StringVar()
        self.VpCode = StringVar()
        # ======================================================================================#

        # ====================================Frame=============================================#
        self.p_login_frame1 = Frame(self.p_frame)
        self.p_login_frame1.grid()
        self.text1 = Label(self.p_login_frame1, text='Patient Registration System', bg='#231441', fg='white',
                           font=('arial', '14'), bd=20)
        self.text1.grid()
        self.p_login_frame2 = Frame(self.p_frame, width=1100, height=500, bd=8, relief='ridge')
        self.p_login_frame2.grid(row=1, column=0)

        # -------------inner frame-----------#
        self.inner1_frame2 = LabelFrame(self.p_login_frame2, width=300, height=500, bd=5)
        self.inner1_frame2.grid(row=0, column=0)
        self.inner2_frame2 = Frame(self.p_login_frame2, width=800, height=500, bd=5)
        self.inner2_frame2.grid(row=0, column=1)

        # -------------sub_inner1 frame---------#
        self.sub_inn_frame1 = LabelFrame(self.inner1_frame2, text='Customer Name', width=300, height=500,
                                         relief='ridge')
        self.sub_inn_frame1.grid()
        self.sub_inn_frame1.grid_propagate(0)
        # -------------sub_inner2 frame---------#
        self.sub_inn_frame2 = LabelFrame(self.inner2_frame2, width=800, height=500, text='Information')
        self.sub_inn_frame2.grid()
        self.sub_inn_frame2.grid_propagate(0)
        # =======================================================================================#

        # sub inner frame datails

        self.tv = ttk.Treeview(self.sub_inn_frame2)
        self.tv['columns']=('Reference No', 'First Name', 'Last Name', 'Postcode', 'Address', 'Telephone No')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Reference No', anchor=CENTER, width=133)
        self.tv.column('First Name', anchor=CENTER, width=133)
        self.tv.column('Last Name', anchor=CENTER, width=133)
        self.tv.column('Address', anchor=CENTER, width=133)
        self.tv.column('Postcode', anchor=CENTER, width=133)
        self.tv.column('Telephone No', anchor=CENTER, width=133)
        self.tv.grid()

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Reference No', text="Reference No")
        self.tv.heading('First Name', text="First Name")
        self.tv.heading('Last Name', text="Surname")
        self.tv.heading('Address', text="Address")
        self.tv.heading('Postcode', text="Postcode")
        self.tv.heading('Telephone No', text="Telephone No")



        # =======================#
        self.refNo = Label(self.sub_inn_frame1, text='Reference No.', font=('arial', 10))
        self.refNo.grid(row=0, column=0, pady=10, sticky=W)
        self.refNo_entry = Entry(self.sub_inn_frame1, font=('arial', 10), bd=4, insertwidth=2, textvariable=self.VrefNo)
        self.refNo_entry.grid(row=0, column=1, padx=10)

        self.fName = Label(self.sub_inn_frame1, text='First Name.', font=('arial', 10))
        self.fName.grid(row=1, column=0, sticky=W, pady=10)
        self.fName_entry = Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,
                                 textvariable=self.VfName)
        self.fName_entry.grid(row=1, column=1, padx=10)

        self.lName = Label(self.sub_inn_frame1, text='Surname.', font=('arial', 10))
        self.lName.grid(row=2, column=0, sticky=W, pady=10)
        self.lName_entry = Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,
                                 textvariable=self.VlName)
        self.lName_entry.grid(row=2, column=1, padx=10)

        self.addr = Label(self.sub_inn_frame1, text='Address.', font=('arial', 10))
        self.addr.grid(row=3, column=0, sticky=W, pady=10)
        self.addr_entry = Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,
                                textvariable=self.Vaddr)
        self.addr_entry.grid(row=3, column=1, padx=10)

        self.pCode = Label(self.sub_inn_frame1, text='Postcode', font=('arial', 10))
        self.pCode.grid(row=4, column=0, sticky=W, pady=10)
        self.pCode_entry = Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,
                                 textvariable=self.VpCode)
        self.pCode_entry.grid(row=4, column=1, padx=10)

        self.telNo = Label(self.sub_inn_frame1, text='Telephone No.', font=('arial', 10))
        self.telNo.grid(row=5, column=0, sticky=W, pady=10)
        self.telNo_entry = Entry(self.sub_inn_frame1, font=('arial', 10, 'bold'), bd=4, insertwidth=2,
                                 textvariable=self.VtelNo)
        self.telNo_entry.grid(row=5, column=1, padx=10)
        # -------------------------------------------------#
        self.submitbtn1 = Button(self.sub_inn_frame1, text='Submit', font=('arial', 10, 'bold'),
                                 width=10, command=self.submit).grid(column=0, sticky=SW, pady=170, row=6)
        self.submitbtn2 = Button(self.sub_inn_frame1, text='Reset', font=('arial', 10, 'bold'),
                                 width=10, command=self.reset).grid(column=1, sticky=SE, pady=170, row=6)
        # ===================================Function Declaration====================================#

    def submit(self):
        no = self.VrefNo.get()
        fn= self.VfName.get()
        ln = self.VlName.get()
        ad = self.Vaddr.get()
        pc = self.VpCode.get()
        tn = self.VtelNo.get()

        conn = mysql.connector.connect(host="localhost", user="root", passwd="", db="hospital management")
        myCursor = conn.cursor()
        if (no and fn and ln and ad and pc and tn) == "":
            tkinter.messagebox.showerror('error', 'some data missing')
        else:
            myCursor.execute("insert into customer values('%s','%s','%s','%s','%s','%s')"%(no,fn,ln,ad,pc,tn))
            conn.commit()
            self.tv.insert('', tk.END, values=(self.VrefNo.get(), self.VfName.get(), self.VlName.get(),
                                           self.Vaddr.get(),self.VpCode.get(), self.VtelNo.get()))
            tkinter.messagebox.showinfo('success', 'Data added succesfully')
            conn.close()

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
