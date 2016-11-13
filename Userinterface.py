import Tkinter as tk
from Tkinter import *
import tkMessageBox

TITLE1_FONT = ("Helvetica", 40, "bold")
EXPLAND_FONT = ("Helvetica", 10, "bold")
TITLE2_FONT = ("Helvetica", 25, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TYPE_FONT = ("Helvetica", 15, "bold")
font1 = ('Verdana', '10', 'bold')
IC_FONT = BUTTON_FONT
D_TYPE = ["Default", "741G374", "74HC74"]
JK_TYPE = ["Default", "DM7473", "DM7476"]
AND_GATE = ["Default", "74HC08", "DM7411"]
NAND_GATE = ["Default", "74LS10", "74LS13"]
OR_GATE = ["Default", "DM74LS32", "741G32"]

#Sorawis code(Arm)

class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(*args, borderwidth=20, bg='orange', **kwargs)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1, minsize=300)
        container.grid_columnconfigure(0, weight=1, minsize=500)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Admin):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''for frame in self.frames.values():
            frame.grid_remove()'''

        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1sttitle = tk.Label(self, text="How to use this machine", font=TITLE1_FONT)
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
                             , font=EXPLAND_FONT)
        label_1st.pack(side="top", fill="x", padx=100)
        button = tk.Button(self, text="I'm accept", height=2, font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(side=BOTTOM, fill='x')
        admin = tk.Button(self, text="ADMIN", height=2, font=BUTTON_FONT,command=lambda :controller.show_frame("Admin"))
        admin.place(x=5,y=10)

class PageOne(tk.Frame):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        label_title = tk.Label(self, text="Choose Your Gift!!", font=TITLE2_FONT)
        label_title.pack()
        elec_type = tk.Label(self, text="Integrated Circuit(IC)", font=TYPE_FONT)
        elec_type.place(x=5, y=40)
        ic_type1 = tk.Label(self, text="D - Type", font=IC_FONT)
        ic_type1.place(x=25, y=80)
        ic_type2 = tk.Label(self, text="JK - Type", font=IC_FONT)
        ic_type2.place(x=25, y=150)
        ic_type3 = tk.Label(self, text="AND - GATE", font=IC_FONT)
        ic_type3.place(x=25, y=220)
        ic_type4 = tk.Label(self, text="OR - GATE", font=IC_FONT)
        ic_type4.place(x=25, y=290)
        ic_type5 = tk.Label(self, text="NAND - GATE", font=IC_FONT)
        ic_type5.place(x=25, y=360)

        global variable1
        global variable2
        global variable3
        global variable4
        global variable5

        variable1 = StringVar(self)
        variable1.set(D_TYPE[0])
        variable2 = StringVar(self)
        variable2.set(JK_TYPE[0])
        variable3 = StringVar(self)
        variable3.set(AND_GATE[0])
        variable4 = StringVar(self)
        variable4.set(OR_GATE[0])
        variable5 = StringVar(self)
        variable5.set(NAND_GATE[0])

        select1 = apply(OptionMenu, (self, variable1) + tuple(D_TYPE))
        select1.place(x=140, y=78)
        select1 = apply(OptionMenu, (self, variable2) + tuple(JK_TYPE))
        select1.place(x=140, y=148)
        select1 = apply(OptionMenu, (self, variable3) + tuple(AND_GATE))
        select1.place(x=140, y=218)
        select1 = apply(OptionMenu, (self, variable4) + tuple(OR_GATE))
        select1.place(x=140, y=288)
        select1 = apply(OptionMenu, (self, variable5) + tuple(NAND_GATE))
        select1.place(x=140, y=358)

        global var1
        var1 = StringVar(self)
        var1.set(0)
        global var2
        var2 = StringVar(self)
        var2.set(0)
        global var3
        var3 = StringVar(self)
        var3.set(0)
        global var4
        var4 = StringVar(self)
        var4.set(0)
        global var5
        var5 = StringVar(self)
        var5.set(0)

        b1 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=self.In1)
        b1.place(height=30, width=30, x=700, y=80)

        label1 = Label(self, textvariable=var1, font=BUTTON_FONT, relief=RAISED)
        label1.place(height=30, width=70, x=605, y=80)

        b2 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=self.De1)
        b2.place(height=30, width=30, x=550, y=80)

        b3 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=self.In2)
        b3.place(height=30, width=30, x=700, y=150)

        label2 = Label(self, textvariable=var2, font=BUTTON_FONT, relief=RAISED)
        label2.place(height=30, width=70, x=605, y=150)

        b4 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=self.De2)
        b4.place(height=30, width=30, x=550, y=150)

        b5 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=self.In3)
        b5.place(height=30, width=30, x=700, y=220)

        label3 = Label(self, textvariable=var3, font=BUTTON_FONT, relief=RAISED)
        label3.place(height=30, width=70, x=605, y=220)

        b6 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=self.De3)
        b6.place(height=30, width=30, x=550, y=220)

        b7 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=self.In4)
        b7.place(height=30, width=30, x=700, y=290)

        label4 = Label(self, textvariable=var4, font=BUTTON_FONT, relief=RAISED)
        label4.place(height=30, width=70, x=605, y=290)

        b8 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=self.De4)
        b8.place(height=30, width=30, x=550, y=290)

        b9 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=self.In5)
        b9.place(height=30, width=30, x=700, y=360)

        label5 = Label(self, textvariable=var5, font=BUTTON_FONT, relief=RAISED)
        label5.place(height=30, width=70, x=605, y=360)

        b10 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=self.De5)
        b10.place(height=30, width=30, x=550, y=360)

        button1 = tk.Button(self, text="Go to the start page", font=BUTTON_FONT,
                            command=lambda: controller.show_frame("StartPage"))
        button1.place(x=20, y=460)
        if self.count1 == 0:
            button2 = tk.Button(self, text="Next", font=BUTTON_FONT, command=self.warning)
            button2.place(x=700, y=460)
        button2 = tk.Button(self, text="Next", font=BUTTON_FONT, command=lambda: controller.show_frame("PageTwo"))
        button2.place(x=700, y=460)


    def In1(self):
        global count1
        self.count1 += 1
        var1.set(self.count1)
        var6.set(self.count1)

    def De1(self):
        self.count1 -= 1
        if self.count1 <= 0:
            self.count1 = 0
        var1.set(self.count1)
        var6.set(self.count1)

    def In2(self):
        self.count2 += 1
        var2.set(self.count2)
        var7.set(self.count2)

    def De2(self):
        self.count2 -= 1
        if self.count2 <= 0:
            self.count2 = 0
        var2.set(self.count2)
        var7.set(self.count2)

    def In3(self):
        self.count3 += 1
        var3.set(self.count3)
        var8.set(self.count3)

    def De3(self):
        self.count3 -= 1
        if self.count3 <= 0:
            self.count3 = 0
        var3.set(self.count3)
        var8.set(self.count3)

    def In4(self):
        self.count4 += 1
        var4.set(self.count4)
        var9.set(self.count4)

    def De4(self):
        self.count4 -= 1
        if self.count4 <= 0:
            self.count4 = 0
        var4.set(self.count4)
        var9.set(self.count4)

    def In5(self):
        self.count5 += 1
        var5.set(self.count5)
        var10.set(self.count5)

    def De5(self):
        self.count5 -= 1
        if self.count5 <= 0:
            self.count5 = 0
        var5.set(self.count5)
        var10.set(self.count5)

    def warning(self):
        tkMessageBox.showwarning("WARNING!!", "Please select at least one piece")


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        notsure = tk.Button(self, text="Not sure", font=BUTTON_FONT, command=lambda: controller.show_frame("PageOne"))
        notsure.place(x=20, y=460)
        sure = tk.Button(self, text="sure", font=BUTTON_FONT, command=lambda: controller.show_frame("PageOne"))
        sure.place(x=700, y=460)
        global var6
        var6 = StringVar(self)
        var6.set(0)
        global var7
        var7 = StringVar(self)
        var7.set(0)
        global var8
        var8 = StringVar(self)
        var8.set(0)
        global var9
        var9 = StringVar(self)
        var9.set(0)
        global var10
        var10 = StringVar(self)
        var10.set(0)


        label1 = Label(self, textvariable=variable1, font=BUTTON_FONT, relief=RAISED)
        label1.place(height=30, width=70, x=100, y=80)
        label2 = Label(self, textvariable=variable2, font=BUTTON_FONT, relief=RAISED)
        label2.place(height=30, width=70, x=100, y=150)
        label3 = Label(self, textvariable=variable3, font=BUTTON_FONT, relief=RAISED)
        label3.place(height=30, width=70, x=100, y=220)
        label4 = Label(self, textvariable=variable4, font=BUTTON_FONT, relief=RAISED)
        label4.place(height=30, width=70, x=100, y=290)
        label5 = Label(self, textvariable=variable5, font=BUTTON_FONT, relief=RAISED)
        label5.place(height=30, width=70, x=100, y=360)
        label6 = Label(self, textvariable=var6, font=BUTTON_FONT, relief=RAISED)
        label6.place(height=30, width=70, x=350, y=80)
        label7 = Label(self, textvariable=var7, font=BUTTON_FONT, relief=RAISED)
        label7.place(height=30, width=70, x=350, y=150)
        label8 = Label(self, textvariable=var8, font=BUTTON_FONT, relief=RAISED)
        label8.place(height=30, width=70, x=350, y=220)
        label9 = Label(self, textvariable=var9, font=BUTTON_FONT, relief=RAISED)
        label9.place(height=30, width=70, x=350, y=290)
        label10 = Label(self, textvariable=var10, font=BUTTON_FONT, relief=RAISED)
        label10.place(height=30, width=70, x=350, y=360)



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

        Label(self.frame2, text=" Admin", fg='red', font=("Vewdana", '14', 'bold'), height=3).pack()
        Label(self.frame2, text='Tye: ', font=font1, width=8).pack(side=LEFT)
        self.type = Entry(self.frame2, width=10, font=font1)
        self.type.focus_force()
        self.type.pack(side=LEFT)
        Label(self.frame5, text='Name IC: ', font=font1, width=8).pack(side=LEFT)
        self.name = Entry(self.frame5, width=10, font=font1)
        self.name.focus_force()
        self.name.pack(side=LEFT)
        Label(self.frame3, text='Integer: ', font=font1, width=8).pack(side=LEFT)
        self.Integer = Entry(self.frame3, width=10, font=font1)
        self.Integer.pack(side=LEFT)
        self.Enter = Button(self.frame4, font=font1, text='Enter', bg='green', command=self.check, relief=RAISED,
                            cursor="plus")
        self.Enter.pack()
        self.Back = Button(self.frame4, font=font1, text='Back', bg='red',  relief=RAISED, cursor="plus",
                           command=lambda: controller.show_frame("StartPage"))
        self.Back.pack()
        self.msg = Label(self.frame4, font=font1,  height=3,text='Your in put...')
        self.msg.pack()

    def check(self):
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
             else:
                self.msg.configure(text="Nothing to Add")

        if ans == "no":
            self.msg.configure(text=" ")

'''def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = UserInterface(root)
    app.mainloop()'''

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
