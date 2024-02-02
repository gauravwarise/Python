import pymysql

db=pymysql.connect(host="localhost",user="root",password="Gaurav.2001@#",database="todo101")

if db.is_connected():
    print("successfull")