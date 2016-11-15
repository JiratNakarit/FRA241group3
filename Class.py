#!/usr/bin/python
import MySQLdb


class Database:
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


Database = Database()
