import pickle
from random import randint

#main takes no arguments
#directs user to create or delete account functions
#returns nothing
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
        
    #hash the password
    password = hash(password)
    #save account to accounts dictionary
    accounts[username] = password
    #write data to file
    save_data(accounts)

#delete_account takes one argument (user accounts dictionary)
#deletes a users account
#returns nothing
def delete_account(accounts):
    #display accounts
    print("Accounts:")
    for account in accounts.keys():
        print(account)
    
    #get account to delete
    print("\nWhat would you like to delete? ")
    account = input(":: ")
    
    #ensure user input account exitst
    if account in accounts:
        #delete the account and resave the file
        accounts.pop(account)
        save_data(accounts)
    else:
        print("Account not found.")

#save_data takes one argument (user accounts object)
#saves the account data to the accounts.dat file
#output data to the file
def save_data(accounts):
    with open("accounts.dat", "wb") as file:
        pickle.dump(accounts, file)
        
#continuation loop
while True:
    main()
    print()
    #prompt user to continue
    if input("Continue. (y/n) ").lower() == "n":
        break