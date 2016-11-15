import tkMessageBox
from Tkinter import *

from Class import *



class Admin:
    def __init__(self, toplevel):
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

        Label(self.frame2, text=" Admin", fg='red',
              font=("Vewdana", '14', 'bold'), height=3).pack()

        fonte1 = ('Verdana', '10', 'bold')

        Label(self.frame2, text='Tye: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.tye = Entry(self.frame2, width=10,
                         font=fonte1)
        self.tye.focus_force()
        self.tye.pack(side=LEFT)

        Label(self.frame5, text='Name IC: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.name = Entry(self.frame5, width=10,
                          font=fonte1)
        self.name.focus_force()
        self.name.pack(side=LEFT)

        Label(self.frame3, text='Integer: ',
              font=fonte1, width=8).pack(side=LEFT)
        self.Integer = Entry(self.frame3, width=10,
                             font=fonte1)
        self.Integer.pack(side=LEFT)

        self.Enter = Button(self.frame4, font=fonte1, text='Enrter', bg='green', command=self.conferir, relief=RAISED,
                            cursor="plus")
        self.Enter.pack()

        self.Back = Button(self.frame4, font=fonte1, text='Back', bg='red', relief=RAISED,
                           cursor="plus")
        self.Back.pack()

        self.msg = Label(self.frame4, font=fonte1, height=3, text='Your in put...')
        self.msg.pack()

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


instance = Tk()
instance.title("Admin CH")
instance.geometry("650x400")
Admin(instance)
instance.mainloop()
