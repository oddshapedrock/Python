class RetailItem():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __str__(self):
        return f"Name: {self.name}, Amount in stock: {self.quantity}, price: {self.price}"
    
    def set_quantity(self, amount):
        self.quantity = amount
    
    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price