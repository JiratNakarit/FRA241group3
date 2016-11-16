from Tkinter import *
import tkMessageBox
import Tkinter as tk
import Tkinter
import tkMessageBox
from Class import *

list_main = []
list = []

B = Database.data_ic(Database.cursor,3)
E = len(B)

for i in range(E):
    type = B[i]

    if (i<=1):
        if i == 0:
            list_main.append(list)
            list.append("Deflaut")
            list.append(type)
        else:
            list.append(type)
            list = []

    elif i>1 and i<=3:
        if i == 2:
            list_main.append(list)
            list.append("Deflaut")
            list.append(type)
        else:
            list.append(type)
            list = []
    elif i>3 and i<=5:
        if i == 4:
            list_main.append(list)
            list.append("Deflaut")
            list.append(type)
        else:
            list.append(type)
            list = []
    elif i>5 and i<=7:
        if i == 6:
            list_main.append(list)
            list.append("Deflaut")
            list.append(type)
        else:
            list.append(type)
            list = []
    elif i>7 and i<=9:
        if i == 8:
            list_main.append(list)
            list.append("Deflaut")
            list.append(type)
        else:
            list.append(type)
print list_main







