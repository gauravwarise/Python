import pymysql as p
import random as r
# con=p.connect(host="localhost",user="root",passwd="Gaurav.2001@#",database="bankmanagement",port=3306)
def connect():
    return p.connect(host="localhost", user="root",password="Gaurav.2001@#",database='bankmanagement',port=3306)

ano=r.randint(123456789,3000000000)
while True:
    print("*"*115)
    print(" "*45,end="")
    print("Bank Management System")
    print("*"*115)
    con=connect()#this function helps to call coonect function for database connectivity.
    cu=con.cursor()#cursor creation
    choice=int(input(" 1->Open Account\n 2->Cash Deposit\n 3->Cash Withdrawal\n 4->Account Statement\n 5->Update Account\n 6->Exit\n Enter Your Choice: "))
    
    if choice == 1:
        print("="*115)
        name=input("Enter Name of Account Hoolder: ")
        balance=int(input("Enter opening balance: "))
        mob=input("Enter Registered Mobile Number: ")
        query = "Insert into bank values({},'{}',{},'{}')".format(ano,name,balance,mob)
        ano=ano+1
        cu.execute(query)
        con.commit()

        print("Account created successfully..!")
        print("="*115)
    
    if choice == 2:
        account = int(input("Enter youre account number: "))
        query = "select * from bank where acno={}".format(account)
        cu.execute(query)
        data=cu.fetchone()
        
        if account == data[0]:
            amount=int(input("How much amount would you like to deposit: "))
            temp_amount=data[2]+amount
            query = "update bank set balance={} where acno={}".format(temp_amount,account)
            cu.execute(query)
            con.commit()
            con.close()
            print("Deposit successfully..!!")
        else:
            print("Invalid Entry!!!")
    
    if choice == 3:
        account = int(input("Enter youre account number: "))
        query = "select * from bank where acno={}".format(account)
        cu.execute(query)
        data=cu.fetchone()
        
        if account == data[0]:
            amount=int(input("How much amount would you like to withdrawal: "))
            if data[2]>amount:
                temp_amount=data[2]-amount
                query = "update bank set balance={} where acno={}".format(temp_amount,account)
                cu.execute(query)
                con.commit
                print("withdrawal successfully..!!")
            else:
                print("You have insufficient balance..!!")
        else:
            print("Invalid Entry!!!")


    if choice == 4:
        print("="*115)
        account = int(input("Enter Account Number: "))
        query = "Select * from bank where acno={}".format(account)
        cu.execute(query)
        data=cu.fetchone()
        # print(data)
        if account == data[0]:
            print("="*115)
            print("Account Details are: ")
            print("Account Number: ",data[0])
            print("Name: ",data[1])
            print("Balance: ",data[2])
            print("Mobile Number: ",data[3])
            print("="*115)
        else:
            print("Account not found")
            print("="*115)

    if choice == 5:
        account=input("Enter Account you want to update:")
        query="Select * from bank where acno={}".format(account)
        #q="update task set id=%s,title=%s,detail=%s,date=%s where id=%s"
        cu.execute(query)
        data=cu.fetchone()
        if data==None:
            print("Record Not Found")
        else:
            print("Account Number:",data[0])
            print("1]Name:",data[1])
            print("2]Mobile Number:",data[3])
            print("3]Exit:")

            ch=int(input("Enter your choice:"))
            # temp_variable=""
            if ch==1:
                new_n=input("Enter New Name:")
                # temp_variable="fullName='{}'".format(new_n)
                qu="update bank set name='{}' where acno={}".format(new_n,account) 
                print(qu)
                cu.execute(qu)
                con.commit()
                print("Record updated")
            elif ch==2:
                new_m=input("Enter New Mobile Number:")
                # temp_variable="mobileNumber={}".format(new_m)
                qu="update bank set mob={} where acno={}".format(new_m,account) 
                cu.execute(qu)
                con.commit()
                print("Record Updated")
            elif ch==3:
                print("Exit")
            else:
                print("Invalid choice")
            # if not temp_variable=='':
                # qu="update bank set '{}' where acno={}".format(temp_variable,account) 
                # print(qu)
                # cu.execute(qu)
                # con.commit()
                # print("Record updated")     

    if choice == 6:
        break
