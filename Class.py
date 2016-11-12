#!/usr/bin/python
import MySQLdb

class UpDown_num:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="fra241", db="test")
        self.cursor = self.db.cursor()

    '''def D_Typeupdate(self,iv):
        self.sql = "UPDATE trello SET Available = Available +" + " " + str(iv) + " " + "WHERE IC = '%s'" % ('D_Type')

    def T_Typeupdate(self,iv):
        self.sql = "UPDATE trello SET Available = Available +" + " " + str(iv) + " " + "WHERE IC = '%s'" % ('T_Type')'''

    def Update(self,icid,numall):
        self.sql = "UPDATE machine SET numall = numall -" + " " + str(numall) + " " + "WHERE icid = '%s'" % (str(icid))         #Arm

    def Update_trllo(self, icid, numall):
        self.sql = "UPDATE trello SET Available = Available -" + " " + str(numall) + " " + "WHERE IC = '%s'" % (str(icid))


    def Admin(self,value_ic,value_type):
        self.sql = "INSERT INTO `ic`(`icid`, `type`) VALUES" + " " + "('%s','%s')" %(str(value_ic),str(value_type))             #Bank

    def trello(self):
        self.sql = "INSERT INTO `trello`(`IC`) VALUES" + " " + "('%s')" %(str('eieiei'))

    def Commit(self):

            # Execute the SQL command
            self.cursor.execute(self.sql)
            # Commit your changes in the database
            self.db.commit()

    def Close(self):
        # disconnect from server
        self.db.close()
D = UpDown_num()


