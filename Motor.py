from Class import *
from ChinReceiveDataFromIcTable import *
from chin import *
#import RPi.GPIO as GPIO

print dataIn.Name_Ic       #ID
print getdata.list_main    #NUM
print (' ')
#GPIO.setmode(GPIO.BOARD)

Motor1 = 5
Motor2 = 6
Motor3 = 13

'''GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(Motor3, GPIO.OUT)'''


class motor():

    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.listmain_NUM = getdata.list_main  # NUM
        self.listmain_ID = dataIn.Name_Ic  # ID
        self.num_list_NUM = len(self.listmain_NUM)
        for i in range(self.num_list_NUM):
            chk_list = self.listmain_NUM[i]
            chkID_list = self.listmain_ID[i]
            num_chk = len(chk_list)
            for j in range(num_chk):
                chk_num = chk_list[j]
                chk_ID = chkID_list[j]
                if chk_num != 0:
                    self.list1.append(chk_ID)
                    self.list2.append(chk_num)
        print self.list1
        print self.list2





M = motor()




