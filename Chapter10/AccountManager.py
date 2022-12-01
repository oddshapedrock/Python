import pickle
from random import randint

#main takes no arguments
def main():
    #main menu
    while True:
        print("1) create account")
        print("2) delete account")
        method = input("::")
        #checks rumber is integer in range
        if method.isnumeric():
            if 0 < int(method) < 3:
                break
    print()
    
    #load the account profiles
    accounts = load_accounts()
    
    #call function based on user input
    [create_account, delete_account][int(method)-1](accounts)

#load_accounts takes no arguments
#loads the accounts from accounts.dat
#returns dictionary of accounts
def load_accounts():
    with open("accounts.dat", "rb") as file:
        accounts = pickle.load(file)
    return accounts

#create_account takes one argument (user accounts dictionary)
#gets user input username and password, hashes it and stores it to file
#returns nothing
def create_account(accounts):
    #username input
    username = input("Enter a username: ")
    
    #password authentication loop
    while True:
        password = input("Enter a password: ")
        authenticator = input("Re-enter password: ")
        #ensure password matches
        if password == authenticator:
            break
        print("\nPasswords do not match")
        
    shift = randint(1, 32)
    password = hash(password)
    
    accounts[username] = password
    save_data(accounts)

def delete_account(accounts):
    print("Accounts:")
    for account in accounts.keys():
        print(account)
    print("\nWhat would you like to delete? ")
    account = input(":: ")
    if account in accounts:
        accounts.pop(account)
        save_data(accounts)
    else:
        print("Account not found.")
    
def save_data(accounts):
    with open("accounts.dat", "wb") as file:
        pickle.dump(accounts, file)

while True:
    main()
    print()
    if input("Continue. (y/n) ").lower() == "n":
        break