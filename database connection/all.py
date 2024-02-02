import pymysql as p  

def connect():
    return p.connect(host="localhost", user="root",password="Gaurav.2001@#",database='todo101',port=3306)

def insert(t):
    con=connect()#this function helps to call coonect function for database connectivity.
    cu=con.cursor()#cursor creation
    q="insert into task values(%s,%s,%s,%s)"
    cu.execute(q,t)
    print("record inserted successfully")
    con.commit()
    con.close()
    
def select():
    con=connect()
    cu=con.cursor()
    #q="select * from task"
    id=1
    q="select * from task where id='{}'".format(id)
    cu.execute(q)
    data=cu.fetchall()
    print(data)
    con.commit()
    con.close()
    
def update():
    con=connect()
    cu=con.cursor()
    id=input("Enter Task ID you want to update:")
    q="Select * from task where id='{}'".format(id)
    #q="update task set id=%s,title=%s,detail=%s,date=%s where id=%s"
    cu.execute(q)
    row=cu.fetchone()
    if row==None:
        print("Record Not Found")
    else:
        print("ID:",row[0])
        print("1]Title:",row[1])
        print("2]Details:",row[2])
        print("3]Date:",row[3])
        print("4]Exit:")

        ch=int(input("Enter your choice:"))
        p=""
        if ch==1:
            new_t=input("Enter New Title:")
            p="title='{}'".format(new_t)
        elif ch==2:
            new_d=input("Enter New detail:")
            p="detail='{}'".format(new_d)
        elif ch==3:
            new_dt=input("Enter New date:")
            p="date='{}'".format(new_dt)  
        elif ch==4:
            print("Exit")
        else:
            print("Invalid choice")
        if not p=='':
            qu="update task set {} where id={}".format(p,id) 
            print(qu)
            cu.execute(qu)
            con.commit()
            print("Record updated")
    con.close()

def delete():
    con=connect()
    cu=con.cursor()
    id=input("Enter Task ID you want to delete:")
    # q="delete from task where id=%s"
    # cu.execute(q,id)
    # con.commit()
    # con.close()
    q="Select * from task where id='{}'".format(id)
    #q="update task set id=%s,title=%s,detail=%s,date=%s where id=%s"
    cu.execute(q)
    row=cu.fetchone()
    if row==None:
        print("Record Not Found")
    else:
        print("ID:",row[0])
        print("1]Title:",row[1])
        print("2]Details:",row[2])
        print("3]Date:",row[3])
        print("4]Exit:")
        
        qu="delete from task where id={}".format(id) 
        print(qu)
        cu.execute(qu)
        con.commit()
        print("Record deleted")
    con.close()
    
print("select 1 to insert record \n select 2 to retrive data\n select 3 to update data\n select 4 to delete data")
c=int(input("Enter your CHOICE:"))

if c==1:
    id=int(input("Enter Task ID:"))
    title=input("Enter task to be done:")
    detail=input("Enter details of the task:")
    date=input("Enter date")
    
    t=(id,title,detail,date)
    insert(t)
elif c==2:
    select()
elif c==3:
    update()
elif c==4:
    delete()  