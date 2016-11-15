from Tkinter import *
import tkMessageBox
import Tkinter as tk
import Tkinter
import tkMessageBox
#from Class import *

TITLE1_FONT = ("Helvetica", 40, "bold")
EXPLAND_FONT = ("Helvetica", 10, "bold")
TITLE2_FONT = ("Helvetica", 25, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TYPE_FONT = ("Helvetica", 15, "bold")
font1 = ('Verdana', '10', 'bold')
IC_FONT = BUTTON_FONT
Item_type = [["Default", "741G374", "74HC74"], ["Default", "DM7473", "DM7476"], ["Default", "74HC08", "DM7411"],
             ["Default", "74LS10", "74LS13"], ["Default", "DM74LS32", "741G32"]]

#Sorawis code(Arm)
#variable1 - data in list of D_TYPE = ["Default", "741G374", "74HC74"]
#variable2 - data in list of JK_TYPE = ["Default", "DM7473", "DM7476"]
#variable3 - data in list of AND_GATE = ["Default", "74HC08", "DM7411"]
#variable4 - data in list of NAND_GATE = ["Default", "74LS10", "74LS13"]
#variable5 - data in list of OR_GATE = ["Default", "DM74LS32", "741G32"]
#var1 , var6 - number of D-Type IC
#var2 , var7 - number of JK-Type IC
#var3 , var8 - number of AND_GATE IC
#var4 , var9 - number of OR_GATE IC
#var5 , var10 - number of NAND_GATE IC
#you can use .get() to see data of variable

class UserInterface(tk.Tk):
    global count
    count = [0,0,0,0,0]
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(*args, borderwidth=20, bg='Dodger Blue4', **kwargs)
        container.option_add("*background", "Dodger Blue2")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1, minsize=300)
        container.grid_columnconfigure(0, weight=1, minsize=500)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Admin,RFID):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def CheckUser(self):
        global state
        global error
        error = 0
        if var1.get() == str(0) and var2.get() == str(0) and var3.get() == str(0) and var4.get() == str(0) and var5.get()\
                == str(0) and variable1.get() == str("Default") and variable2.get() == str("Default") and variable3.get() \
                == str("Default") and variable4.get() == str("Default") and variable5.get() == str("Default"):
            tkMessageBox.showwarning("WARNING!", "Please select at least one")
            error += 1
        if variable1.get() != str("Default") and var1.get() == str(0):
            tkMessageBox.showwarning("WARNING!", message="How many "+variable1.get()+" do you want?")
            error += 1
        if variable2.get() != str("Default") and var2.get() == str(0):
            tkMessageBox.showwarning("WARNING!", message="How many "+variable2.get()+" do you want?")
            error += 1
        if variable3.get() != str("Default") and var3.get() == str(0):
            tkMessageBox.showwarning("WARNING!", message="How many "+variable3.get()+" do you want?")
            error += 1
        if variable4.get() != str("Default") and var4.get() == str(0):
            tkMessageBox.showwarning("WARNING!", message="How many "+variable4.get()+" do you want?")
            error += 1
        if variable5.get() != str("Default") and var5.get() == str(0):
            tkMessageBox.showwarning("WARNING!", message="How many "+variable5.get()+" do you want?")
            error += 1
        if variable1.get() == str("Default") and var1.get() != str(0):
            tkMessageBox.showwarning("WARNING!", message="What IC of D-Type do you want?")
            error += 1
        if variable2.get() == str("Default") and var2.get() != str(0):
            tkMessageBox.showwarning("WARNING!", message="What IC of JK-Type do you want?")
            error += 1
        if variable3.get() == str("Default") and var3.get() != str(0):
            tkMessageBox.showwarning("WARNING!", message="What IC of AND-GATE do you want?")
            error += 1
        if variable4.get() == str("Default") and var4.get() != str(0):
            tkMessageBox.showwarning("WARNING!", message="What IC of OR-GATE do you want?")
            error += 1
        if variable5.get() == str("Default") and var5.get() != str(0):
            tkMessageBox.showwarning("WARNING!", message="What IC NAND-GATE do you want?")
            error += 1
        if ((variable1.get() != str("Default") and var1.get() != str(0)) or (variable2.get() != str("Default") and \
            var2.get() != str(0)) or (variable3.get() != str("Default") and var3.get() != str(0)) or (variable4.get() \
            != str("Default") and var4.get() != str(0)) or (variable5.get() != str("Default") and var5.get() != str(0)))\
            and (error == 0):
            self.verify()

    def verify(self):
        x = tkMessageBox.askquestion("Are you sure","Do you want to go to verify page?")
        if x == "yes":
            self.show_frame("PageTwo")

    def In(self, num):
        count[num - 1] += 1
        if (num == 1):
            var1.set(count[num - 1])
        elif (num == 2):
            var2.set(count[num - 1])
        elif (num == 3):
            var3.set(count[num - 1])
        elif (num == 4):
            var4.set(count[num - 1])
        elif (num == 5):
            var5.set(count[num - 1])
        print count

    def De(self, num):
        count[num - 1] -= 1
        if count[num - 1] <= 0:
            count[num - 1] = 0
        if (num == 1):
            var1.set(count[num - 1])
        elif (num == 2):
            var2.set(count[num - 1])
        elif (num == 3):
            var3.set(count[num - 1])
        elif (num == 4):
            var4.set(count[num - 1])
        elif (num == 5):
            var5.set(count[num - 1])
        print count

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1sttitle = tk.Label(self, text="How to use this machine", fg='SystemWindow', font='times 40 underline')
        label_1sttitle.pack(side="top", fill="x", pady=0)
        label_1st = tk.Label(self,
                             text="\n\nThe first step of using vending machines, electronic devices allow users to select \n "
                                  "the type and number of devices such as the amount you want by pressing the + sign \n "
                                  "to add the device to one of the press - to decrease the device that one. the user \n "
                                  "choose the number is unlimited, but the producers enlisted to choose what's right \n "
                                  "for the part of saving resources are limited and we have the Data Sheet of each \n "
                                  "componentin the form of. QR CODE you can check that the device is made, and some \n "
                                  "are unique,however.from this machine \n\n"
                                  "The second step when the user selects completed successfully,the user presses the OK \n "
                                  "button at the lower right corner one time, the system will display a list of devices \n "
                                  "and users have ordered earlier if the users. the type and number of devices you have \n "
                                  "to go on our website and will automatically supply the user has been ordered out of \n "
                                  "the area in front of the machine. And in addition, the manufacturer has a zipper storage \n "
                                  "bag to prevent damage of electronic devices as well. Welcome to the user when the user \n "
                                  "does not have to be finished off.\n\n"
                                  "Finally If the user wants to check your history. You can also check that each device \n "
                                  "inside the electronics remaining amount.\n\n\n\n"
                             , fg='SystemWindow', font=EXPLAND_FONT)
        label_1st.pack(side="top", fill="x", padx=100)
        button = tk.Button(self, text="I'm accept",bg="OliveDrab2", height=2, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(side=BOTTOM, fill='x')
        admin = tk.Button(self, text="ADMIN", height=2, bg="salmon", font=BUTTON_FONT,command=lambda :controller.show_frame("RFID"))
        admin.place(x=5,y=10)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        self.height = 5
        tk.Frame.__init__(self, parent)
        self.controller = controller
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        label_title = tk.Label(self, text="What do you want",fg='SystemWindow', font='times 35 underline')
        label_title.pack()
        elec_type = tk.Label(self, text="Integrated Circuit(IC)", fg='SystemWindow', font='times 18 underline')
        elec_type.place(x=5, y=55)
        ic_type1 = tk.Label(self, text="D - Type", fg='SystemWindow', font=IC_FONT)
        ic_type1.place(x=25, y=100)
        ic_type2 = tk.Label(self, text="JK - Type",  fg='SystemWindow', font=IC_FONT)
        ic_type2.place(x=25, y=170)
        ic_type3 = tk.Label(self, text="AND - GATE",  fg='SystemWindow', font=IC_FONT)
        ic_type3.place(x=25, y=240)
        ic_type4 = tk.Label(self, text="OR - GATE",  fg='SystemWindow', font=IC_FONT)
        ic_type4.place(x=25, y=310)
        ic_type5 = tk.Label(self, text="NAND - GATE",  fg='SystemWindow', font=IC_FONT)
        ic_type5.place(x=25, y=380)

        self.variables = []
        self.nup = 0
        for i in range(self.height):
            var = StringVar()
            var.set(Item_type[self.nup][0])
            self.variables.append(var)
            self.nup += 1

        global variable1, variable2, variable3, variable4, variable5
        variable1 = self.variables[0]
        variable2 = self.variables[1]
        variable3 = self.variables[2]
        variable4 = self.variables[3]
        variable5 = self.variables[4]


        select1 = apply(OptionMenu, (self, variable1) + tuple(Item_type[0]))
        select1.config(bg = "pale green")
        select1.place(x=150, y=98)
        select2 = apply(OptionMenu, (self, variable2) + tuple(Item_type[1]))
        select2.config(bg = "gold")
        select2.place(x=150, y=168)
        select3 = apply(OptionMenu, (self, variable3) + tuple(Item_type[2]))
        select3.config(bg = "maroon4")
        select3.place(x=150, y=238)
        select4 = apply(OptionMenu, (self, variable4) + tuple(Item_type[3]))
        select4.config(bg = "orange red")
        select4.place(x=150, y=308)
        select5 = apply(OptionMenu, (self, variable5) + tuple(Item_type[4]))
        select5.config(bg = "grey20")
        select5.place(x=150, y=378)

        self.vars = []
        for i in range(self.height):
            var = StringVar()
            var.set(0)
            self.vars.append(var)

        global var1, var2, var3, var4, var5
        var1 = self.vars[0]
        var2 = self.vars[1]
        var3 = self.vars[2]
        var4 = self.vars[3]
        var5 = self.vars[4]

        b1 = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(1))
        b1.place(height=30, width=30, x=700, y=100)

        label1 = Label(self, textvariable=var1, bg='lavender', font=BUTTON_FONT, relief=RAISED)
        label1.place(height=30, width=70, x=605, y=100)

        b2 = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2',  command= lambda :controller.De(1))
        b2.place(height=30, width=30, x=550, y=100)

        b3 = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(2))
        b3.place(height=30, width=30, x=700, y=170)

        label2 = Label(self, textvariable=var2, bg='lavender', font=BUTTON_FONT, relief=RAISED)
        label2.place(height=30, width=70, x=605, y=170)

        b4 = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command= lambda :controller.De(2))
        b4.place(height=30, width=30, x=550, y=170)

        b5 = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(3))
        b5.place(height=30, width=30, x=700, y=240)

        label3 = Label(self, textvariable=var3, bg='lavender', font=BUTTON_FONT, relief=RAISED)
        label3.place(height=30, width=70, x=605, y=240)

        b6 = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command= lambda :controller.De(3))
        b6.place(height=30, width=30, x=550, y=240)

        b7 = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(4))
        b7.place(height=30, width=30, x=700, y=310)

        label4 = Label(self, textvariable=var4, bg='lavender', font=BUTTON_FONT, relief=RAISED)
        label4.place(height=30, width=70, x=605, y=310)

        b8 = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command= lambda :controller.De(4))
        b8.place(height=30, width=30, x=550, y=310)

        b9 = Button(self, text="+", font=BUTTON_FONT, bg='grey20', fg='red2', command= lambda :controller.In(5))
        b9.place(height=30, width=30, x=700, y=380)

        label5 = Label(self, textvariable=var5, bg='lavender', font=BUTTON_FONT, relief=RAISED)
        label5.place(height=30, width=70, x=605, y=380)

        b10 = Button(self, text="-", font=BUTTON_FONT, bg='grey20', fg='green2', command= lambda :controller.De(5))
        b10.place(height=30, width=30, x=550, y=380)

        button1 = tk.Button(self, text="Go to the start page", bg="salmon", font=BUTTON_FONT,
                            command=lambda: controller.show_frame("StartPage"))
        button1.place(x=20, y=460)
        button2 = tk.Button(self, text="Next", bg="OliveDrab2", font=BUTTON_FONT, command=lambda: controller.CheckUser())
        button2.place(x=700, y=460)





