from tkinter import *
import tkinter.messagebox

class window2:
    def __init__(self, master2):
        self.master2 = master2
        self.master2.title('Patient Registration Page')
        self.master2.geometry('1050x700+200+0')
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
        self.p_login_frame2 = Frame(self.p_frame, width=1000, height=500, bd=8, relief='ridge')
        self.p_login_frame2.grid(row=1, column=0)
                    #-------------inner frame-----------#
        self.inner1_frame2 = LabelFrame(self.p_login_frame2, width=300, height=500, bd=5)
        self.inner1_frame2.grid(row=0, column=0)
        self.inner2_frame2 = Frame(self.p_login_frame2, width=700, height=500, bd=5)
        self.inner2_frame2.grid(row=0, column=1)
                                 #-------------sub_inner1 frame---------#
        self.sub_inn_frame1 = LabelFrame(self.inner1_frame2, text='Customer Name', width=300, height=500, bd=8, relief='ridge')
        self.sub_inn_frame1.grid()
        self.sub_inn_frame1.grid_propagate(0)
                                # -------------sub_inner2 frame---------#
        self.sub_inn_frame2 = LabelFrame(self.inner2_frame2, width=700, height=500, bd=8, text='Information')
        self.sub_inn_frame2.grid()
        self.sub_inn_frame2.grid_propagate(0)
        # =======================================================================================#

        #sub inner frame datails
        self.display_details = Label(self.sub_inn_frame2, font=('arial','9','bold'),
                                     text='Reference No.\t First Name\t Surname\t\t Address\t\t Telephone No \t Post Code')
        self.display_details.grid( pady=10, padx=15, columnspan=4)

        self.textReceipt = Text(self.sub_inn_frame2, font=('arial','9',''), width=97, height=25, bg='white', state='disabled')
        self.textReceipt.grid(row=1, column=0, columnspan=4)
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
        self.submitbtn2 = Button(self.sub_inn_frame1, text='Reset', state = 'disabled',font=('arial', 10, 'bold'),
                                 width=10).grid(column=1,sticky=SE,pady=170,row=6)

        #===================================Function Declaration====================================#

    def submit(self):
        self.textReceipt.config(state='normal')
        self.textReceipt.insert(END, "\t" + self.VrefNo.get())
        self.textReceipt.config(state='disabled')
        self.textReceipt.bind("<Button>", lambda event: self.textReceipt.focus_set())





root = Tk()
window2(root)
root.mainloop()