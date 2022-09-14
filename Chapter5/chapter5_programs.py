from random import randint as random
import turtle
from math import sqrt, hypot
import circle
import rectangle
import my_graphics as graph

#message accepts no arguments
#prints line I am iron man
def message():
    print("I am Iron Man")
    
#main_5_2 accepts no arguments
#prints some text stuff
def main_5_2():
    print("I am invitable.")
    message()
    print("Only one way to win...")
    
#acme_dryer accepts no arguments
#validate input 1-5
def acme_dryer():
    print("Hello welcome to the acme dryer help center.")
    step = int(input("Enter a step# to contincue or 0 to exit. : "))
    #input validation
    while step < 0 or step > 5:
        print()
        print("invalid! Enter a number 0-5")
        step = int(input("Enter a step# to contincue or 0 to exit. : "))
    
    #makes a list of steps as strings    
    stepList = [step0(), step1(), step2(), step3(), step4(), step5()]
    #prints step
    print(stepList[step])
    #checks if to continue
    if step == 0:
        return
    else:
        print()
        acme_dryer()
    
#returns speciftic stings of text corospinding with a step
def step1():
    return "Unplug the dryer and move it away from the wall."
def step2():
    return "Remove the six screws from the back of the dryer"
def step3():
    return "Remove the back panel"
def step4():
    return "Pull the top of the dryer strait up."
def step5():
    return "Pull the front of the dryer off"
def step0():
    return "Goodbye"
    
    
#badscope accepts no arguments
#it ccalls procedure get_name() to get a name
def bad_scope():
    get_name()
    print("Hello", name)
    
def get_name():
    name = input("Enter your name: ")
# -------------------------------------------------------------------------
#brid calculator calls texas then cansas
def bird_calculator():
    texas()
    kansas()
    
def texas():
    birds = 5000
    print("Texas has", birds, "birds")
    
def kansas():
    birds = 8000
    print("Kansas has", birds, "birds")
# ----------------------------------------------------------------------------    
    
def pass_arg():
    value = 5
    show_double(value)
    
def show_double(value):
    print(value * 2)

# ---------------------------------------------------------------------
def volume_conversion():
    #accepts no args
    #clls intro
    #prompts for cups
    #calls cums to oz
    intro()
    cups = int(input("Enter a number of cups: "))
    cups_to_oz(cups)
    
def intro():
    #takes no args
    #print text
    print("Welcome to the cups to fluid ounces conversion program.\n" +
          "For your reference, 1 cup = 8 fluid oz.")
    print()
    
def cups_to_oz(cups):
    #takes on argument a value for cups
    #prints text
    print()
    print(cups, "cup(s) is equal to", cups * 8, "fluid ounces.")

# ------------------------------------------------------------------------------
def show_sum():
    #accepts not arguments
    #output s a message
    #calls sum_of_numbers()
    print("12 + 45 = ", end="")
    sum_of_numbers(12,45)
    
def sum_of_numbers(num1, num2):
    #takes two numbers as arguments
    #prints sum
    print(num1 + num2)
    
# -----------------------------------------------------------------------------------------
def get_name():
    #takes no arguments
    #prompts the user for their first then last name
    fullName = input("What is your name (first last)? : ").split()
    first = fullName[0]
    last = fullName[1]
    reverse_name(first, last)

def reverse_name(first, last):
    print(last, first)
    
# ------------------------------------------------------------------------------------------
#get_value accepts no arguments assigns 99 calls change_me
def get_value():
    value = 99
    print("I just assigned the variable value: ", value)
    change_me(value)
    
    print("The value in the function get_value is still: ", value)
    
#changes value to 0 prints text
def change_me(value):
    value = 0
    print("The value in the function change me has been changed to: ", value)
    
# --------------------------------------------------------------------------------------------
def set_args():
    show_intrest(rate=0.01, periods=10, principal=10000.0)
    
def show_intrest(rate, periods, principal):
    intrest = principal * rate * periods
    print("simple inrest will be $", format(intrest, ",.2f"), sep="")
 
# --------------------------------------------------------------------------------------------
my_value = 10
def show_value():
    global my_value
    my_value +=1
    print("The value of the global variable my_value is", my_value)

# --------------------------------------------------------------------------------------------
number = 10
def change_global():
    global number
    number = int(input("What do you want to change the global variable to? "))
    global_variables_are_bad()
    
def global_variables_are_bad():
    print("The value of the global wariable was changed in change_global to", number)
    
# --------------------------------------------------------------------------------------------
CONTRIBUTION_RATE = 0.05
def pay_me():
    #accpets no arguments
    #prompts gross pay
    #calls show pay, passes gross
    #calls show bonus, passing bonus
    pay = float(input("Enter Your gross pay: "))
    bonus = float(input("Enter Your bonus pay: "))
    print()
    #calls a functoins
    show_pay(pay)
    show_bonus(bonus)
    
def show_pay(gross):
    #accepts float for gross
    #calculates teh contribution = gross * constant
    #it outputs the contibution from gross pay
    contribution = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $" + format(contribution, "0.2f"))

def show_bonus(bonus):
    #takes a float for bonus
    #contribution = bonus * global constant
    #outputs the contibution
    contribution = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $" + format(contribution, "0.2f"))
    
# --------------------------------------------------------------------------------------------
def random_numbers():
    #accepts no arguments
    #generates random int 1-10
    #outputs number
    print("The random number is", random(1,10))
    
