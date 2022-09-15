#<FunctionName> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>

import math
import random

# ----------------------------------------------------------------------------------------------- #
#sales_tax takes no argumetns
#calculates the sale amount
#calculates state and country tax
#calculates total tax and total sale
#returns price values
def sales_tax():
    #user sale input
    sale = float(input("Enter the sale amount: "))
    #input validation
    while sale < 0:
        print("Enter a correct value.")
        sale = float(input("Enter the sale amount: "))
    #calculate tax
    saleStateTax = stateTax(sale)
    saleCountryTax = countryTax(sale)
    #get totals
    totalTax = total(saleStateTax, saleCountryTax)
    totalSale = total(sale, totalTax)
    #call output
    printLines(sale, saleStateTax, saleCountryTax, totalTax, totalSale)
#stateTax accpets no aguments
#calculates state tax
#returns state tax
def stateTax(sale):
    STATE_TAX = .05
    saleStateTax = (sale * STATE_TAX)
    return saleStateTax
#countryTax accpets no aguments
#calculates country tax
#returns country tax
def countryTax(sale):
    COUNTRY_TAX = .025
    saleCountryTax = (sale * COUNTRY_TAX)
    return saleCountryTax
#total accpets two number arguments
#adds the two numbers
#returns the total
def total(num1, num2):
    total = num1 + num2
    return total
#printLines accepts 5 arguments
#(sale, State Tax, Country Tax, total Tax, total Sale)
#prints output lines
def printLines(sale, saleStateTax, saleCountryTax, totalTax, totalSale):
    print("Your purcase price was:\t\t", end="$")
    print(format(sale, "8.2f"))
    #state tax output
    print("Your state tax amount is:\t", end="$")
    print(format(saleStateTax, "8.2f"))
    #country tax output
    print("Your county tax amount is:\t", end="$")
    print(format(saleCountryTax, "8.2f"))
    #sale country tax output
    print("Your tax total is:\t\t", end="$")
    print(format(totalTax, "8.2f"))
    #total sale output
    print("Your total sale is:\t\t", end="$")
    print(format(totalSale, "8.2f"))
    
# ----------------------------------------------------------------------------------------------- #
#calories takes no arguments
#calls fat and carb grams
#returns calorie totals
def calories():
    #call functions
    carbs = carbGrams()
    fats = fatGrams()
    #output
    print()
    print("Here is you calorie count for the day.")
    print("You consumed", carbs, "calories of carbs.")
    print("You consumed", fats, "calories of fats.")

#carbGrams takes no arguments
#carbGrams gets user input number of carbs
#multiplies grams by 4
#returns total carb calories
def carbGrams():
    grams = int(input("How many grams of carbs did you eat? : "))
    #input validation
    while grams < 0:
        print("You must enter a positive value")
        grams = int(input("How many grams of carbs did you eat? : "))
    return grams * 4
     
#carbGrams takes no arguments
#carbGrams gets user input number of carbs
#multiplies fats by 9
#returns total carb calories
def fatGrams():
    grams = int(input("How many grams of fats did you eat? : "))
    #input validation
    while grams < 0:
        print("You must enter a positive value")
        grams = int(input("How many grams of fats did you eat? : "))
    return grams * 9

# ----------------------------------------------------------------------------------------------- #
#stadium_seating takes no arguments
#calls class functions
#calculates total ticket sales
#outputs total ticket income
def stadium_seating():
    #call functions adding to total
    total = 0
    total += classA()
    total += classB()
    total += classC()
    #output
    print()
    print("Total income from tickets is $"+ format(total, "0.2f"))
    
#classA takes no arguments
#gets the number of tickets sold in this section
#multiplies tickets by 20 to get income
#returns ticket income
def classA():
    tickets = int(input("Enter the number of class A tickets sold: "))
    #input validation
    while tickets < 0:
        print("Tickets must be 0+")
        tickets = int(input("Enter the number of class A tickets sold: "))
    return tickets * 20

#classB takes no arguments
#gets the number of tickets sold in this section
#multiplies tickets by 15 to get income
#returns ticket income
def classB():
    tickets = int(input("Enter the number of class B tickets sold: "))
    #input validation
    while tickets < 0:
        print("Tickets must be 0+")
        tickets = int(input("Enter the number of class B tickets sold: "))
    return tickets * 15

#classC takes no arguments
#gets the number of tickets sold in this section
#multiplies tickets by 10 to get income
#returns ticket income
def classC():
    tickets = int(input("Enter the number of class C tickets sold: "))
    #input validation
    while tickets < 0:
        print("Tickets must be 0+")
        tickets = int(input("Enter the number of class C tickets sold: "))
    return tickets * 10
    
# ----------------------------------------------------------------------------------------------- #
#paint_estimator takes no arguments
#calls functions
#prints output summary of job
def paint_estimator():
    #call functions and assign variables
    sqFT = roomSize()
    hoursCost, gallons = getQuantity(sqFT)
    paintPrice = paintCost(gallons)
    #output
    print("\nThe cost breakdown to paint", format(sqFT, "0.1f"), "square feet is:")
    print("----------------------------------------------------")
    print("Total cost of paint: $"+format(paintPrice, "0.2f"))
    print("Total labor cost: $"+format(hoursCost, "0.2f"))
    print("The total cost of the job is: $"+ format(hoursCost + paintPrice, "0.2f"))
#roomSize takes no arguments
#gets the size of the room
#returns the size of the room
def roomSize():
    roomSize = int(input("What is the square footage to be painted? : "))
    #input validation
    while roomSize < 0:
        roomSize = int(input("Enter a valid square footage to be painted? : "))
    return roomSize
#getQuantity takes one argument (Square footage)
#calculates the total hours need work
#calculates the price of those total hours
#calculates the total gallons of paint required
#returns (cost of labor, gallons of paint needed)
def getQuantity(sqFT):
    hoursTotal = (sqFT / 112) * 8
    hoursCost = hoursTotal * 35
    paintTotal = math.ceil(sqFT / 112)
    return hoursCost, paintTotal
#paintCost takes one argument (gallons of paint)
#gets the cost of paint per gallon
#calculates the total cost of paint
#returns cost of paint
def paintCost(amount):
    price = int(input("How much is each gallon of paint? : "))
    #input validation
    while price < 0:
        price = int(input("Enter a valid price for each gallon of paint? : "))
    return price * amount

# ----------------------------------------------------------------------------------------------- #
def math_quiz():
    
def generateNumberSet():
    num1 = math.randint(1, 200)
    num2 = math.randint(1, 200)
    total = num1 + num2
    return num1, num2, total