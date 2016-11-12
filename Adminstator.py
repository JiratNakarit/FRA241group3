from Class import *
list1=[['74hc64','Drive_motor'],['74hc00','T_Type']]
D = UpDown_num()
for i in list1:
     value_ic = i[0]
     value_type = i[1]
     D.Admin(value_ic,value_type)
     D.Commit()

