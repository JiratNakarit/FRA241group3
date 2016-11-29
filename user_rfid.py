from Class import *
# Use below module when this program is used on RPi
import RPi.GPIO as GPIO
import MFRC522

class Read_RFID:

    def get_uid(self):
        # return uid in RFID
        rfid_uid = []
        # rfid_uid = [128,15,177,88]
        MIFAREReader = MFRC522.MFRC522()
        hex_uid = ''

        while True:
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print "Card detected"
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:
                rfid_uid = uid
                break

        rfid_uid.pop()
        rfid_uid.reverse()

        ###################
        # changes uid to hex number but on string
        for i in range(len(rfid_uid)):
            rfid_uid[i] = format(rfid_uid[i],'02x')

        for i in range(len(rfid_uid)):
            hex_uid = hex_uid + rfid_uid[i]

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

    def check_role(self,uid):
        lst = Database.data_user(Database.cursor,1)
        lst2 = Database.data_user(Database.cursor,1)
        lst_role = Database.data_user(Database.cursor,3)
        lst = list(lst)
        lst2 = list(lst2)
        for i in range(len(lst)):
            lst[i] = int(lst[i])

        for i in range(len(lst)):
            lst[i] = format(lst[i],'02x')

        for i in range(len(lst)):
            if uid == lst[i]:
                post = i
        role = lst_role[post]

        if role == 'admin':
            return True
        else:
            return False
