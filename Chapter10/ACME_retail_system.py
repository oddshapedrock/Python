import pickle
from RetailItem import RetailItem as RI
from CashRegister import CashRegister as CR
#----------------------------------------------------------------------------------------------------------#
#menu system

#main menu takes no arguments
#directs user to correct place
#returns nothing
def main():
    choice = get_choice(main_menu, 2)
    #load inventory
    inventory = load_inventory()
    #call choice
    [inventory_system_main, retail_store_main][choice](inventory)
    
    
#main menu takes no arguments
#displays main menu
def main_menu():
    print("What would you like to use?")
    print("1) Inventory Control System")
    print("2) Retail Store")

#inventory menu takes no arguments
#displays inventory menu
def inventory_menu():
    print("What would you like to use?")
    print("1) Display inventory")
    print("2) Add inventory")
    print("3) Save inventory")
    print("4) Exit")

def retail_menu():
    print("Choose an option")
    print("1) View cart")
    print("2) Display items for sale")
    print("3) Purchase item")
    print("4) Empty cart and start over")
    print("5) Check out")
    print("6) Exit to main menu")

#get_choice takes two arguments (menu to display, max value in menu)
#calls the menu to display and promts user for choice
#returns user choice as and integer if it meets input validation
def get_choice(menu, maxVal):
    #display menu
    menu()
    #input validation loop
    while True:
        choice = input(":: ")
        if choice.isnumeric():
            #checks input is within value range
            if 0 < int(choice) <= maxVal:
                break
    #returns user input offset for lists
    return int(choice) -1

#----------------------------------------------------------------------------------------------------------#
#inventory system

def inventory_system_main(inventory):
    while True:
        choice = get_choice(inventory_menu, 4)
        #call choice
        [inventory_system_display, inventory_system_add, inventory_system_save, system_exit][choice](inventory)

def inventory_system_display(inventory):
    if len(inventory) > 0:
        for item in inventory:
            print(item)
    else:
        print("Inventory is empty")

def inventory_system_add(inventory):
    #create item
    name = input("Enter a name: ")
    #quantity validation
    while True:
        quantity = input(f"Enter amount of {name} in stock: ")
        if quantity.isnumeric():
            if int(quantity) > 0:
                break
            else:
                print("Amount must be > 0.")
        else:
            print("Amount must be a number.")
    #price validation
    while True:
        price = input(f"Enter price of {name}: ")
        if price.replace(".",  "", 1).isnumeric():
            if float(price) > 0:
                break
            else:
                print("Amount must be > 0.")
        else:
            print("Amount must be a valid number.")
    
    item = RI(name, quantity, price)
    inventory.append(item)

def inventory_system_save(inventory):
    with open("inventory.dat", "wb") as file:
        pickle.dump(inventory, file)
#----------------------------------------------------------------------------------------------------------#
#Retail Store

def retail_store_main(inventory):
    #create empty cart
    register = CR()
    while True:
        choice = get_choice(retail_menu, 6)
        #call choice
        loop = False
        if choice == 1:
            inventory_system_display(inventory)
        elif choice == 2:
            retail_store_purchase(inventory, register)
        elif choice == 3:
            retail_store_clear(register)
        elif choice == 4:
            loop = retail_store_check_out(inventory, register)
        elif choice == 5:
            loop = retail_system_exit(register)
        elif choice == 0:
            retail_store_cart(register)
        #test for loop break
        if loop:
            break
    main()

def retail_store_cart(register):
    register.show_cart()

def retail_store_purchase(inventory, register):
    while True:
        key = input("What would you like to purchase? ")
        for item in inventory:
            if item.get_name().lower() == key.lower():
                success = register.purchase_item(item)
                if success:
                    print(f"{key} have been added to the cart.")
                else:
                    print("We do not have enough of that item in stock!")
                break
        else:
            print("Item not found!")
        cont = input("Add another item? (y/n) ").lower()
        if cont == "n":
            break

def retail_store_clear(register):
    register.empty()
    print("Cleared the cart!")

def retail_store_check_out(inventory, register):
    register.show_cart()
    complete = input("Enter Y to complete transaction and return to main menu.\nAny other key will clear the cart.").lower()
    
    #remove from quantity
    for item in register.get_cart():
        newInventory = []
        if item[0] in inventory:
            index = inventory.index(item[0])
            origional = inventory[index].get_quantity()
            new = int(origional) - item[1]
            if new > 0:
                inventory[index].set_quantity(new)
                newInventory.append(item[0])
                
        inventory_system_save(newInventory)
        
    if complete == "y":
        print("Purchase complete")
        return True
    else:
        retail_store_clear(register)

#----------------------------------------------------------------------------------------------------------#
#inventory system
def load_inventory():
    with open("inventory.dat", "rb") as file:
        data = pickle.load(file)
    return data

#----------------------------------------------------------------------------------------------------------#
#exit

def retail_system_exit(_arg):
    return True

def system_exit(_arg):
    print("Thank you for using the ACME Retail System")
    exit()

main()