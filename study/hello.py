import pymysql

#打开数据库连接
db = pymysql.connect("localhost","TESTDB")

#使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute（）方法执行SQL查询
cursor.execute("SELECT VERSON()")

#使用fetchone（）方法获取单条数据
data = cursor.fetchone()

print("Database verson: %s".format(data))

db.close()