class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_2ndtitle = tk.Label(self, text="This is your order", fg='SystemWindow', font='times 40 underline')
        label_2ndtitle.pack(side="top", fill="x", pady=0)

        name1 = Label(self, textvariable=variable1, font=BUTTON_FONT, bg='pale green', relief=RAISED)
        name1.place(height=30, width=70, x=85, y=100)
        number1 = Label(self, textvariable=var1, font=BUTTON_FONT, bg='lavender', relief=RAISED)
        number1.place(height=30, width=70, x=355, y=100)
        unit1 = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
        unit1.place(height=30, width=70, x=625, y=100)
        name2 = Label(self, textvariable=variable2, font=BUTTON_FONT, bg='gold', relief=RAISED)
        name2.place(height=30, width=70, x=85, y=170)
        number2 = Label(self, textvariable=var2, font=BUTTON_FONT, bg='lavender', relief=RAISED)
        number2.place(height=30, width=70, x=355, y=170)
        unit2 = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
        unit2.place(height=30, width=70, x=625, y=170)
        name3 = Label(self, textvariable=variable3, font=BUTTON_FONT, bg='maroon4', relief=RAISED)
        name3.place(height=30, width=70, x=85, y=240)
        number3 = Label(self, textvariable=var3, font=BUTTON_FONT, bg='lavender', relief=RAISED)
        number3.place(height=30, width=70, x=355, y=240)
        unit3 = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
        unit3.place(height=30, width=70, x=625, y=240)
        name4 = Label(self, textvariable=variable4, font=BUTTON_FONT, bg='orange red', relief=RAISED)
        name4.place(height=30, width=70, x=85, y=310)
        number4 = Label(self, textvariable=var4, font=BUTTON_FONT, bg='lavender', relief=RAISED)
        number4.place(height=30, width=70, x=355, y=310)
        unit4 = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
        unit4.place(height=30, width=70, x=625, y=310)
        name5 = Label(self, textvariable=variable5, font=BUTTON_FONT, bg='grey20', relief=RAISED)
        name5.place(height=30, width=70, x=85, y=380)
        number5 = Label(self, textvariable=var5, font=BUTTON_FONT, bg='lavender', relief=RAISED)
        number5.place(height=30, width=70, x=355, y=380)
        unit5 = Label(self, text="piece", font=BUTTON_FONT, bg='lavender', relief=RAISED)
        unit5.place(height=30, width=70, x=625, y=380)
        notsure = tk.Button(self, text="Not sure", bg="salmon", font=BUTTON_FONT, command=lambda: controller.show_frame("PageOne"))
        notsure.place(x=20, y=460)
        sure = tk.Button(self, text="sure", bg="OliveDrab2", font=BUTTON_FONT, command=self.Show_Product)
        sure.place(x=700, y=460)

    def Show_Product(self):
        answer = tkMessageBox.askquestion("Verify","Please use your keycard")
        if answer == "yes":
            product=[]
            product.append(variable1.get())
            product.append(var1.get())
            product.append(variable2.get())
            product.append(var2.get())
            product.append(variable3.get())
            product.append(var3.get())
            product.append(variable4.get())
            product.append(var4.get())
            product.append(variable5.get())
            product.append(var5.get())
            print product


