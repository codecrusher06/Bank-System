def create_acc(accounts):
    user_id=input("Enter Account number: ")
    if user_id in accounts:
        print("User already exists ")
        return
    password= int(input("Please set a Password: "))
    name=input("Enter your Name: ")
    bal= float(input("Enter Your Initial Balance: "))
    accounts[user_id]={"password":password,"name":name ,"balance":bal}
    print("Account created successfully!")
   
def save_data(accounts):
    with open("bankdb.txt","w")as file:
        for user_id,info in accounts.items():
            file.write(f"{user_id},{info['password']},{info['name']},{info['balance']}\n") 

def deposit(accounts,user_id):
    amt=float(input("Enter the amount to deposit: "))
    
    if amt > 0 :
        accounts[user_id]['balance']+=amt
        print(f"New Balance : {accounts[user_id]['balance']}") 
    else:
        print("Error: Deposits Amount should be positive")

def withdraw(accounts,user_id):
    amt=float(input("Enter the amount to withdraw: "))
    if amt > accounts[user_id]['balance']:
        print("Error: Insufficient funds !")
    elif amt > 0:
        accounts[user_id]['balance']-=amt
        print(f"New balance: {accounts[user_id]['balance']}")
    else:
        print("Error: Amount must be positive") 
        
def transfer(accounts,sender_id):
    receiver_id=input("Enter Receivers Id: ")
    if receiver_id not in accounts:
        print("Error:Recipient not found")
        return
    transfer_amt=float(input("Enter amount to transfer"))
    if transfer_amt <= 0:
        print("Invalid Amount!!")
        return
    if accounts[sender_id]['balance']>=transfer_amt:
        accounts[sender_id]['balance']-=transfer_amt
        accounts[receiver_id]['balance']+=transfer_amt
        print("Transfer Successfully!!!")
    else:
        print("Insufficient funds! ")

def check_bal(accounts,user_id):
    print("your Account Balance: ",accounts[user_id]['balance'])
                         
def load_data():
    accounts={}
    try:
        with open("bankdb.txt","r")as file:
            for line in file :
                parts = line.strip().split(",")
                if len(parts)==4:
                    u_id,u_pw,u_name,u_bal=parts
                    accounts[u_id]={"password":int(u_pw),"name":u_name ,"balance":float(u_bal)}
    except FileNotFoundError:
        print("Error:File not Exsits")
        return{}
    return accounts

def authentication(accounts):
    user_id = input("Enter Account Number: ")
    if user_id in accounts:
        attempt = 3
        while attempt > 0:
            try:
                password=int(input("please enter the password: "))
                if accounts[user_id]['password'] == password:
                      print(f"Welcome {accounts[user_id]['name']}! ")
                      return user_id
                else:
                    attempt-=1
                    print("Invalid Password")
            except ValueError:
                print("Please enter Numbers for password")
        print("Too many failed attempts")
        return None
    else:
        print("Account not fount.")
        return None

def main():
    accounts=load_data()
    while True:
            print("---Welcome to Kuber Bank---")
            print("1. Create Accoount")
            print("2. Login") 
            print("3. Exit")
            choice=input("Enter the choice: ")
            if choice =="1":
                create_acc(accounts)
                save_data(accounts)
            elif choice == "2":
                 user=authentication(accounts)
                 if user:
                     while True:
                         print(f"\n[{accounts[user]['name']}'s Session]")
                         print("1. Deposit")
                         print("2. Withdraw")
                         print("3.Transfer")
                         print("4.Check Balance")
                         print("5. Exit")
                         act=input("Select: ")
                         if act == "1": deposit(accounts, user)
                         elif act == "2": withdraw(accounts, user)
                         elif act == "3": transfer(accounts, user)
                         elif act == "4": check_bal(accounts,user)
                         elif act == "5": break
                         else: print("Invalid Input")
                         save_data(accounts)
            elif choice == "3":
                print("Thank you !!")
                break
            
            
if __name__=="__main__":
    main()
    
