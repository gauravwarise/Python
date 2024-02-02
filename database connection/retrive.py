import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="Gaurav.2001@#",database="todo101")
    cu=db.cursor()
    q="select * from task"
    cu.execute(q)
    result=cu.fetchall()
    for i in result:
        print(i)
    db.commit()
    db.close()
    print("Record show successfully")
except Exception as e:
    print("Error: ",e)