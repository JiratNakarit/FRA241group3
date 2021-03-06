import Tkinter as tk
import Tkinter
import tkMessageBox
from Tkinter import *

from user_rfid import *

import tkSimpleDialog as simpledialog
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)            #LM293D
GPIO.setup(31, GPIO.OUT)

GPIO.setup(33, GPIO.OUT)            #SN74HC166
GPIO.setup(35, GPIO.OUT)

GPIO.setup(36, GPIO.OUT)            #SN74HC100N
GPIO.setup(38, GPIO.OUT)
A = 5
B = 5
C = 5
I = 0
J = 0
K = 0
>>>>>>> refs/remotes/origin/master

from ChinReceiveDataFromIcTable import *

TITLE1_FONT = ("Helvetica", 40, "bold")
EXPLAND_FONT = ("Helvetica", 14, "bold")
TITLE2_FONT = ("Helvetica", 25, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TYPE_FONT = ("Helvetica", 15, "bold")
font1 = ('Verdana', '10', 'bold')
IC_FONT = BUTTON_FONT

rfid = Read_RFID()

class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        # tkinter method
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(*args, borderwidth=20, bg='Dodger Blue4', **kwargs)
        container.option_add("*background", "Dodger Blue2")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1, minsize=300)
        container.grid_columnconfigure(0, weight=1, minsize=500)
        self.row = len(dataIn.Type_Ic)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Admin, RFID):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        # create variable
        global count
        self.count = []
        for i in range(len(dataIn.Type_Ic)):
            self.count.append(0)

        count = self.count

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def CheckUser(self, row):
        correct, false, No_Type, No_Name = 0, 0, 0, 0

        for j in range(row):
            if quantity[j].get() == str(0):
                No_Name += 1
            if Name_ofIC[j].get() == str("Default"):
                No_Type += 1

        for i in range(row):
            if Name_ofIC[i].get() != str("Default") and quantity[i].get() == str(0):
                tkMessageBox.showwarning("WARNING!", message="How many " + Name_ofIC[i].get() + " do you want?")
                false += 1
            if Name_ofIC[i].get() == str("Default") and quantity[i].get() != str(0):
                tkMessageBox.showwarning("WARNING!", message="What IC of " + str(Type_Ic[i][0]) + " do you want?")
                false += 1
            if Name_ofIC[i].get() != str("Default") and quantity[i].get() != str(0):
                correct += 1
        if No_Type == row and No_Name == row:
            tkMessageBox.showwarning("WARNING!", "Please select at least one")
        elif correct != 0 and false == 0:
            self.show_frame("PageTwo")

    def In(self, num):
        if str(Name_ofIC[num - 1].get()) != "Default":
            data = Database.get_num(str(Name_ofIC[num - 1].get()))  # data[0] = NameofIC data[1] = NumofIc
            if count[num - 1] < data[1]:
                count[num - 1] += 1
                quantity[num - 1].set(count[num - 1])
            else:
                tkMessageBox.showwarning("WARNING!", message=str(Name_ofIC[num - 1].get()) + "Out of stock")
            #print count, Name_ofIC[num - 1].get()
        else:
            tkMessageBox.showwarning("WARNING!", message="Please select IC")

    def De(self, num):
        count[num - 1] -= 1
        if count[num - 1] <= 0:
            count[num - 1] = 0
        quantity[num - 1].set(count[num - 1])
        #print count

    def Show_Product(self):
        self.list_ID = []
        self.list_NUM = []
        answer = tkMessageBox.showinfo("Verify", "Please use your KeyCard")
        uid = rfid.get_uid()

        if rfid.check_on_database(uid):
            uid_fordb = rfid.get_stid(uid)
            stid = Database.get_stid(uid_fordb)

            product = []
            for i in range(self.row):
                product.append(Name_ofIC[i].get())
                product.append(quantity[i].get())
            print product
            for i in range(0, len(product) - 1):
                if product[i] != "Default":
                    if i % 2 == 0:
                        value_idofic = product[i]
                        self.list_ID.append(product[i])
                        value_numofall = product[i + 1]
                        self.list_NUM.append(int(product[i+1]))
                        Database.id_user(value_idofic, value_numofall)
                        Database.Commit()
                        Database.insert_history(stid,value_idofic,value_numofall)
                        Database.Commit()
                        Motor(self.list_ID,self.list_NUM)
                        self.show_frame("StartPage")
        else:
            error = tkMessageBox.showinfo("Card is not correct","Try again!")


            print self.list_ID
            print self.list_NUM

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1startle = tk.Label(self, text="How to use this machine", fg='SystemWindow', font='times 40 underline')
        label_1startle.pack(side="top", fill="x", pady=0)
        label_1st = tk.Label(self,text="\n1.Press "+"I'm accept\n\n"+"2.Finish your order then press "+"Next\n\n"+
                            "3.Check your order, Are they correctly?\n\n"+"4.If they are correct press sure if not "
                            "press not sure\n\n"+"5.Use your student card\n\n"+"6.Wait for your IC and have fun with it\n\n"
                            ,fg='green', font=EXPLAND_FONT)
        label_1st.pack(side="top", fill="x", padx=200)
        button = tk.Button(self, text="I'm accept", bg="OliveDrab2", height=2, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(side=BOTTOM, fill='x')
        admin = tk.Button(self, text="ADMIN", height=2, bg="salmon", font=BUTTON_FONT,
                          command=lambda: controller.show_frame("Admin"))
        admin.place(x=5, y=10)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create variables
        global Name_ofIC, quantity, Type_Ic

        self.Type_Ic = dataIn.Type_Ic
        self.Name_Ic = dataIn.Name_Ic
        self.row = len(dataIn.Type_Ic)
        self.Name_ofIC = []
        self.quantity = []
        self.count = 0
        self.y = 100

        for i in range(self.row):
            var = StringVar()
            var.set(self.Name_Ic[self.count][0])
            self.Name_ofIC.append(var)
            self.count += 1

        for i in range(self.row):
            var = StringVar()
            var.set(0)
            self.quantity.append(var)

        quantity = self.quantity
        Name_ofIC = self.Name_ofIC
        Type_Ic = self.Type_Ic

        # create title
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        label_title = tk.Label(self, text="What do you want", fg='SystemWindow', font='times 35 underline')
        label_title.pack()
        elect_type = tk.Label(self, text="Integrated Circuit(IC)", fg='SystemWindow', font='times 18 underline')
        elect_type.place(x=5, y=55)

        # create ic widget
        for i in range(self.row):
            ic_type1 = tk.Label(self, text=self.Type_Ic[i], fg='SystemWindow', font=IC_FONT)
            ic_type1.place(x=25, y=self.y)

            select = apply(OptionMenu, (self, Name_ofIC[i]) + tuple(self.Name_Ic[i]))
            select.config(bg="pale green")
            select.place(x=150, y=self.y)

            Number = Label(self, textvariable=quantity[i], bg='lavender', font=BUTTON_FONT, relief=RAISED)
            Number.place(height=30, width=70, x=805, y=self.y)

            # B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(i+1))
            # B_plus.place(height=30, width=30, x=700, y=self.y)

            # B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2',  command= lambda :controller.De(i+1))
            # B_minus.place(height=30, width=30, x=550, y=100)
            self.y += 70

        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(1))
        B_plus.place(height=30, width=30, x=885, y=100)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(2))
        B_plus.place(height=30, width=30, x=885, y=170)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(3))
        B_plus.place(height=30, width=30, x=885, y=240)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(4))
        B_plus.place(height=30, width=30, x=885, y=310)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(5))
        B_plus.place(height=30, width=30, x=885, y=380)

        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(1))
        B_minus.place(height=30, width=30, x=765, y=100)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(2))
        B_minus.place(height=30, width=30, x=765, y=170)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(3))
        B_minus.place(height=30, width=30, x=765, y=240)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(4))
        B_minus.place(height=30, width=30, x=765, y=310)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(5))
        B_minus.place(height=30, width=30, x=765, y=380)

        # create changePage widget
        button1 = tk.Button(self, text="Go to the start page", bg="salmon", font=BUTTON_FONT,
                            command=lambda: controller.show_frame("StartPage"))
        button1.place(x=25, y=460)
        button2 = tk.Button(self, text="Next", bg="OliveDrab2", font=BUTTON_FONT,
                            command=lambda: controller.CheckUser(self.row))
        button2.place(x=850, y=460)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create variables
        self.row = len(dataIn.Type_Ic)
        self.y = 100

        # create title
        label_2ndtitle = tk.Label(self, text="This is your order", fg='SystemWindow', font='times 40 underline')
        label_2ndtitle.pack(side="top", fill="x", pady=0)

        # create ic widget
        for i in range(self.row):
            name = Label(self, textvariable=Name_ofIC[i], font=BUTTON_FONT, bg='pale green', relief=RAISED)
            name.place(height=30, width=120, x=85, y=self.y)
            number = Label(self, textvariable=quantity[i], font=BUTTON_FONT, bg='lavender')
            number.place(height=30, width=50, x=355, y=self.y)
            unit = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
            unit.place(height=30, width=55, x=500, y=self.y)
            self.y += 70

        # create changePage widget
        Notsure = tk.Button(self, text="Not sure", bg="salmon", font=BUTTON_FONT,
                            command=lambda: controller.show_frame("PageOne"))
        Notsure.place(x=20, y=460)
        sure = tk.Button(self, text="sure", bg="OliveDrab2", font=BUTTON_FONT, command=lambda :controller.Show_Product())
        sure.place(x=700, y=460)

class Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frame1 = Frame(self)
        self.frame1.pack()
        self.frame2 = Frame(self)
        self.frame2.pack()
        self.frame5 = Frame(self)
        self.frame5.pack()
        self.frame3 = Frame(self)
        self.frame3.pack()
        self.frame4 = Frame(self, pady=10)
        self.frame4.pack()
        self.textEntryVar = StringVar()
        self.textEntryVar2 = StringVar()
        self.textEntryVar3 = StringVar()

        Label(self.frame2, text=" Admin", fg='red', font='times 35 ', height=3).pack()
        Label(self.frame2, text='Type: ', font=font1, width=8).pack(side=LEFT)
        self.type = Entry(self.frame2, width=10, font=font1,textvariable=self.textEntryVar)
        self.type.config(bg='lavender')
        self.type.pack(side=LEFT)
        self.type.bind('<FocusIn>',self.numpadEntry1)

        Label(self.frame5, text='Name IC: ', font=font1, width=8).pack(side=LEFT)
        self.name = Entry(self.frame5, width=10, font=font1,textvariable=self.textEntryVar2)
        self.name.config(bg='lavender')
        self.name.pack(side=LEFT)
        self.name.bind('<FocusIn>',self.numpadEntry2)

        Label(self.frame3, text='Integer: ', font=font1, width=8).pack(side=LEFT)
        self.Integer = Entry(self.frame3, width=10, font=font1,textvariable=self.textEntryVar3)
        self.Integer.config(bg='lavender')
        self.Integer.pack(side=LEFT)
        self.Integer.bind('<FocusIn>',self.numpadEntry3)

        self.Enter = Button(self, font=BUTTON_FONT, text='Enter', bg='OliveDrab2', height=2, width=10,
                            command=self.checkadmin,
                            relief=RAISED,
                            cursor="plus")
        self.Enter.place(x=850, y=450)
        self.Back = Button(self, font=BUTTON_FONT, height=2, width=10, text='Back', bg='salmon', relief=RAISED,
                           cursor="plus",
                           command=lambda: controller.show_frame("StartPage"))
        self.Back.place(x=20, y=450)
        self.ButtonClear = Button(self.frame4, font=font1, text='Clear your in put', bg='grey20', fg='red2',
                                  relief=RAISED,
                                  cursor="plus", command=self.Clear)
        self.ButtonClear.pack()
        self.msg = Label(self.frame4, font=font1, height=3, text='Your in put...')
        self.msg.pack()

        self.edited = 0
        self.count = 0

    def Clear(self):
        self.name.delete(0, Tkinter.END)
        self.type.delete(0, Tkinter.END)
        self.Integer.delete(0, Tkinter.END)

    def checkadmin(self):
        ans = tkMessageBox.askquestion("Check!", "Are you sure?")
        if ans == "yes":
            uid = rfid.get_uid()

            if rfid.check_role(uid):

                if self.Integer.get().isdigit():
                    self.msg.configure(text=("Added:", self.type.get(), "__", self.name.get(), "__", self.Integer.get()
                                             , "piece"))
                    if self.name.get() in Database.data_ic(Database.cursor, 3):
                        Database.num_admin(self.name.get(), self.Integer.get())
                        Database.Commit()
                    else:
                        x = []
                        x.append(self.type.get())
                        x.append(self.name.get())
                        x.append(int(self.Integer.get()))
                        print x
                        value_type = x[0]
                        value_idofic = x[1]
                        value_numofall = x[2]
                        datasheet = 'Nothing'
                        Database.ic_admin(value_type, value_idofic ,value_numofall,datasheet)
                        Database.Commit()
                else:
                    self.msg.configure(text="Nothing to Add")
            else:
                error = tkMessageBox.showinfo("Card is not correct","Try again!")

        if ans == "no":
            self.msg.configure(text=" ")

    def numpadEntry1(self,event):
        self.edited = 1
        if self.count == 0:
            self.count = 1
            new = numPad(self,self)

    def numpadEntry2(self, event):

        self.edited = 2
        if self.count == 0:
            self.count = 1
            new = numPad(self,self)


    def numpadEntry3(self, event):

        self.edited = 3
        if self.count == 0:
            self.count = 1
            new = numPad(self,self)


