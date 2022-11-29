class CellPhone():
    def __init__(self, manufacturer, model, price):
        self.manu = manufacturer
        self.model = model
        self.price = price
        
    def __str__(self):
        return f"\nManufacturer: {self.manu}\nModel: {self.model}\nRetail price: {self.price}"
    
    def set_manufact(self, manufacturer):
        self.manu = manufacturer
        
    def set_model(self, model):
        self.model = model
        
    def set_retail_price(self, price):
        self.price = price
        
    def get_menufact(self):
        return self.manu
    
    def get_model(self):
        return self.model
    
    def get_retail_price(self):
        return self.model

cellphone = CellPhone