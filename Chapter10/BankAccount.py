class BankAccount():
    def __init__(self, bal):
        self._balance = bal
    
    def __str__(self):
        return "The balance is $" + format(self.__balance, ",.2f")
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise Exception("Insufficient: funds")
        
    def get_balance(self):
        return self.__balance
    
bankaccount = BankAccount