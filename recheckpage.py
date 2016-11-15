import Tkinter as tk
from Tkinter import *

TITLE1_FONT = ("Helvetica", 40, "bold")
EXPLAND_FONT = ("Helvetica", 10, "bold")
TITLE2_FONT = ("Helvetica", 25, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TYPE_FONT = ("Helvetica", 15, "bold")
IC_FONT = BUTTON_FONT
D_TYPE = ["Default", "741G374", "74HC74"]
JK_TYPE = ["Default", "DM7473", "DM7476"]
AND_GATE = ["Default", "74HC08", "DM7411"]
NAND_GATE = ["Default", "74LS10", "74LS13"]
OR_GATE = ["Default", "DM74LS32", "741G32"]

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(*args, borderwidth=20, bg = 'cyan', **kwargs)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1,minsize=300)
        container.grid_columnconfigure(0, weight=1,minsize=500)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):#, PageThree):
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
        label_1st = tk.Label(self, text="\n\nThe first step of using vending machines, electronic devices allow users to select \n "
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
                                    ,font=EXPLAND_FONT)
        label_1st.pack(side="top", fill="x", padx=100)
        button = tk.Button(self, text="I'm accept", height=2, font=BUTTON_FONT, command=lambda: controller.show_frame("PageOne"))
        button.pack(side=BOTTOM , fill='x')



def In1():
    global count1
    count1 += 1
    var1.set(count1)
    var6.set(count1)



def De1():
    global count1
    count1 -= 1
    if count1 <= 0:
        count1 = 0
    var1.set(count1)
    var6.set(count1)

def In2():
    global count2
    count2 += 1
    var2.set(count2)
    var7.set(count2)
def De2():
    global count2
    count2 -= 1
    if count2 <= 0:
        count2 = 0
    var2.set(count2)
    var7.set(count2)
def In3():
    global count3
    count3 += 1
    var3.set(count3)
    var8.set(count3)
def De3():
    global count3
    count3 -= 1
    if count3 <= 0:
        count3 = 0
    var3.set(count3)
    var8.set(count3)
def In4():
    global count4
    count4 += 1
    var4.set(count4)
    var9.set(count4)

def De4():
    global count4
    count4 -= 1
    if count4 <= 0:
        count4 = 0
    var4.set(count4)
    var9.set(count4)
def In5():
    global count5
    count5 += 1
    var5.set(count5)
    var10.set(count5)
def De5():
    global count5
    count5 -= 1
    if count5 <= 0:
        count5 = 0
    var5.set(count5)
    var10.set(count5)



