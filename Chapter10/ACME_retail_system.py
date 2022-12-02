from RetailItem import RetailItem as RI
from CashRegister import CashRegister as CR

#file management
import pickle

#password encryption
import hashlib

#two factor
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
#----------------------------------------------------------------------------------------------------------#

#ACME_retail_system is the stores management program

#Has an inventory management system to manage the store inventory
#Has a retail system to purchase items from the inventory

#To access the retail management you will need to create and account with AccountManager.py!

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

#retail_menu takes no arguments
#displays retial menu
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
        print(f"Invalid option. Choose an option between 1 and {maxVal}.")
    print("\n")
    #returns user input offset for lists
    return int(choice) -1

#----------------------------------------------------------------------------------------------------------#
#inventory system

#load_inventory takes no arguments
#reads inventory data from file
#returns the data from the file
def load_inventory():
    #try to read from file
    try:
        with open("inventory.dat", "rb") as file:
            data = pickle.load(file)
    #try to write to file
    except Exception:
        print("File created!")
        #create file
        data  = []
        with open("inventory.dat", "wb") as file:
            pickle.dump([], file)
    #returns the inventory
    return data


#two_factor_auth takes one argument (the email recipient)
#emails the recipient the auth code
#returns the auth code
def two_factor_auth(recipient):
    #account info
    #kdjsqlfjwklfewqf@outlook.com
    #Ajkljgfalj!
    
    #generate Auth Code
    code = randint(10000, 99999)
    
    #set up server
    smtp_server = "smtp.outlook.com"
    port = 587  # For starttls
    sender_email = "kdjsqlfjwklfewqf@outlook.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        #create server
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection

        server.login(sender_email, "Ajkljgfalj!")
        
        #esmail content
        message = MIMEMultipart("alternative")
        message["Subject"] = "2 Factor Authentication"
        message["From"] = sender_email
        message["To"] = recipient
        #eamil body
        html = f"""\
            <html>
              <body>
                <p>Auth Code:<br>
                   {code}
                </p>
              </body>
            </html>
            """
        #add body to content
        content = MIMEText(html, "html")
        message.attach(content)
        
        #sent message
        server.sendmail(sender_email, recipient, message.as_string())
        
    except Exception as e:
        # Print any error messages to stdout
        print(e)
        
    finally:
        #close the server
        server.quit() 
    
    return code

#inventory_system_main takes one argument (list of inventory objects)
#calls upon inventory_system functions
#returns nothing
def inventory_system_main(inventory):
    #attempts to log in to inventory system
    accounts = load_accounts()
    log = login(accounts)
    print()
    #return if login fails
    if not log:
        print("Username or password is incorrect!")
        main()
        return
    
    #two factor authentication
    print("Generating Auth...")
    number = two_factor_auth(log)
    print(f"Auth email sent to {log}")
    auth = input("2 Factor Auth: ")
    #incorect authentication entered
    if not int(auth) == number:
        print("Authenticaion failed!")
        main()
        return
    
    print()
    #stick in inventory system until exit
    while True:
        #call function relative to user choice
        choice = get_choice(inventory_menu, 4)
        [inventory_system_display, inventory_system_add, inventory_system_save, system_exit][choice](inventory)

#inventory_system_display takes one argument (list of inventory objects)
#displayes all the items in the inventory
#outputs every item in the inventory
def inventory_system_display(inventory):
    #checks that inventory is not empty
    if len(inventory) > 0:
        #print inventory
        print("Inventory: ")
        for item in inventory:
            print(item)
        print()
    else:
        #empty inventory statement
        print("Inventory is empty\n")

#inventory_system_add takes one argument (list of inventory objects)
#adds an item to the inventory
#returns nothing
def inventory_system_add(inventory):
    #loop item creation
    while True:
        #create list of item names
        itemList = []
        for item in inventory:
            itemList.append(item.get_name())
        #user input name validation
        while True:
            name = input("Enter a name: ").lower()
            #name does not exist
            if not name in itemList:
                break
            
            print("Item with that name already exists")
        
        #quantity validation
        while True:
            quantity = input(f"Enter amount of {name} in stock: ")
            #check that it is a number
            if quantity.isnumeric():
                #check that the number is > 0
                if int(quantity) > 0:
                    break
                else:
                    print("Amount must be > 0.")
            else:
                print("Amount must be a number.")
                
        #price validation
        while True:
            price = input(f"Enter price of {name}: ")
            #checks that string with one decimal removed a float
            if price.replace(".",  "", 1).isnumeric():
                #checks that number is > 0
                if float(price) > 0:
                    break
                else:
                    print("Amount must be > 0.")
            else:
                print("Amount must be a valid number.")
        
        #creates a new item object
        item = RI(name, quantity, price)
        
        #add item object to list
        inventory.append(item)

        cont = input("Add another? (y/n) ").lower()
        if cont == "n":
            print()
            break

        print()

