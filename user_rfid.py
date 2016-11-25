from Class import *


class Read_RFID:
    def __init__(self):
        ## for test
        self.test_uid = [128,15,141,59]

    def get_uid(self,lst_uid = [0,0,0,0,0]):
        # return uid in RFID
        # wait for code to get uid
        ##################

        ## Input yor code here
        ##

        ###################
        hex_uid = ''
        # changes uid to hex number but on string
        for i in range(len(self.test_uid)):
            self.test_uid[i] = format(self.test_uid[i],'02x')

        for i in range(len(self.test_uid)):
            hex_uid = hex_uid + self.test_uid[i]

        print "Hello"
        return hex_uid

    # Check data from RFID in database
    #     |
    #     |- parameter uid as string(hexa number)
    #     |- return boolean (True or Fase)
    def check_on_database(self,uid):
        lst = Database.data_user(Database.cursor,1)
        lst = list(lst)

        for i in range(len(lst)):
            lst[i] = int(lst[i])

        for i in range(len(lst)):
            lst[i] = format(lst[i],'02x')

        if uid in lst:
            return True
        else:
            return False

    def get_stid(self,uid):
        lst = Database.data_user(Database.cursor,1)
        lst2 = Database.data_user(Database.cursor,1)
        lst = list(lst)
        lst2 = list(lst2)
        for i in range(len(lst)):
            lst[i] = int(lst[i])

        for i in range(len(lst)):
            lst[i] = format(lst[i],'02x')

        for i in range(len(lst)):
            if uid == lst[i]:
                post = i
        return int(lst2[post])
