#CashRegister is used to manage purchases
#it takes zero initialization arguments
class CashRegister():
    #initialize variables
    def __init__(self):
        self.itemList = []
        self.cart = []
        self.total = 0

    #purchase_items takes one argument (the item to purches)
    #handles the values of the items in the cart
    #returns true if purchase was successful
    def purchase_item(self, RetailItem):
        #checks if item is not already in cart
        if not RetailItem.get_name() in self.itemList:
            #add name of item to item list for checking
            self.itemList.append(RetailItem.get_name())
            #adds teh item to the cart
            self.cart.append([RetailItem, 1, float(RetailItem.get_price())])
            #increases the total by the price
            self.total += float(RetailItem.get_price())
        
        #item is already in cart
        else:
            #gets index of item
            index = self.itemList.index(RetailItem.get_name())
            #ensures enough inventory is in stock
            if self.cart[index][1] < int(RetailItem.get_quantity()):
                #increases the quantity of the item in the card
                self.cart[index][1] += 1
                #increases the total price of item category
                self.cart[index][2] += float(RetailItem.get_price())
                #increases total price
                self.total += float(RetailItem.get_price())
            else:
                #purchase insuccessful
                return False
        #purchase sucessful
        return True
    
    #get_total takes no arguments
    #returns total
    def get_total(self):
        return self.total
    
    #show_cart takes no arguments
    #displays the contents of the cart
    #outputs the items of the cart
    def show_cart(self):
        #checks if cart is empty
        if len(self.cart) > 0:
            #prints every item in the cart
            for item in self.cart:
                print(f"{item[0].get_name()} <-----> {item[2]}")
            #prints the total of the cart
            print(f"\nTotal: {self.total}")
        else:
            print("Cart is currently empty\n")
          
    #get_cart takes no arguments
    #returns the cart
    def get_cart(self):
        return self.cart
    
    #empty takes no arguments
    #resets the CashRegister object cart
    #returns nothing
    def empty(self):
        self.itemList = []
        self.cart = []
        self.total = 0
        