#inventory_system_save takes one argument (list of inventory objects)
#pickles the inventory list
#outputs to inventory.dat file
def inventory_system_save(inventory):
    with open("inventory.dat", "wb") as file:
        pickle.dump(inventory, file)
        
#----------------------------------------------------------------------------------------------------------#
#Retail Store
        
#retail_store_main takes one argument (list of inventory objects)
#calls upon retail system functions
#returns nothing
def retail_store_main(inventory):
    #create empty cart
    register = CR()
    
    #stay in retail store loop
    while True:
        choice = get_choice(retail_menu, 6)
        loop = False
        #call functions based on choice
        if choice == 1:
            inventory_system_display(inventory)
        elif choice == 2:
            retail_store_purchase(inventory, register)
        elif choice == 3:
            retail_store_clear(register)
        elif choice == 4:
            loop = retail_store_check_out(inventory, register)
        elif choice == 5:
            loop = True
        elif choice == 0:
            retail_store_cart(register)
            
        #test for loop break
        if loop:
            break

    #return to main menu
    main()

#retail_store_cart takes one argument (cash register object)
#calls the registers show cart function to display the cart
#returns nothing
def retail_store_cart(register):
    register.show_cart()

#retail_store_purchase takes two arguments (list of inventory objects, and the register object)
#adds an item from the inventory to the cart
#returns nothing
def retail_store_purchase(inventory, register):
    #display invenory
    inventory_system_display(inventory)
    
    #continue buying items until user quits 
    while True:
        #gets name of item from user
        key = input("What would you like to purchase? ")
        
        for item in inventory:
            #checks for item in inventory
            if item.get_name().lower() == key.lower():
                #attempts to add item to cart
                success = register.purchase_item(item)
                
                #if item was added to cart
                if success:
                    print(f"{key} added to the cart.")
                #item failed to be added to cart
                else:
                    print("We do not have enough of that item in stock!")
                    
                break
        else:
            print("Item not found!")
        
        #checks if user want to continue
        cont = input("Add another item? (y/n) ").lower()
        if cont == "n":
            break  
    print()

#retail_store_clear takes one argument (register object)
#emptys the cart of the register
#prints validation messagae
def retail_store_clear(register):
    register.empty()
    print("Cleared the cart!\n")

#retail_store_check_out takes two arguments (list of inventory objects, and the register object)
#removes items in cart from inventory if check out is successful
#returns true if the checkout was sucessful
def retail_store_check_out(inventory, register):
    #display items in cart
    register.show_cart()
    
    #promts user to accept checkout
    complete = input("Enter Y to complete transaction and return to main menu.\nAny other key will clear the cart.").lower()
    print()
    
    #if user accepts checkout
    if complete == "y":
        #decrease number of sold items from quantity
        #loops through every item in the cart
        #creates a new inventory to remove empty items
        newInventory = []
        
        for item in register.get_cart():
            
            #checks that item is in inventory
            if item[0] in inventory:
                #gets index of item in inventory list
                index = inventory.index(item[0])
                #gets origional quantity of item
                origional = inventory[index].get_quantity()
                #gets new quantity of item by subtracting by amount in cart
                new = int(origional) - item[1]
                
                #checks that quantity of item is now > 0
                if new > 0:
                    #resets the quantity of the item
                    inventory[index].set_quantity(new)
                    #adds the item to the new inventory
                    newInventory.append(item[0])     
        #save the new inventory to the file
        inventory_system_save(newInventory)
        #validation message
        print("Purchase complete\n")
        
        #add non cart items to new inventory
        
        
        return True
    else:
        #clear cart if user does not wish to checkout
        retail_store_clear(register)

#----------------------------------------------------------------------------------------------------------#
#passwords
        
#load_accounts takes no arguments
#reads the accounts data from file
#returns the account data
def load_accounts():
    #try to open file
    try:
        with open("accounts.dat", "rb") as file:
            accounts = pickle.load(file)
        return accounts
    #file could not be opened
    except Exception:
        print("accounts.dat not found!")

#login takes one argument (accounts data)
#asks the user for a username and password
#checks if password matches username from account data
#returns email if username and password match account data
def login(accounts):
    #user inputs
    username = input("Username: ")
    password = input("Password: ")
    
    #checks that username exits
    if username in accounts:
        #gets user info
        account = accounts[username]
        #shifts the password
        password = int(hashlib.sha1(password.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        #checks the password
        if account[0] == password:
            #successful login
            return account[1]
    #unsuccessful login
    return False

#----------------------------------------------------------------------------------------------------------#
#exit

#system_exit takes one argument (a throwaway argument for ease of coding)
#prints exit message then ends the code
#returns nothing
def system_exit(_arg):
    print("Thank you for using the ACME Retail System")
    exit()

#start code with main function
main()