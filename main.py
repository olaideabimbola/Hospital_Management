from tkinter import *
import tkinter.messagebox
import random
import time
import datetime

class window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('800x750+0+0')
        self.frame = Frame(self.master)
        self.frame.grid()
        self.master.resizable(False, True)

        self.label_title = Label(self.frame, text = 'Pharmacy Management System', font=('arial',30,'bold'), bd=20)
        self.label_title.grid(row=0, column=0, columnspan=2, pady=40)
        self.login_frame1 = Frame(self.frame, width=1000, height=300, bd=20, relief='ridge')
        self.login_frame1.grid(row=1, column=0,pady=3)
        self.login_frame2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.login_frame2.grid(row=2, column=0)
        self.login_frame3 = Frame(self.frame, width=1000, height=200, bd=20, relief='ridge')
        self.login_frame3.grid(row=3, column=0, pady=4)

        #=====================================================================================================#
        self.username = StringVar()
        self.password = StringVar()

        self.lb_username = Label(self.login_frame1, text='Username', font=('arial', 11, 'bold'), bd=20)
        self.lb_username.grid(row=0, column=0)
        self.txt_username = Entry(self.login_frame1, text='Username', width=20, font=('arial', 13, 'bold'), textvariable = self.username)
        self.txt_username.grid(row=0, column=1)
        self.lb_password = Label(self.login_frame1, text='Password', font=('arial', 11, 'bold'), bd=20)
        self.lb_password.grid(row=1, column=0)
        self.txt_Password = Entry(self.login_frame1, text='Password', width=20, font=('arial', 13, 'bold'), textvariable = self.password)
        self.txt_Password.grid(row=1, column=1)
        # =====================================================================================================#

        self.login_btn = Button(self.login_frame2, text='Login',width=20,font=('arial',13,'bold'),command=self.login)
        self.login_btn.grid(row=0, column=0)
        self.reset_btn = Button(self.login_frame2, text='Reset',width=20,font=('arial',13,'bold'),command=self.reset)
        self.reset_btn.grid(row=0, column=1)
        self.exit_btn = Button(self.login_frame2, text='Exit',width=20,font=('arial',13,'bold'),command=self.exitt)
        self.exit_btn.grid(row=0, column=2)


        self.registration_btn = Button(self.login_frame3,width=20,text = 'Hospital Management', state = DISABLED, font=('arial',10,'bold'),command = self.Registration_window)
        self.registration_btn.grid(row=0, column=0)
        self.pharmacy_btn = Button(self.login_frame3, width=20,text = 'Patient Registration', state = DISABLED, font=('arial',10,'bold'),command = self.Pharmacy_window)
        self.pharmacy_btn.grid(row=0, column=1)

        # =====================================================================================================#
    def login(self):
        user = (self.username.get())
        pas = (self.password.get())
        if (user == str('olaide')) and (pas == str(1234)):
            self.registration_btn.config(state = NORMAL)
            self.pharmacy_btn.config(state = NORMAL)
        else:
            tkinter.messagebox.showerror('Login Page', 'Invalid login, try again')
            self.registration_btn.config(state = DISABLED)
            self.pharmacy_btn.config(state = DISABLED)
            self.username.set("")
            self.password.set("")
            self.txt_username.focus()

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

class window3:
    def __init__(self, master):
        self.master = master
        self.master.title('Pharmacy System')
        self.master.geometry('1000x750')
        self.frame = Frame(self.master)
        self.frame.pack()

root = Tk()
window1(root)
root.mainloop()
