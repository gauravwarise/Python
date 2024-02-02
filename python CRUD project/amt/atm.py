from cardholder import cardHolder

def print_menu():
    print("Please choose from one of the following options....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much amount would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you!! Your amount is debited successfully...")
        print("Your account balance is: ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much amount would you like to withdraw: "))
        if(cardHolder.get_balance()< withdraw):
            print("Insufficient balance: ")
        else:

            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go !!!")
            print("Thank you!! Your amount is withdraw successfully...")
            print("Your account balance is: ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ",cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    # create a repo of cardHolder
    list_of_cardHolder = []
    list_of_cardHolder.append(cardHolder("1234567890",1234,"gaurav","warise",150.32))
    list_of_cardHolder.append(cardHolder("9876543211",9876,"rahul","mishra",600.28))
    list_of_cardHolder.append(cardHolder("5432112345",5432,"onkar","shinde",300.37))
    list_of_cardHolder.append(cardHolder("6789009876",6789,"sejal","shinde",10.09))
    
    # prompt user from debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            # Check against repo
            debitMatch = [holder for holder in list_of_cardHolder if holder.cardnum == debitCardNum]
            if(len(debitMatch)>0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")
    
    # prompt for pin
    while True:
        try:
            userPin = int(input("Please enter your pin: ".strip()))
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again")
        except:
            print("Invalid PIN. Please try again")
    
    # print options
    print("Welcome ", current_user.get_firstname(),":)")
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
    
    print("Thank you !!! Have a nice day")