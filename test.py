import MySQLdb

class database():
    def __init__(self):
        self.database = MySQLdb.Connect(host = "localhost", user = "root",passwd = "", db = "test")
        self.cursor = self.database.cursor()

def Update(table,column,operator,value,data,case):
    if data != None:
        command = "UPDATE " + str(table) + " SET " + str(column) + " = " + str(column) + " " + str(operator) + " " + \
                str(value) + " WHERE " + str(data) + " = " + 'chin'
        return command
    else:
        command = "UPDATE " + str(table) + " SET " + str(column) + " = " + str(column) + " " + str(operator) + " " + \
                str(value)
        return command

sql1 = Update("employee","age","+","1","first_name","chin")
print sql1

def Select(column,table,data,case):
    if data != None:
        command = "SELECT " + str(column) + " FROM " + str(table) + " WHERE " + str(data) + " " + str(case)
        return command
    else:
        command = "SELECT " + str(column) + " FROM " + str(table)
        return command

db = database()

sql = Select("*","EMPLOYEE",None,None)

db.cursor.execute(sql1)
db.database.commit()

db.cursor.execute(sql)
data = db.cursor.fetchall()

def IncludeColumn(data):
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

column = IncludeColumn(data)

print(column)
db.database.close()