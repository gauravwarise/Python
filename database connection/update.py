import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="Gaurav.2001@#",database="todo101")
    cu=db.cursor()
    q="update task set title='update records' where id=2"
    cu.execute(q)
    db.commit()
    fetch="select * from task where id=2"
    cu.execute(fetch)
    result=cu.fetchall()
    for i in result:
        print(i)
    db.close()
    print("Record updated successfully")
except Exception as e:
    print("Error: ",e)