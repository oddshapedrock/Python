from BankAccount import bankaccount

def main():
    stBal = input("Start Balance: ")
    savings = bankaccount(int(stBal))
    
    payCheck = input("Enter the amount of your paycheck to deposit: ")
    savings.deposit(int(payCheck))
    
    withdraw = input("Enter amount to withdraw: ")
    try:
        savings.withdraw(int(withdraw))
    except Exception as e:
        print(e)
    print(savings)
    
main()