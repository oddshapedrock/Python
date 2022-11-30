class CashRegister():
    def __init__(self):
        self.itemList = []
        self.cart = []
        self.total = 0

    def purchase_item(self, RetailItem):
        if not RetailItem.get_name() in self.itemList:
            self.itemList.append(RetailItem.get_name())
            self.cart.append([RetailItem, 1, float(RetailItem.get_price())])
            self.total += float(RetailItem.get_price())
        else:
            index = self.itemList.index(RetailItem.get_name())
            if self.cart[index][1] < int(RetailItem.get_quantity()):
                self.cart[index][1] += 1
                self.cart[index][2] += float(RetailItem.get_price())
                self.total += float(RetailItem.get_price())
            else:
                return False
        return True
    
    def get_total(self):
        return self.total
    
    def show_cart(self):
        if len(self.cart) > 0:
            for item in self.cart:
                print(f"{item[0].get_name()} <-----> {item[2]}")
            print(f"Total: {self.total}")
        else:
            print("Cart is currently empty")
            
    def get_cart(self):
        return self.cart
    
    def empty(self):
        self.itemList = []
        self.cart = []
        self.total = 0