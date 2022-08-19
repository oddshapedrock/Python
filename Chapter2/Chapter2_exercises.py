#personal_info accepts no arguments
#it prints out personal information
#returns my personal information
def personal_info():
    print("Aaron Hamor")
    print("2421 E Summerwood Cir, Goddard KS, 67052")
    print("316-640-2227")
    print("Computer science")

#total_purchase accepts no arguments
#it takes five prices totals them up and adds tax
#returns subtotal, tax, and total
def total_purchase():
    #user price inputs
    price1 = float(input("Please enter a price for your first item: "))
    price2 = float(input("Please enter a price for your second item: "))
    price3 = float(input("Please enter a price for your third item: "))
    price4 = float(input("Please enter a price for your fourth item: "))
    price5 = float(input("Please enter a price for your fifth item: "))
    #newline
    print()
    #adds the prices outputs subtotal
    total = price1 + price2 + price3 + price4 + price5
    print("Subtotal: ", end="\t$  ")
    print(format(total, ".2f"))
    #adds 7% tax and outputs tax
    tax = total*.07
    print("Tax:", end="\t\t$   ")
    print(format(tax, ".2f"))
    #adds tax to subtotal
    total += tax
    print("Total:", end="\t\t$  ")
    print(format(total, ".2f"))
    
#distance_traveled accepts no arguments
#it takes the user speed and calculates the distance at three different times
#returns distance after 6 10 and 15 hours
def distance_traveled():
    #user speed input
    speed = int(input("How fast are you driving? : "))
    #6 hours
    distance = speed * 6 #speed * hours
    print("At", speed, "you will travel", distance, "miles in 6 hours")
    #10 hours
    distance = speed * 10 #speed * hours
    print("At", speed, "you will travel", distance, "miles in 10 hours")
    #15 hours
    distance = speed * 15 #speed * hours
    print("At", speed, "you will travel", distance, "miles in 15 hours")
    
#sales_tax accepts no arguments
#computes the state and country sales tax
#returns purchase price, state tax total, sales tax total, total tax, and total sale
def sales_tax():
    #tax rates
    COUNTRY_TAX = .025
    STATE_TAX = .05
    #user sale input
    sale = float(input("Enter the sale amount: "))
    #calculate tax
    saleStateTax = (sale * STATE_TAX)
    saleCountryTax = (sale * COUNTRY_TAX)
    #total tax
    totalTax = (saleStateTax + saleCountryTax)
    #add tax to sale total
    totalSale = sale + totalTax
    #purchase price output
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

#tip_tax_total accepts no arguments
#computes the tax and tip with the bill
#returns the purchase price the tip amount the sales tax and the total
def tip_tax_total():
    #18% tip and 7% tax
    TIP = .18
    SALES_TAX = .07
    #user sale input
    sale = float(input("Enter the sale amount: "))
    #calculate tax & tip
    tipAmount = (sale * TIP)
    taxAmount = (sale * SALES_TAX)
    #add tax and tip to sale total
    totalSale = sale + tipAmount + taxAmount
    #purchase price output
    print("The sale was:\t\t\t", end="$")
    print(format(sale, "8.2f"))
    #total tax output
    print("The tip amount is:\t\t", end="$")
    print(format(tipAmount, "8.2f"))
    #sales tax output
    print("The sales tax amount is:\t", end="$")
    print(format(taxAmount, "8.2f"))
    #total sale output
    print("The total bill is:\t\t", end="$")
    print(format(totalSale, "8.2f"))
   
#temp_converter accepts no arguments
#converts temps from celsius to fahrenheit
#returns fahrenheit calculation
def temp_converter():
    #user temperature input
    tempCelsius = float(input("Please enter the degrees Celsius: "))
    
    #fahrenheit to celsius formula
    fahrenheit = str(((9 / 5) * tempCelsius) + 32)
    
    #output fahrenheit
    print(format(tempCelsius, ".0f"), "degrees celsius is", fahrenheit, "degrees fahrenheit")
    
def cookie_monster():
    #prompt for cookie amount
    cookieAmount = float(input("How many cookies do you want to make? : "))
    cookieCups = []
    cookieOz = []
    #amount per cookie
    COOKIE = [.5, .3333, .9166]
    for ingredient in COOKIE:
        ingredient = ingredient * cookieAmount
        cookieCups.append(int(format(ingredient, ".0f")) // 8)
        cookieOz.append(int(format(ingredient, ".0f")) % 8)

    sugarCups = cookieCups[0]
    sugarOz = cookieOz[0]
    
    butterCups = cookieCups[1]
    butterOz = cookieOz[1]
    
    flourCups = cookieCups[2]
    flourOz = cookieOz[2]

    print(COOKIE, sugarCups)