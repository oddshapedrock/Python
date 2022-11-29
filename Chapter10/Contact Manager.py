import pickle
from contact import Contact

def main():
    dic = load_contacts()
    while True:
        try:
            choice = get_menu_choice()
            paths = [look_up, add, delete, change, exit]
            paths[choice-1](dic)
            save_contats(dic)
        except:
            print("\nSomething happened an error occured, you were sent back to the menu.\n")
    
def load_contacts():
    with open("contacts.dat", "rb") as file:
        contacts = pickle.load(file)
    return contacts
    
def add(myContacts):
    
    name = input("Enter a name: ")

    phone = input("Enter a phone: ")

    email = input("Enter a email: ")


    contact = Contact(name, phone, email)
    myContacts.append(contact)
    print(contact)
    
    print("Updated...\n")
    
    
def look_up(myContacts):
    lookup = input("\nName to lookup: ")
    for contact in myContacts:
        if contact.get_name().lower() == lookup.lower():
            print(contact)
            print()
            break
    else:
        print("not found\n")

def get_menu_choice():
    while True:
        ch = input("1) lookup\n2) add\n3) delete\n4) change\n5) exit\n:: ")
        if ch.isnumeric():
            if 0 < int(ch) <= 5:
                break

    return int(ch)

def change(myContacts):
    lookup = input("\nName of account to change: ")
    for contact in myContacts:
        if contact.get_name().lower() == lookup.lower():
            phone = input("New Phone: ")
            email = input("New Email: ")
            contact.set_phone(phone)
            contact.set_email(email)
            break
    else:
        print("not found\n")

def delete(myContacts):
    lookup = input("\nName of account to delete: ")
    for contact in myContacts:
        if contact.get_name().lower() == lookup.lower():
            myContacts.remove(contact)
            print("deleted account\n")
            break
    else:
        print("not found\n")

def save_contats(myContacts):
    with open("contacts.dat", "wb") as file:
        pickle.dump(myContacts, file)


main()