# --------------------------------------------------------------------------------------------
def random_numbers2():
    #accepts no arguments
    #generates random int 1-100 5 times
    #outputs number
    for x in range(5):
        number = random(1,100)
        print(number)
        
# --------------------------------------------------------------------------------------------
def random_numbers3():
    #accepts no arguments
    #generates random int 1-100 5 times
    #outputs number
    for x in range(5):
        print(random(1,100))
        
# --------------------------------------------------------------------------------------------
#dice accepts no arguments
#loops two dice rolls until the user states no
def dice():
    #main loop
    while 1:
        #output
        print("Rolling your dice...")
        print("Your two dice are", random(1, 6), "and", random(1,6))
        print()
        #get user input
        prompt = input("Try your luck again? (y/n): ").lower()
        #checks input and breaks loop
        if prompt != "y":
            break
        
# --------------------------------------------------------------------------------------------
#accpets no arguments
#outputs random heads or tails 10 times
def coin_toss():
    #possible outputs
    options = ["Heads!", "Tails!"]
    #main loop
    for toss in range(10):
        #output
        print(options[random(0, 1)])
        
# --------------------------------------------------------------------------------------------
def test_random():
    start = [0,0,0,0,0,0,0,0,0,0,0]
    for x in range(1000000):
        lis = range(0,11)
        number = random(0,10)
        start[number] += 1
    print (start)
    
# --------------------------------------------------------------------------------------------
def total_ages():
    #gets user iput
    age1 = int(input("Please enter your age: "))
    age2 = int(input("Please enter the age of your best friend: "))
    
    total = calculate_ages(age1, age2)
    print("\ntogether you are", total, "years old.")
    
def calculate_ages(age1, age2):
    #adds and returns ages
    total_ages = age1 + age2
    return total_ages

# --------------------------------------------------------------------------------------------
#global constant
DISCOUNT_PERCENT = 0.2
#accpets no arguments
#calculates the sale price
#outputs the sale price
def sale_price():
    #creates the sale price
    salePrice = regular_price - discount(get_regular_price())
    #output
    print("The sale price was", format(salePrice, "0.2f"))

#accepts no argumetns
#returns value of user input
def get_regular_price():
    return int(input("What was the regular price of the item: "))
    
#accepts one argument (price)
#returns discount
def discount(price):
    return price * DISCOUNT_PERCENT

# --------------------------------------------------------------------------------------------
def commission_rate():
    #accepts no arguments
    #calculates the pay and outputs pay
    #determines if pay is negative (must reimberse)
    sales = get_sales()
    advancedPay = get_advanced_pay()
    commRate = determine_comm_rate(sales)
    pay = (sales * commRate) - advancedPay
    #checks if payed or owed
    if pay < 0:
        print("You owe the company $" + str(-1 * pay))
    else:
        print("You made $" + format(pay, "0.2f"))

def get_sales():
    #accepts no arguments
    #it promts the user for monthly sales
    #and returns the monthly sales
    sales = float(input("What are your total monthly sales? :"))
    return sales
    
def get_advanced_pay():
    #accepts no arguments
    #promts user to enter any advanced pay, or 0 for none
    #returns the advanced pay
    advancedPay = float(input("How much advanced pay did you get? : "))
    return advancedPay
    
def determine_comm_rate(sales):
    #accepts a float for sales
    #calculates commision rate for sales
    #returns commision rate        
    i = 0
    rates = [10000, 14999.01, 17999.01, 21999.01] #commission caps
    for percent in range(10, 18, 2):
        if sales < rates[i]:
            return percent/100
        i += 1
    return .18

# ------------------------------------------------------------------------------
def get_name():
    name = input("Please enter your name: ")
    return name

def validate_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
def nameIsEven():
    name = get_name()
    isEven = validate_even(len(name))
    if isEven:
        print("Your name has an even number of letters.")
    else:
        print("Your name has an odd number of letters.")

# ------------------------------------------------------------------------------
def getName2():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    return firstName, lastName
    
def printName():
    firstName, lastName = getName2()
    print(firstName, lastName)

# ------------------------------------------------------------------------------
def squareRoot():
    number = int(input("Please enter a value: "))
    print("The square root of", number, "is", sqrt(number))
    
# ------------------------------------------------------------------------------
def hypotenuse():
    numberA = int(input("Please enter A value: "))
    numberB = int(input("Please enter B value: "))
    print("The length of the hypotenuse is: ", hypot(numberA, numberB))
# ------------------------------------------------------------------------------
def thing():
    print(circle.area(5))
    print(rectangle.area(5,5))
# ------------------------------------------------------------------------------
def test():
    num1, num2, num3, num4, num5 = range(1, 6)
    print(num2)
    
# ------------------------------------------------------------------------------
def drawTriangle():
    TOP_X = 0
    TOP_Y = 100
    BASE_LEFT_X = -100
    BASE_LEFT_Y = -100
    BASE_RIGHT_X = 100
    BASE_RIGHT_Y = -100
    graph.line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    graph.line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    graph.line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, "green")
    
def graphic_fun():
    x1 = 0
    y1 = x3 = 100 
    x2 = y2 = y3 = -100
    radius = 50
    
    graph.square(x2, y2, 200, 'gray')
    graph.circle(x2, y2, radius, 'red')
    graph.circle(x1, y1, radius, 'blue')
    graph.circle(x3, y3, radius, 'green')
    graph.line(x1, y1, x2, y2, 'black')
    graph.line(x2, y2, x3, y3, 'black')
    graph.line(x3, y3, x1, y1, 'black')
    
    turtle.done()