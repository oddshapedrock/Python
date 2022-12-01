#CashRegister is used to create items for the inventory
#it takes three initialization arguments (items name, items quantity, items price)
class RetailItem():
    #initialize variables
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    #print message
    def __str__(self):
        return f"{self.name} | Amount: {self.quantity} | ${self.price} each"
    
    #set_quantity takes one argument (a quantity)
    #sets the items quantity to amount of argument
    #returns nothing
    def set_quantity(self, amount):
        self.quantity = amount
    
    #get_name takes no arguments
    #returns name
    def get_name(self):
        return self.name
    
    #get_quantity takes no arguments
    #returns quantity
    def get_quantity(self):
        return self.quantity
    
    #get_price takes no arguments
    #returns price
    def get_price(self):
        return self.price
    