#Worawit Code(Bank)
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
        self.Enter = Button(self, font=BUTTON_FONT, text='Enter', bg='OliveDrab2', height=2, width=10, command=self.checkadmin,
                            relief=RAISED,
                            cursor="plus")
        self.Enter.place(x=645, y=450)
        self.Back = Button(self, font=BUTTON_FONT, height=2, width=10, text='Back', bg='salmon', relief=RAISED, cursor="plus",
                           command=lambda: controller.show_frame("StartPage"))
        self.Back.place(x=20, y=450)
        self.ButtonClear = Button(self.frame4, font=font1, text='Clear your in put', bg='grey20', fg='red2', relief=RAISED,
                                  cursor="plus", command=self.Clear)
        self.ButtonClear.pack()
        self.msg = Label(self.frame4, font=font1,  height=3, text='Your in put...')
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
                value_name = x[1]
                value_numall = x[2]

                Database.ic(value_type, value_name)
                Database.Commit()
                Database.machine_user(value_numall)
                Database.Commit()
             else:
                self.msg.configure(text="Nothing to Add")

        if ans == "no":
            self.msg.configure(text=" ")


class RFID(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button = tk.Button(self, text=" scan RFID", bg='OliveDrab2', height=2,width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("Admin"))
        button.place(x=600,y=430)
        button = tk.Button(self, text="back", bg='salmon', height=2, width=15, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=20,y=430)

'''def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = UserInterface(root)
    app.mainloop()'''

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()