class numPad(simpledialog.Dialog):
    def __init__(self,master=None,parent=None):
        self.parent = parent
        self.top = Toplevel(master=master)
        self.top.protocol("WM_DELETE_WINDOW",self.ok)
        self.createWidgets()
    def createWidgets(self):
        btn_list = [
        '1','2', '3', '4', '5', '6', '7', '8', '9', '0', '-','<--',
          'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '(', ')', '|',
         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '_', 'Ent',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'
         ]
        # create and position all buttons with a for-loop
        # r, c used for row, column grid values
        r = 1
        c = 0
        n = 0
        # list(range()) needed for Python3
        btn = []
        for label in btn_list:
            # partial takes care of function and argument
            cmd = lambda x = label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=2, height=1, command=cmd)
            btn.append(cur)
            # position the button
            btn[-1].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c == 12:
                c = 0
                r += 1
    def click(self,label):
        print(label)
        if self.parent.edited == 1:
            if label == 'Backspace':
                currentText = self.parent.textEntryVar.get()
                self.parent.textEntryVar.set(currentText[:-1])
            elif label == 'Enter':
                self.ok()
            else:
                currentText = self.parent.textEntryVar.get()
                self.parent.textEntryVar.set(currentText+label)
                print self.parent.edited
        elif self.parent.edited == 2:
            if label == 'Backspace':
                currentText = self.parent.textEntryVar2.get()
                self.parent.textEntryVar2.set(currentText[:-1])
            elif label == 'Enter':
                self.ok()
            else:
                currentText = self.parent.textEntryVar2.get()
                self.parent.textEntryVar2.set(currentText+label)
                print self.parent.edited
        elif self.parent.edited == 3:
            if label == 'Backspace':
                currentText = self.parent.textEntryVar3.get()
                self.parent.textEntryVar3.set(currentText[:-1])
            elif label == 'Enter':
                self.ok()
            else:
                currentText = self.parent.textEntryVar3.get()
                self.parent.textEntryVar3.set(currentText+label)
                print self.parent.edited

    def ok(self):
        self.parent.count = 0
        self.top.destroy()
        self.top.master.focus()


