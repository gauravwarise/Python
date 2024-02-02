import pymysql as p
import random as r
def connect():
    return p.connect(host="localhost", user="root",password="Gaurav.2001@#",database='bankmanagement',port=3306)

AccountNum=r.randint(1000000,2000000)


while True:
    #print Heading
    print("*"*115)
    print(" "*45,end="")
    print("|| Wellcome to ATM ||")
    print("*"*115)
    con=connect()
    cu=con.cursor()
    try:
        choice=int(input(" 1->Open Account\n 2->Cash Deposit\n 3->Cash Withdrawal\n 4->Account Statement\n 5->Update Account\n 6->Delete Account\n 7->Exit\n Enter Your Choice: "))
    except ValueError:
        print("Enter valid number..!!")
        pass
    if choice == 1:
        # create account
        print("="*115)
        name=input("Enter Full Name of Account Holder: ")
        mob=input("Enter Registered Mobile Number: ")
        balance=int(input("Enter opening balance: "))
        pin=int(input("Enter 4 Digits Sequrity PIN: "))
        query = "Insert into atm values({},'{}','{}',{},{})".format(AccountNum,name,mob,balance,pin)
        cu.execute(query)
        con.commit()

        print(" Account created successfully..!\n Your Account Number is {}".format(AccountNum))
        print("="*115)
    
    elif choice == 2:
        # Debit amount
        account = int(input("Enter youre AccountNumber: "))
        pin = int(input("Enter security PIN: "))
        query = "select * from atm where SecurityPin={}".format(pin)
        cu.execute(query)
        data=cu.fetchone()
        try:
            if pin == data[4]:
                amount=int(input("How much amount would you like to deposit: "))
                temp_amount=data[3]+amount
                query = "update atm set balance={} where SecurityPin={}".format(temp_amount,pin)
                cu.execute(query)
                con.commit()
                con.close()
                print(" Deposit successfully..!! \n Your Account Balance is:{}".format(temp_amount) )

        except:
            print("Invalid Entry!!!")
    
    elif choice == 3:
        # withdraw amount
        account = int(input("Enter youre AccountNumber: "))
        pin = int(input("Enter security PIN: "))
        query = "select * from atm where SecurityPin={}".format(pin)
        cu.execute(query)
        data=cu.fetchone()
        try:
            if pin == data[4]:
                amount=int(input("How much amount would you like to withdraw : "))
                if data[3]>=amount:
                    temp_amount=data[3]-amount
                    query = "update atm set balance={} where SecurityPin={}".format(temp_amount,pin)
                    cu.execute(query)
                    con.commit()
                    con.close()
                    print("withdrawal successfully..!!\n Your Account Blanace is: {}".format(temp_amount))
                else:
                    print("You have insufficient balance..!!!")
        except:
                print("Invalid Entry!!!")
        


    elif choice == 4:
        # Account Satatments
        print("="*115)
        mob = input("Enter Registered Mobile Number: ")
        pin=int(input("Enter Security PIN: "))
        query = "Select * from atm where SecurityPin={}".format(pin)
        cu.execute(query)
        data=cu.fetchone()
        
        # print(data)
        try: 
            if pin == data[4]:
                print("="*115)
                print("Account Details are: ")
                print("Account Number: ",data[0])
                print("Name: ",data[1])
                print("Mobile Number: ",data[2])
                print("Balance: ",data[3])
                print("="*115)
        except:
                # raise TypeError("Account Not Found..!!")
                print("Account not found")
                print("="*115)

    elif choice == 5:
        account=input("Enter Account Number you want to update:")
        query="Select * from atm where AccountNumber={}".format(account)
        cu.execute(query)
        data=cu.fetchone()
        if data==None:
            print("Record Not Found")
        else:
            print("Account Number:",data[0])
            print("1]Name:",data[1])
            print("2]Mobile Number:",data[2])
            print("3]Exit:")

            ch=int(input("Enter your choice:"))
            
            if ch==1:
                new_n=input("Enter New Name:")
                # temp_variable="fullName='{}'".format(new_n)
                qu="update atm set FullName='{}' where AccountNumber={}".format(new_n,account) 
                # print(qu)
                cu.execute(qu)
                con.commit()
                print("Record updated")
                print("{} Changed to {}".format(data[1],new_n))
            elif ch==2:
                new_m=input("Enter New Mobile Number:")
                # temp_variable="mobileNumber={}".format(new_m)
                qu="update atm set MobileNumber='{}' where AccountNumber={}".format(new_m,account) 
                cu.execute(qu)
                con.commit()
                print("Record Updated")
                print("{} Changed to {}".format(data[2],new_m))
            elif ch==3:
                print("Exit")
            else:
                print("Invalid choice")
     

    elif choice == 6:
        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN: "))
        query1 = "select * from atm where SecurityPin={}".format(pin)
        cu.execute(query1)
        data = cu.fetchone()
        
        
        query2 = "delete from atm where SecurityPin={}".format(pin)
        cu.execute(query2)
        con.commit()

        print("Account will deleted successfully..!!")

        



    elif choice == 7:
        break

    else:
        print("Invalid Choice")

     