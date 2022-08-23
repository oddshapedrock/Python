import turtle as tur
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

#cookie_monster accepts no arguments
#calculates the needed ingredients based on the amount of cookies
#returns amount of each ingredient in cups and oz
def cookie_monster():
    #prompt for cookie amount
    cookieAmount = float(input("How many cookies do you want to make? : "))
    cookieCups = []
    cookieOz = []
    #amount per cookie
    COOKIE = [.5, .3333, .9166] #[sugar butter flour]
    #loops through cookie multiplies each number by cookie amount then divides into cups and oz
    for ingredient in COOKIE:
        ingredient = ingredient * cookieAmount
        cookieCups.append(int(format(ingredient, ".0f")) // 8)
        cookieOz.append(int(format(ingredient, ".0f")) % 8)

    #sugar
    sugarCups = cookieCups[0]
    sugarOz = cookieOz[0]
    #butter
    butterCups = cookieCups[1]
    butterOz = cookieOz[1]
    #flour
    flourCups = cookieCups[2]
    flourOz = cookieOz[2]

    #outpur amounts 
    print("For", cookieAmount, "cookies you will need:")
    print(sugarCups, "cup(s)", sugarOz, "ounces of suggar.")
    print(butterCups, "cup(s)", butterOz, "ounces of butter")
    print(flourCups, "cup(s)", flourOz, "ounces of flour")

#class_demographics accepts no arguments
#takes the famales and males to calculate thier percentages
#returns the percentages of the class demographics
def class_demographics():
    females = float(input("Enter the number of females: "))
    males = float(input("Enter the number of Males: "))
    total = males + females
    malePercent = format(males / total * 100, "0.0f")
    femalePercent = format(females / total * 100, "0.0f")
    print("The class consists of", femalePercent +  "% females and", malePercent + "% males.")

#tortuga_1 accepts no arguments
#makes a compas
#returns image of compas
def tortuga_1():
    #setup
    tur.setup(500, 500)
    tur.hideturtle()
    tur.pensize(4)
    
    def flip():
        tur.left(180)
    def orgin():
        tur.goto(0, 0)
    #creates line through origin with distance argument
    def line(dist):
        orgin()
        tur.forward(dist)
        orgin()
        flip()
        tur.forward(dist)
        flip()
    
    #writes given letter at given location
    def letter(loc, letter):
        tur.goto(loc)
        tur.write(letter, font=("arial", 16))
    
    #biglines
    line(100)
    tur.setheading(90)
    line(100)
    #smalllines
    tur.setheading(45)
    tur.pensize(2)
    line(70)
    tur.setheading(135)
    line(70)
    
    #writes the letters
    tur.penup()
    letter((-6, 105), "N")
    letter((-6, -127), "S")
    letter((110, -10), "E")
    letter((-125, -10), "W")
    
    
    tur.done()

#tortuga_2 accepts no arguments
#draws house
#returns image of house
def tortuga_2():
    #setup
    tur.setup(800, 800)
    tur.hideturtle()
    tur.pensize(4)
    
    #square
    tur.color('black', 'red')
    tur.begin_fill()
    tur.penup()
    tur.goto(50*3, 50*3)
    tur.pendown()
    tur.goto(-50*3, 50*3)
    tur.goto(-50*3, -70*3)
    tur.goto(50*3, -70*3)
    tur.goto(50*3, 50*3)
    tur.end_fill()
    
    #trapazoid
    tur.begin_fill()
    tur.goto(130*3, 30*3)
    tur.goto(130*3, -50*3)
    tur.goto(50*3, -70*3)
    tur.end_fill()
    
    #roof triangle
    tur.color('black', '#964B00')
    tur.penup()
    tur.goto(50*3, 50*3)
    tur.pendown()
    tur.begin_fill()
    tur.goto(0*3, 110*3)
    tur.goto(-50*3, 50*3)
    tur.end_fill()
    
    #roof end
    tur.begin_fill()
    tur.goto(0*3, 110*3)
    tur.goto(105*3, 60*3)
    tur.goto(130*3, 30*3)
    tur.goto(50*3, 50*3)
    tur.goto(0*3, 110*3)
    tur.end_fill()
    
    tur.done()
    
#tortuga_3 accepts no arguments
#olympics logo
#returns image of olympics logo
#just trying to get it as close as possible including space gaps
def tortuga_3():
    tur.setup(500,500)
    tur.hideturtle()
    tur.pensize(8)
    tur.speed(0)
    tur.goto(0, 0)
    
    #makes a skip space slightly wider than the line width
    def skip():
        tur.penup()
        tur.circle(50, 30)
        tur.pendown()
    #middle black circle
    skip()
    tur.circle(50, 230)
    skip()
    tur.circle(50, 70)
    #move to spot for green circle
    tur.penup()
    tur.goto(60, -50)
    tur.pendown()
    #color to green and draw green circle
    tur.color("#179a13")
    tur.circle(50, 75)
    skip()
    tur.circle(50, 75)
    skip()
    tur.circle(50, 180)
    #move to red circle spot
    tur.penup()
    tur.goto(140, 7)
    tur.pendown()
    #set color to red and draw red circle
    tur.color("red")
    tur.circle(50, 225)
    skip()
    tur.circle(50, 180)
    #move to spot for yellow circle
    tur.penup()
    tur.goto(-10, 10)
    tur.pendown()
    #collor to yellow and draw yellow circle
    tur.color("#ffce01")
    skip()
    tur.circle(50, 50)
    skip()
    tur.circle(50, 225)
    skip()
    tur.circle(50, 23)
    #move to blue circle spot
    tur.penup()
    tur.goto(-85, 83)
    tur.pendown()
    #color to blue and draw blue circle
    tur.color("#3e76ec")
    tur.circle(50, 230)
    skip()
    tur.circle(50, 97)
    
    tur.done()