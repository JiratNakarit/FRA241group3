import MySQLdb

class Database():
    def __init__(self):
        self.database = MySQLdb.connect(host = "localhost", user = "root",passwd = "", db = "test")

    def cursor(self):
        return self.database.cursor()

    def IncludeColumn(self,data):
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


class Connect_data(Database):
    db = Database()
    cursor = db.cursor()
    sql = "SELECT * from EMPLOYEE"

    cursor.execute(sql)

    data = cursor.fetchall()

    print db.IncludeColumn(data)














