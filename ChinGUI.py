import Tkinter as tk
import Tkinter
import tkMessageBox
from Tkinter import *

from ChinReceiveDataFromIcTable import *

TITLE1_FONT = ("Helvetica", 40, "bold")
EXPLAND_FONT = ("Helvetica", 10, "bold")
TITLE2_FONT = ("Helvetica", 25, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TYPE_FONT = ("Helvetica", 15, "bold")
font1 = ('Verdana', '10', 'bold')
IC_FONT = BUTTON_FONT


class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        # tkinter method
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(*args, borderwidth=20, bg='Dodger Blue4', **kwargs)
        container.option_add("*background", "Dodger Blue2")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1, minsize=300)
        container.grid_columnconfigure(0, weight=1, minsize=500)

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
        if No_Type == 5 and No_Name == 5:
            tkMessageBox.showwarning("WARNING!", "Please select at least one")
        elif correct != 0 and false == 0:
            self.show_frame("PageTwo")

    def In(self, num):
        data = Database.get_num(str(Name_ofIC[num - 1].get()))  # data[0] = NameofIC data[1] = NumofIc
        if count[num - 1] < data[1]:
            count[num - 1] += 1
            quantity[num - 1].set(count[num - 1])
        else:
            tkMessageBox.showwarning("WARNING!", message=str(Name_ofIC[num - 1].get())+"Out of stock")
        print count,Name_ofIC[num - 1].get()

    def De(self, num):
        count[num - 1] -= 1
        if count[num - 1] <= 0:
            count[num - 1] = 0
        quantity[num - 1].set(count[num - 1])
        print count


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1startle = tk.Label(self, text="How to use this machine", fg='SystemWindow', font='times 40 underline')
        label_1startle.pack(side="top", fill="x", pady=0)
        label_1st = tk.Label(self,
                             text="\n\n\n\nThe first step of using vending machines, electronic devices allow users to select \n "
                                  "the type and number of devices such as the amount you want by pressing the + sign \n "
                                  "to add the device to one of the press - to decrease the device that one. the user \n "
                                  "choose the number is unlimited, but the producers enlisted to choose what's right \n "
                                  "for the part of saving resources are limited.\n\n\n"
                                  "The second step when the user selects completed successfully,the user presses the OK \n "
                                  "button at the lower right corner one time, the system will display a list of order's devices. \n "
                                  "Then recheck your devices if you already check ,So press the sure button and then scan your \n"
                                  "KeyCard for receive your order. And the system will automatically save your history into server.\n\n\n"
                                  "Finally If the user wants to check your history,you can check it in system website.\n"
                                  "And you can also check that each device inside the electronics remaining amount.\n\n"
                                  "-----------------------------------------------------------------------------------------------\n"
                                  "The system website : http://hello world.com\n\n\n"
                             , fg='SystemWindow', font=EXPLAND_FONT)
        label_1st.pack(side="top", fill="x", padx=100)
        button = tk.Button(self, text="I'm accept", bg="OliveDrab2", height=2, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(side=BOTTOM, fill='x')
        admin = tk.Button(self, text="ADMIN", height=2, bg="salmon", font=BUTTON_FONT,
                          command=lambda: controller.show_frame("RFID"))
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
            Number.place(height=30, width=70, x=605, y=self.y)

            # B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(i+1))
            # B_plus.place(height=30, width=30, x=700, y=self.y)

            # B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2',  command= lambda :controller.De(i+1))
            # B_minus.place(height=30, width=30, x=550, y=100)
            self.y += 70

        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(1))
        B_plus.place(height=30, width=30, x=700, y=100)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(2))
        B_plus.place(height=30, width=30, x=700, y=170)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(3))
        B_plus.place(height=30, width=30, x=700, y=240)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(4))
        B_plus.place(height=30, width=30, x=700, y=310)
        B_plus = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command=lambda: controller.In(5))
        B_plus.place(height=30, width=30, x=700, y=380)

        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(1))
        B_minus.place(height=30, width=30, x=550, y=100)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(2))
        B_minus.place(height=30, width=30, x=550, y=170)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(3))
        B_minus.place(height=30, width=30, x=550, y=240)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(4))
        B_minus.place(height=30, width=30, x=550, y=310)
        B_minus = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command=lambda: controller.De(5))
        B_minus.place(height=30, width=30, x=550, y=380)

        # create changePage widget
        button1 = tk.Button(self, text="Go to the start page", bg="salmon", font=BUTTON_FONT,
                            command=lambda: controller.show_frame("StartPage"))
        button1.place(x=20, y=460)
        button2 = tk.Button(self, text="Next", bg="OliveDrab2", font=BUTTON_FONT,
                            command=lambda: controller.CheckUser(self.row))
        button2.place(x=700, y=460)


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
        sure = tk.Button(self, text="sure", bg="OliveDrab2", font=BUTTON_FONT, command=self.Show_Product)
        sure.place(x=700, y=460)

    def Show_Product(self):
        answer = tkMessageBox.askquestion("Verify", "Please use your KeyCard")
        if answer == "yes":
            product = []
            for i in range(self.row):
                product.append(Name_ofIC[i].get())
                product.append(quantity[i].get())
            print product
            for i in range(0, len(product) - 1):
                if product[i] != "Default":
                    if i % 2 == 0:
                        value_idofic = product[i]
                        value_numofall = product[i + 1]
                        Database.id_user(value_idofic, value_numofall)
                        Database.Commit()
                        print product[i], product[i + 1]
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

        Label(self.frame2, text=" Admin", fg='red', font='times 35 ', height=3).pack()
        Label(self.frame2, text='Type: ', font=font1, width=8).pack(side=LEFT)
        self.type = Entry(self.frame2, width=10, font=font1)
        self.type.focus_force()
        self.type.config(bg='lavender')
        self.type.pack(side=LEFT)
        Label(self.frame5, text='Name IC: ', font=font1, width=8).pack(side=LEFT)
        self.name = Entry(self.frame5, width=10, font=font1)
        self.name.focus_force()
        self.name.config(bg='lavender')
        self.name.pack(side=LEFT)
        Label(self.frame3, text='Integer: ', font=font1, width=8).pack(side=LEFT)
        self.Integer = Entry(self.frame3, width=10, font=font1)
        self.Integer.config(bg='lavender')
        self.Integer.pack(side=LEFT)
        self.Enter = Button(self, font=BUTTON_FONT, text='Enter', bg='OliveDrab2', height=2, width=10,
                            command=self.checkadmin,
                            relief=RAISED,
                            cursor="plus")
        self.Enter.place(x=645, y=450)
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

    def Clear(self):
        self.name.delete(0, Tkinter.END)
        self.type.delete(0, Tkinter.END)
        self.Integer.delete(0, Tkinter.END)

    def checkadmin(self):
        ans = tkMessageBox.askquestion("Check!", "Are you sure?")
        if ans == "yes":
            if self.Integer.get().isdigit():
                self.msg.configure(text=("Added:", self.type.get(), "__", self.name.get(), "__", self.Integer.get()
                                         , "piece"))
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

        if ans == "no":
            self.msg.configure(text=" ")


class RFID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button = tk.Button(self, text=" scan RFID", bg='OliveDrab2', height=2, width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("Admin"))
        button.place(x=600, y=430)
        button = tk.Button(self, text="back", bg='salmon', height=2, width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=20, y=430)


'''def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = UserInterface(root)
    app.mainloop()'''

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