class RFID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button = tk.Button(self, text=" scan RFID", bg='OliveDrab2', height=2, width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("Admin"))
        button.place(x=600, y=430)
        button = tk.Button(self, text="back", bg='salmon', height=2, width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=20, y=430)



class Motor():
    def __init__(self,list_ID,list_NUM):
        print list_ID
        print list_NUM
        print len(list_ID)
        global A,I,J,K
        global B
        global C

        for i in range(len(list_ID)):
            print list_ID[i]
            if list_ID[i] == 'LM293P':
                print A
                print list_ID[i]
                print list_NUM[i]
                if list_NUM[i] >= 5:
                    list_NUM[i] = 5
                    t1 = (0.31 * list_NUM[i])
                    print t1
                elif list_NUM[i] > A:
                    list_NUM[i] = A
                    t1 = (0.31 * list_NUM[i])
                    print t1
                elif list_NUM[i] < A:
                    t1 = (0.31 * list_NUM[i])
                    print t1
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29, GPIO.HIGH)
                time.sleep(t1)
                GPIO.output(31, GPIO.LOW)
                GPIO.output(29, GPIO.LOW)
                A = A - list_NUM[i]
                print ('Available A: ', A)
                if A <= 0:
                    t1 = (0.31 * 5)
                    GPIO.output(31, GPIO.HIGH)
                    GPIO.output(29, GPIO.LOW)
                    time.sleep(t1)
                    GPIO.output(31, GPIO.LOW)
                    GPIO.output(29, GPIO.LOW)

            elif list_ID[i] == 'SN74HC166':
                print B
                print list_ID[i]
                print list_NUM[i]
                if list_NUM[i] >= 5:
                    list_NUM[i] = 5
                    t2 = (0.41 * list_NUM[i])
                    print t2
                elif list_NUM[i] > B:
                    list_NUM[i] = B
                    t2 = (0.41 * list_NUM[i])
                    print t2
                elif list_NUM[i] < B:
                    t2 = (0.41 * list_NUM[i])
                    print t2
                GPIO.output(35, GPIO.LOW)
                GPIO.output(33, GPIO.HIGH)
                time.sleep(t2)
                GPIO.output(35, GPIO.LOW)
                GPIO.output(33, GPIO.LOW)
                B = B - list_NUM[i]
                print ('Available B: ', B)
                if B <= 0:
                    t1 = (0.36 * 5)
                    GPIO.output(35, GPIO.HIGH)
                    GPIO.output(33, GPIO.LOW)
                    time.sleep(t2)
                    GPIO.output(35, GPIO.LOW)
                    GPIO.output(33, GPIO.LOW)

            elif list_ID[i] == 'SN74HC100N':
                print C
                print list_ID[i]
                print list_NUM[i]
                if list_NUM[i] >= 5:
                    list_NUM[i] = 5
                    t3 = (0.31 * list_NUM[i])
                    print t3
                elif list_NUM[i] > C:
                    list_NUM[i] = C
                    t3 = (0.31 * list_NUM[i])
                    print t3
                elif list_NUM[i] < C:
                    t3 = (0.31 * list_NUM[i])
                    print t3
                GPIO.output(38, GPIO.LOW)
                GPIO.output(36, GPIO.HIGH)
                time.sleep(t3)
                GPIO.output(38, GPIO.LOW)
                GPIO.output(36, GPIO.LOW)
                C = C - list_NUM[i]
                print ('Available C: ', C)
                if C <= 0:
                    t1 = (0.305 * 5)
                    GPIO.output(38, GPIO.HIGH)
                    GPIO.output(36, GPIO.LOW)
                    time.sleep(t1)
                    GPIO.output(38, GPIO.LOW)
                    GPIO.output(36, GPIO.LOW)


'''def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = UserInterface(root)
    app.mainloop()'''

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
