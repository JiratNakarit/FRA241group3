from Class import *


class item:
    dataIn = []
    Type_Ic = []
    Name_Ic = []

    for j in range(4):
        if (j == 0):
            for i in range(len(Database.data_ic(Database.cursor, 2))):
                if (Database.data_ic(Database.cursor, 2)[i] not in dataIn):
                    dataIn.append([])
                    dataIn[i].append(Database.data_ic(Database.cursor, 2)[i])
        elif (j == 1):
            for i in dataIn:
                if i not in Type_Ic:
                    Type_Ic.append(i)
        elif (j == 2):
            for i in range(len(Type_Ic)):
                Name_Ic.append(["Default"])
        elif (j == 3):
            check = 0
            for i in range(len(Database.data_ic(Database.cursor, 3))):
                for j in range(len(Type_Ic)):
                    if (Database.data_ic(Database.cursor, 2)[i] == Type_Ic[j][0]):
                        Name_Ic[j].append(Database.data_ic(Database.cursor, 3)[i])


dataIn = item()
#print dataIn.Type_Ic
#print dataIn.Name_Ic
