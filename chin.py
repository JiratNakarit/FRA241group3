from Tkinter import *
import tkMessageBox
import Tkinter as tk
import Tkinter
import tkMessageBox
from Class import *



B = Database.data_ic(Database.cursor,4)
E = len(B)
class Getdata_Tar():
        list_main = []
        list = []
        for i in range(E):
            type = B[i]
            if (i<=1):
                if i == 0:
                    list_main.append(list)
                    list.append(0)
                    list.append(type)
                else:
                    list.append(type)
                    list = []

            elif i>1 and i<=3:
                if i == 2:
                    list_main.append(list)
                    list.append(0)
                    list.append(type)
                else:
                    list.append(type)
                    list = []
            elif i>3 and i<=5:
                if i == 4:
                    list_main.append(list)
                    list.append(0)
                    list.append(type)
                else:
                    list.append(type)
                    list = []
            elif i>5 and i<=7:
                if i == 6:
                    list_main.append(list)
                    list.append(0)
                    list.append(type)
                else:
                    list.append(type)
                    list = []
            elif i>7 and i<=9:
                if i == 8:
                    list_main.append(list)
                    list.append(0)
                    list.append(type)
                else:
                    list.append(type)
getdata =Getdata_Tar()
#print getdata.list_main






