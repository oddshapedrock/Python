import turtle

def comment_example():
    #comment_example recieves no arguments
    #it explains how to create a function header
    #and outputs or returns "Hello World!"
    print("hello world")
    
def program2_1():
    #program 2 1 recieves no arguments
    #it outputs three messages using apostrophies
    print ('Kate Austen')
    print ('123 Full Cirlce Drive')
    print ('Asheville, NC 2899')
    
def program2_2():
    #program 2 2 recieves no arguments
    #it outputs three messages using double quotes
    print ("Kate Austen")
    print ("123 Full Cirlce Drive")
    print ("Asheville, NC 2899")
    
def program2_3():
    #program 2 3 recieves no arguments
    #displays a simple string
    print ("Don't fear!")
    print ("I'm Here!")
    
def program2_4():
    #program 2 3 recieves no arguments
    #displays a simple string
    print('Your assignment is to read "Hamlet" by tomorrow')
    
def program2_5():
    #program 2 6 recieves no arguments
    #it outputs three messages using apostrophies
    #This function displays a person's name and address
    print ('Kate Austen')
    print ('123 Full Cirlce Drive')
    print ('Asheville, NC 2899')
    
def program2_6():
    #program 2 6 recieves no arguments
    #it outputs three messages using apostrophies
    #This function displays a person's name and address
    
    #Display the Name
    print ('Kate Austen')
    #Display the Address
    print ('123 Full Cirlce Drive')
    #Display the city, state, and ZIP
    print ('Asheville, NC 2899')
    
def program2_7():
    #program 2 7 recieves no arguments
    #it outputs a string containing a variable
    room = "503"
    print("I am staying in room\n#" + room)
    
def program2_8():
    #program 2 8 recieves no arguments
    #outputs a string containing two variables
    top_speed = "160"
    distance = "300"
    #Display Message
    print("The top speed is\n"
          + top_speed +
          "\nThe distance traveled is\n"
          + distance)
    
def program2_9():
    #program 2 9 recieves no arguments
    #it outputs a string containing a variable
    room = "503"
    print("I am staying in room", "#"+room)

def program2_10():
    #program 2 10 recieves no arguments
    #it outputs 2 strings with a varibable that changes
    dollars = "2.70"
    print("I have", dollars, "in my account.")
    #reassigning of value
    dollars = "99.95"
    print("But now I have", dollars, "in my account!")
    
def program2_11():
    #program 2 11 recieves no arguments
    #uses variables to output a full name
    firstName = "Kathryn"
    lastName = "Marino"
    print(firstName + " " + lastName)

def program2_12():
    #program 2 11 recieves no arguments
    #prompts user for two values and outputs them in string
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("Hello", first_name, last_name)
    
def program2_13():
    #program 2 13 recieves no arguments
    #takes user input to display name age and income
    userName = input("What is your name? : ")
    userAge = int(input("What is your age? : "))
    userIncome = float(input("What is your income? : "))
    print ("Here is what you entered:\n"
           + "Name:", userName
           + "\nAge:", userAge,
            "\nIncome:", userIncome)

def program2_14():
    #program 2 14 revieves no arguments
    #adds the values of two variables to create output of 3700
    salary = 2500
    bonus = 1200
    pay = salary + bonus
    print("Your pay is", pay)
    
def program2_15():
    #program 2 15 revieves no arguments
    #Gets origional price and take 20% off
    price = float(input("Origional Price : "))
    #knocks 20% off
    price -= (price * .2)
    print("The sale price is", price)
    
def program2_16():
    #program 2 16 revieves no arguments
    #gets score 1
    testScore1 = float(input("Enter test score 1 : "))
    #adds score 2 to score 1
    testScore2 = testScore1 + float(input("Enter test score 2 : "))
    #adds score 3 to the first score then divides by three
    average = (testScore2 + float(input("Enter test score 3 : "))) / 3
    
    #output avarage
    print("Average score is : ", average)
    
def program2_17():
    #program 2 17 recieves no arguments
    #input seconds
    inputTime = float(input("Enter the number of seconds: "))
    #calculations
    hours = inputTime // 3600
    minutes = (inputTime // 60) % 60
    seconds = inputTime % 60
    #output
    print("Here is the time in hours, minutes, and seconds:",
    "\nHours: ", hours,
    "\nMinutes: ", minutes,
    "\nSeconds: ", seconds)
    
def program2_18():
    #program 2 18 recieves no arguments
    #creates variable and prompts for desired amount
    deposit = (float(input("Enter the desired future value: "))
    #divides by (1 + input intrest rate) ^ #of years 
    / (1 + float(input("Enter the annual interest rate: ")))
    ** float(input("Enter the number of years: ")))
    #output formated to two decimal places
    print("You will need to deposit: $" + str(format(deposit, ".2f")))
    
def program2_19():
    #program 2 19 recieves no arguments
    #math stuff
    amountDue = 5000
    monthlyPayment = amountDue / 12
    #output
    print("monthly payment is: ", monthlyPayment)
    
def program2_20():
    #program 2 20 recieves no arguments
    #math stuff
    amountDue = 5000
    monthlyPayment = amountDue / 12
    #output
    print("monthly payment is: ", end="$")
    print(format(monthlyPayment, ".2f"))
    
def program2_22():
    #program 2 21 recieves no arguments
    num1 = 127.90
    num2 = 3465.15
    num3 = 3.78
    num4 = 264.82
    num5 = 88.08
    num6 = 800.00
    print(format(num1, "7.2f"),
          format(num2, "7.2f"),
          format(num3, "7.2f"),
          format(num4, "7.2f"),
          format(num5, "7.2f"),
          format(num6, "7.2f"), sep="\n")
    