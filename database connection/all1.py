
import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="Gaurav.2001@#" ,database="todo101")

def insert(t):
    con=connect() #This function helps to call connect function for database connectivity
    cu=con.cursor() #cursor creation
    q="insert into task values(%s,%s,%s,%s)"
    cu.execute(q,t)
    con.commit()
    con.close()

def select():
    con=connect()
    cu=con.cursor()
    q="select * from task"
    cu.execute(q)
    data=cu.fetchall()
    print(data)
    con.commit()
    con.close()

def update(data):
    con=connect()
    cu=con.cursor()
    q="update task set id=%s title=%s,detail=%s,date=%s where id=%s"
    cu.execute(q,data)
    con.commit()
    con.close()

def delete(id):
    con=connect()
    cu=con.cursor()
    q="delete from task where id=%s"
    cu.execute(q,id)
    con.commit()
    con.close()

print("select 1 to insert record \n select 2 to retrive data \n select 3 to update data \n select 4 to delete data: ")
c=int(input("Enter your choice: "))

if c==1:
    id=int(input("Enter your task id: "))
    title=input("Enter task to be done: ")
    detail=input("Enter details of the task: ")
    date=input("Enter date: ")

    t=(id,title,detail,date)
    insert(t)
    print("Record inserted successfully")
elif c==2:
    select()
# elif c==3:
#     # id1=int(input("Enter id which you wnt to update: "))
#     id=int(input("Enter your task id: "))
#     title=input("Enter task to be done: ")
#     detail=input("Enter details of the task: ")
#     date=input("Enter date: ")
#     id1=int(input("Enter id which you wnt to update: "))
#     data=(id,title,detail,date,id1)
#     update(data)
#     print("After updating: ",select())
elif c==4:
    id=int(input("Enter your task id: "))
    # u=(id,title,detail,date)
    delete(id)
    print("delete successfully")
    # print("After updating: ",select())
    select()