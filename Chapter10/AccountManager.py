import pickle
from random import randint

def main():
    while True:
        print("1) create account")
        print("2) delete account")
        method = input("::")
        if method.isnumeric():
            if 0 < int(method) < 3:
                break
    
    print()
    accounts = load_accounts()
    [create_account, delete_account][int(method)-1](accounts)

def load_accounts():
    with open("accounts.dat", "rb") as file:
        accounts = pickle.load(file)
    return accounts

def cypher(string, shift):
    shifted_string = ""
    alphabet = [*"abdefhijkmnoprsuvyz023568!"]
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    for letter in string:
        index = shifted_alphabet.index(letter)
        shifted_string += alphabet[index]
    return shifted_string

def create_account(accounts):
    username = input("Enter a username: ").lower()
    while True:
        password = input("Enter a password: ").lower()
        authenticator = input("Re-enter password: ").lower()
        if password == authenticator:
            break
        print("\nPasswords do not match")
        
    shift = randint(1, 25)
    password = cypher(password, shift)
    
    accounts[username] = [password, shift]
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