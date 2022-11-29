import pickle
from RetailItem import RetailItem as RI
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
    print("4) Empty card and start over")
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
    cart = []
    while True:
        choice = get_choice(retail_menu, 6)
        #call choice
        [retail_store_cart, inventory_system_display, retail_store_purchase, retail_store_clear, retail_store_check_out, system_exit][choice](inventory)

def retail_store_cart():
    pass

def retail_store_purchase():
    pass

def retail_store_clear():
    pass

def retail_store_check_out():
    pass

#----------------------------------------------------------------------------------------------------------#
#inventory system
def load_inventory():
    with open("inventory.dat", "rb") as file:
        data = pickle.load(file)
    return data

#----------------------------------------------------------------------------------------------------------#
#exit
def system_exit(_arg):
    pass

main()