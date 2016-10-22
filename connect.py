import MySQLdb


class Database():
    def __init__(self):
        self.database = MySQLdb.connect(host="localhost", user="root", passwd="", db="fra241")
        self.cursor = self.database.cursor()

    def getData(self,table, column):
        sql = "SELECT " + str(column) + " FROM " + str(table)
        return sql

    def includeColumn(self,data):
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



    def data_user(self,cursor, column):
        sql = self.getData("user","*")
        cursor.execute(sql)
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column]
        else:
            return list_column

    def data_machine(self, cursor, column):
        cursor.execute(self.getData("machine", "*"))
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column-1]
        else:
            return list_column

    def data_ic(self, cursor, column):
        cursor.execute(self.getData("ic", "*"))
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column-1]
        else:
            return list_column

    def data_history(self, cursor, column):
        cursor.execute(self.getData("history", "*"))
        data = cursor.fetchall()
        list_column = self.includeColumn(data)
        if column != "*":
            return list_column[column-1]
        else:
            return list_column

    #name = data_user(db,cursor,2)
    #stid = data_user(db,cursor,4)
    #num_in_machine = data_machine(db,cursor,2)

