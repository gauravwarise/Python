import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="Gaurav.2001@#",database="todo101")
    cu=db.cursor()
    q="insert into task(id,title,details,date) values(1,'Insert record','insert record into table','2022-12-02'),(2,'Insert record','insert record into table','2022-12-02')"
    cu.execute(q)
    db.commit()
    print("Record inserted successfully")
except Exception as e:
    print("Error: ",e)