account = {}

def create_account():
    
    ac_no = input("Enter Account Number: ")
    if ac_no in account:
        print("Already exists")
        return
    name = input("Enter the Applicant Name: ")
    balance = float(input("Enter initial Balance: "))

    account[ac_no] = {
        "Account no": ac_no,
        "Account Holder": name,
        "Current Balance": balance,
    }
    print("Account has been created successfully!..")
    
def Deposit_money():
    c = input("Enter Account number: ")
    if c in account:
        d = account[c]  
        money = float(input("Enter money to deposit: "))
        d["Current Balance"] += money  
        print("Money deposited successfully")
        print(f"The current balance in your account is {d['Current Balance']}")
    else:
        print("Account not found")
        
def withdraw():
    c = input("Enter Account number: ")
    if c in account:
        d = account[c]  
        money = float(input("Enter money to withdraw: "))
        if money > d["Current Balance"]:
            print("Insufficient funds")
        else:
            d["Current Balance"] -= money  
            print("Money withdrawal successfully")
            print(f"The current balance is {d['Current Balance']}")
    else:
        print("Account not found")

def check():
    c = input("Enter Account number: ")
    if c in account:
        d = account[c]  
        print("\n--- Account Details ---")
        print("Account Number: ", c)
        print("Account Holder: ", d["Account Holder"])
        print("Current Balance:", d["Current Balance"])
    else:
        print("Account not found")

while True:
    print("\n===Bank Account management===")
    print("1. Deposit Money")
    print("2. Withdrawal Money")
    print("3. Check Balance")
    print("4. Create Account")
    print("5. Exit")
    choice = input("Enter the choice to perform: ")
    
    if choice == '1':
        Deposit_money()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        check()
    elif choice == '4':
        create_account()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print('Invalid choice')
