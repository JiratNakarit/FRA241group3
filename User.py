from Class import *
list=[['D_Type', 15], ['T_Type',0]]
D = UpDown_num()
for i in list:
     icid = i[0]
     numall = i[1]
     print icid,numall
     D.Update_trllo(icid,numall)
     D.Commit()











