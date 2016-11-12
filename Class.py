#!/usr/bin/python
import MySQLdb

class UpDown_num:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="fra241", db="test")
        self.cursor = self.db.cursor()

    def Update(self,icid,numall):
        self.sql = "UPDATE machine SET numall = numall -" + " " + str(numall) + " " + "WHERE icid = '%s'" % (str(icid))

    def Update_trllo(self, icid, numall):
        self.sql = "UPDATE trello SET Available = Available -" + " " + str(numall) + " " + "WHERE IC = '%s'" % (str(icid))


    def ic(self,value_type,value_name):
        self.sql = "INSERT INTO `ic`(`type`,`name`) VALUES" + " " + "('%s','%s')" % (str(value_type),str(value_name))

    def machine(self,value_numall):
        self.sql = "INSERT INTO `machine`(`numall`) VALUES" + " " + "('%d')" % (value_numall)

    def Commit(self):

            # Execute the SQL command
            self.cursor.execute(self.sql)
            # Commit your changes in the database
            self.db.commit()

    def Close(self):
        # disconnect from server
        self.db.close()
D = UpDown_num()


