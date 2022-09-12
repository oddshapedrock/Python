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
    pay = float(input("Enter Your gross pay"))
    
def show_pay(gross):
    #accepts float for gross
    #calculates teh contribution = gross * constant
    #it outputs the contibution from gross pay

def show_bonus(bonus):
    #takes a float for bonus
    #contribution = bonus * global constant
    #outputs the contibution