class PageOne(tk.Frame):

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
        variable1 = StringVar(self)
        variable1.set(D_TYPE[0])
        global variable2
        variable2 = StringVar(self)
        variable2.set(JK_TYPE[0])
        global variable3
        variable3 = StringVar(self)
        variable3.set(AND_GATE[0])
        global variable4
        variable4 = StringVar(self)
        variable4.set(OR_GATE[0])
        global variable5
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
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.count5 = 0
        self.count6 = 0
        self.count7 = 0
        self.count8 = 0
        self.count9 = 0
        self.count10= 0
        global var1
        var1 = StringVar(self)
        var1.set(self.count1)
        global var2
        var2 = StringVar(self)
        var2.set(self.count2)
        global var3
        var3 = StringVar(self)
        var3.set(self.count3)
        global var4
        var4 = StringVar(self)
        var4.set(self.count4)
        global var5
        var5 = StringVar(self)
        var5.set(self.count5)
        global var6
        var6 = StringVar(self)
        var6.set(self.count6)
        global var7
        var7 = StringVar(self)
        var7.set(self.count7)
        global var8
        var8 = StringVar(self)
        var8.set(self.count8)
        global var9
        var9 = StringVar(self)
        var9.set(self.count9)
        global var10
        var10 = StringVar(self)
        var10.set(self.count10)
        b1 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=In1)
        b1.place(height=30, width=30, x=700, y=80)
        label1 = Label(self, textvariable=var1, font=BUTTON_FONT, relief=RAISED)
        label1.place(height=30, width=70, x=605, y=80)
        b2 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=De1)
        b2.place(height=30, width=30, x=550, y=80)
        b3 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=In2)
        b3.place(height=30, width=30, x=700, y=150)
        label2 = Label(self, textvariable=var2, font=BUTTON_FONT, relief=RAISED)
        label2.place(height=30, width=70, x=605, y=150)
        b4 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=De2)
        b4.place(height=30, width=30, x=550,y=150)
        b5 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=In3)
        b5.place(height=30, width=30, x=700, y=220)
        label3 = Label(self, textvariable=var3, font=BUTTON_FONT, relief=RAISED)
        label3.place(height=30, width=70, x=605, y=220)
        b6 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command= De3)
        b6.place(height=30, width=30, x=550, y=220)
        b7 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=In4)
        b7.place(height=30, width=30, x=700, y=290)
        label4 = Label(self, textvariable=var4,font=BUTTON_FONT, relief=RAISED)
        label4.place(height=30, width=70, x=605, y=290)
        b8 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=De4)
        b8.place(height=30, width=30, x=550, y=290)
        b9 = Button(self, text="+", font=BUTTON_FONT, bg='green', command=In5)
        b9.place(height=30, width=30, x=700, y=360)
        label5 = Label(self, textvariable=var5, font=BUTTON_FONT, relief=RAISED)
        label5.place(height=30, width=70, x=605, y=360)
        b10 = Button(self, text="-", font=BUTTON_FONT, bg='pink', command=De5)
        b10.place(height=30, width=30, x=550, y=360)


        button1 = tk.Button(self, text="Go to the start page", font=BUTTON_FONT, command=lambda: controller.show_frame("StartPage"))
        button1.place(x=20, y=460)
        button2 = tk.Button(self, text="Sure", font=BUTTON_FONT, command=lambda: controller.show_frame("PageTwo") )

        button2.place(x=700, y=460)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = tk.Button(self, text="Not sure",font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Sure",font=BUTTON_FONT,
                           command=lambda: controller.show_frame("PageThree"))
        button.place(x=20, y=460)
        button2.place(x=700, y=460)


        if variable1.get() == str("Default") and var6.get() == str(0):
            label1 = Label(self, textvariable=variable1, font=BUTTON_FONT, relief=RAISED)
            label1.place(x=25, y=80)
            label2 = Label(self, textvariable=var6, font=BUTTON_FONT, relief=RAISED)
            label2.place(height=30, width=70, x=605, y=80)
        if variable2.get()==str("Default") and var7.get() == str(0) :

            label3 = Label(self, textvariable=variable2, font=BUTTON_FONT, relief=RAISED)
            label3.place(x=25, y=150)
            label4 = Label(self, textvariable=var7, font=BUTTON_FONT, relief=RAISED)
            label4.place(height=30, width=70, x=605, y=150)

        if variable3.get() == str("Default") and var8.get() == str(0) :

            label5 = Label(self, textvariable=variable3, font=BUTTON_FONT, relief=RAISED)
            label5.place(x=25, y=220)
            label6 = Label(self, textvariable=var8, font=BUTTON_FONT, relief=RAISED)
            label6.place(height=30, width=70, x=605, y=220)
        if variable4.get() == str("Default") and var9.get() == str(0):

            label7 = Label(self, textvariable=variable4, font=BUTTON_FONT, relief=RAISED)
            label7.place(x=25, y=290)
            label8 = Label(self, textvariable=var9, font=BUTTON_FONT, relief=RAISED)
            label8.place(height=30, width=70, x=605, y=290)
        if variable5.get() == str("Default") and var10.get() == str(0):
            label9 = Label(self, textvariable=variable5, font=BUTTON_FONT, relief=RAISED)
            label9.place(x=25, y=360)
            label9 = Label(self, textvariable=var10, font=BUTTON_FONT, relief=RAISED)
            label9.place(height=30, width=70, x=605, y=360)







# class PageThree(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label_1sttitle = tk.Label(self, text="Scan your student ID card", font=TITLE1_FONT)
#         label_1sttitle.pack(side="top", fill="x", pady=0)

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()


