print("Build a banking system which has the following functionalities :: 2.1 Add account for a new user 2.2 Add money to the account 2.3 Withdraw money from the account 2.4 Display balance for a particular user")
accounts={}
def add_account():
    name=input("\n Enter your name: ")
    balance=int(input("\n Enter your min balance amount: "))
    accounts[name]=balance
    print("\n Your account is created successfully.")

def add_money(name,money):
    for key , value in accounts.items():
        if key == name :
            accounts[key]=value+money
            print("\n Updated Balance : ",accounts[key])
            break
    
    else:
        print("\n Please create your account first")

def withdraw_money(name,money):
    for key , value in accounts.items():
        if key==name and value > money :
            accounts[key]=value-money
            print("\n Updated balance is : ",accounts[key])
            break
   
    else:
        print("\n unable to find account or less balance")

def check_balance(name):
    for key , value in accounts.items():
        if key==name:
            print("\n Your current account balance is : ",accounts[key] )

if __name__ == "__main__":
    while True:
        print("Welcome to neni's bank \n")
        n= int(input("\n Choose your option \n 1. Create account \n 2. Add money \n 3. Withdraw money \n 4. Check balance \n 5. Show all acounts \n "))
        match n :
            case 1:
                add_account()
            case 2:
                name=input("\n Enter your name: ")
                money=int(input("\n Enter amount of money you want to add : "))
                add_money(name,money)
                
            case 3:
                name=input("\n Enter your name: ")
                money=int(input("\n Enter amount of money you want to withdraw : "))
                withdraw_money(name,money)
            case 4:
                name=input("\n Enter your name:")
                check_balance(name)

            case 5:
                print(accounts)

        a= int(input("\n Do you want to perform any other task : (0-no/1-yes) \n "))
        if a==0:
            break




    



