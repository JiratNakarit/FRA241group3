#!/usr/bin/python
import MySQLdb


class Database:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="fra241", db="fra241")
        self.cursor = self.db.cursor()

    def Commit(self):
        # Execute the SQL command
        self.cursor.execute(self.sql)
        # Commit your changes in the database
        self.db.commit()

    def Close(self):
        # disconnect from server
        self.db.close()

    # below is Function to Update new Data to database

    def id_user(self,value_idofic,value_numofall):
        self.sql = "UPDATE ic SET numofall = numofall -" + " " + str(value_numofall) + " " + "WHERE idofic = '%s'" % (str(value_idofic))

    def ic_admin(self,value_type,value_idofic,value_numofall,datasheet):
        self.sql = "INSERT INTO `ic`(`type`, `idofic`, `numofall` ,`datasheet`) VALUES" + " " + "('%s','%s','%d','%s')" % (str(value_type),str(value_idofic),value_numofall,datasheet)

    # -----------------------------------------------------------------------------------------------#
    # below is Functions to getting data from database
    def getData(self, table, column):
        sql = "SELECT " + str(column) + " FROM " + str(table)
        return sql

    def includeColumn(self, data):
        column = []
        count = 1
        pointer = 0

        for i in data:
            if count == 1:
                for k in i:
                    column.append([])

            for j in i:
                column[pointer].append(j)
                pointer += 1
            pointer = 0
            count += 1

        return column

    def data_user(self, cursor, column):
        sql = self.getData("user", "*")
        cursor.execute(sql)
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column]
        else:
            return list_column


    def data_ic(self, cursor, column):
        cursor.execute(self.getData("ic", "*"))
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column - 1]
        else:
            return list_column

    def data_history(self, cursor, column):
        cursor.execute(self.getData("history", "*"))
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column - 1]
        else:
            return list_column
            #-------------------------------------------------------------------------------------------#

Database = Database()
