import tkMessageBox
from Tkinter import *
import tkSimpleDialog as simpledialog

from Class import *



class Admin(Frame):
    def __init__(self, toplevel,parent=None,**kw):
        Frame.__init__(self,parent,**kw)
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
        self.frame2 = Frame(toplevel)
        self.frame2.pack()
        self.frame5 = Frame(toplevel)
        self.frame5.pack()
        self.frame3 = Frame(toplevel)
        self.frame3.pack()
        self.frame4 = Frame(toplevel, pady=10)
        self.frame4.pack()
        self.textEntryVar = StringVar()
        self.textEntryVar2 = StringVar()
        self.textEntryVar3 = StringVar()

        Label(self.frame2, text=" Admin", fg='red',
              font=("Vewdana", '14', 'bold'), height=3).pack()

        fonte1 = ('Verdana', '10', 'bold')

        Label(self.frame2, text='Tye: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.tye = Entry(self.frame2, width=10,
                         font=fonte1,textvariable=self.textEntryVar)
        self.tye.pack(side=LEFT)
        self.tye.bind('<FocusIn>',self.numpadEntry1)

        Label(self.frame5, text='Name IC: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.name = Entry(self.frame5, width=10,
                          font=fonte1,textvariable=self.textEntryVar2)
        self.name.pack(side=LEFT)
        self.name.bind('<FocusIn>',self.numpadEntry2)
        #############33

        Label(self.frame3, text='Integer: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.Integer = Entry(self.frame3, width=10,
                             font=fonte1,textvariable=self.textEntryVar3)
        self.Integer.pack(side=LEFT)
        self.Integer.bind('<FocusIn>',self.numpadEntry3)
        ###############

        self.Enter = Button(self.frame4, font=fonte1, text='Enrter', bg='green', command=self.conferir, relief=RAISED,
                            cursor="plus")
        self.Enter.pack()

        self.Back = Button(self.frame4, font=fonte1, text='Back', bg='red', relief=RAISED,
                           cursor="plus")
        self.Back.pack()

        self.msg = Label(self.frame4, font=fonte1, height=3, text='Your in put...')
        self.msg.pack()

        self.edited = 0
        self.count = 0


    def conferir(self):

        ans = tkMessageBox.askquestion("Are you ok", "check you in put")

        if ans == "yes":
            if self.Integer.get().isdigit():
                self.msg.configure(text=(self.tye.get(), "__", self.name.get(), "__", self.Integer.get()))
                # print (self.tye.get(),self.name.get(),self.Integer.get())
                x = []
                x.append(self.tye.get())
                x.append(self.name.get())
                x.append(int(self.Integer.get()))
                print type(x)
                print x
                value_type = x[0]
                value_name = x[1]
                value_numall = x[2]
                Database.ic(value_type, value_name)
                Database.Commit()
                Database.machine(value_numall)
                Database.Commit()
            else:
                self.msg.configure(text="try agan  Ja")

        if ans == "no":
            self.msg.configure(text="not ")

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
        '1',    '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace',
        'Tab',  'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '(', ')', '|',
        'Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '_', 'Enter',
        'Shift','Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift',
        '<<',   'Space', '>>', 'Clear'
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
            cur = Button(self.top, text=label, width=10, height=5, command=cmd)
            btn.append(cur)
            # position the button
            btn[-1].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c == 13:
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
        self.top.destroy()
        self.top.master.focus()




instance = Tk()
instance.title("Admin CH")
instance.geometry("650x400")
Admin(instance)
instance.mainloop()
