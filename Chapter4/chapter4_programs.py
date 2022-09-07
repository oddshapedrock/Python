import turtle as trt

#loop_example takes no arguments
#takes input from the user for the number of loops
#loops intil reaches the users input
def loop_example():
    keep_going = 'y'
    while keep_going == 'y': #sentinel loop
        number = int(input("Enter the number of loops to run: "))
        counter = 0
        while counter < number: #counted loop
            #run these lines of code
            counter += 1
            print("This is loop number", counter)
        keep_going = input("Keep going? : (y/n)")
     
#tur_draw takes no arguments
#draws a bunch of random lines
def tur_draw():
    for x in range(0, 50):
        trt.left(110)
        trt.forward(80)
        trt.done
        
#commission takes no arguments
#uses a while loop to get sale and rate from user
#calculate the sale
#output results
#see if user wants to run again
def commission():
    again = 'y'
    while again == 'y':
        sale = float(input("Enter the sale amount: "))
        commissionRate = float(input("Enter the commission rate: "))
        
        commission = commissionRate * sale
        
        print("The commission is $" + format(commission, "0.2f"))
        again = input("Do you want to calculate another? : (y/n) ")

#max_temp takes no arguments
#gets the temp from user
#while temp is greater than max temp
#asks for input again
def max_temp():
    MAX_TEMP = 102.5
    temp = 103
    while temp > MAX_TEMP:
        temp = float(input("Please enter the current temperature in degrees celcius: "))
        print()
        if temp > MAX_TEMP:
            print("Temperature is too high")
            print("Turn the thermostat down and wait for it to cool.")
            print("Then wait 5 min and measure again.")
        else:
            print("The temperature is acceptable.")
            print("Measure again in 15 min")
        
#loop_example2 takes no arguments
#just an example of a loop
def loop_example2():
    for item in range(5):
        print(item)
    
#loop_example3 takes no arguments
#just an example of a loop
def loop_example3():
    for item in range(1,10,2):
        print(item)
        
#loop_example4 takes no arguments
#just an example of a loop
def loop_example4():
    for item in range(1,6):
        print(item)
        
#loop_example5 takes no arguments
#just an example of a loop
def loop_example5():
    for item in range(1,6):
        print("Hello World!")
        
#squares takes no arguments
#squares the numbers 1-10
def square():
    print("Number \t Square")
    print("----------------")
    for item in range(1,11):
        print(item,'\t', item ** 2)
        
#speed_converter takes no arguments
#takes the kph to mph
def speed_converter():
    print("KPH \t MPH")
    print("----------------")
    for kph in range(60,131,10):
        print(kph,'\t', format(kph * .6214, "0.1f"))
        
#user_squares1() takes no arguments
#calculates squares to and including number
def user_squares1():
    number = int(input("Enter a number: "))

    print("Number \t Square")
    print("----------------")
    for item in range(1,number + 1):
        print(item,'\t', item ** 2)
        
#user_squares2() takes no arguments
#calculates squares to and including number
def user_squares2():
    number = int(input("Enter a start number: "))
    number2 = int(input("Enter an end number: "))
    lis = ''
    print("Number \t Square")
    print("----------------")
    for item in range(number,number2 + 1):
        lis += str(str(item) + '\t' + str(item ** 2) + "\n")
    print(lis)
    
def sum_numbers():
    loopTimes = int(input("Enter a number for loops: "))
    storeNum = loopTimes
    total = 0
    while loopTimes > 0:
        number = int(input("Enter a number: "))
        total += number
        loopTimes -= 1
    print("THe total of your", storeNum, "numbers is: ", total)
    
#takes no arguments
def property_tax():
    lotNum = int(input("Enter a lot Number (0 to end): "))
    while lotNum != 0:
        propVal = float(input("Please enter a property value: "))
        propTax = propVal * .0065
        if propVal != 0:
            print("Property Tax", propTax)
        lotNum = int(input("Enter a lot Number (0 to end): "))
        
def gross_pay():
    #gross_pay takes no arguments
    
    hours = int(input("Enter teh number of hours worked for 1 week: "))
    
    pay_rate = int(input("Enter the hourly rate:"))
    
    gross_pay = hours * pay_rate
    
    print('Gross pay: $', format(gross_pay, ',.2f'), sep=(""))
    
def retail_no_validation():
    #gross_pay takes no arguments
    MARK_UP = 1.25
    another = 'y'
    while another == "y" or another == "Y":
        wholesale = float(input("Enter the whole sale cost: "))
        
        retail = wholesale * MARK_UP
        
        print('Retail price: $', format(retail, ',.2f'), sep=(""))
        
        another = input('Do you want to enter another item? (enter y for yes): ')
        
def retail_with_validation():
    #gross_pay takes no arguments
    MARK_UP = 1.25
    another = 'y'
    while another == "y" or another == "Y":
        def validateCost():
            try:
                global wholesale
                wholesale = float(input("Enter the whole sale cost: "))
                while wholesale < 1:
                    print("We only accept values of $1+")
                    wholesale = float(input("Please enter a new value: "))
            except:
                print("Sorry that did not look like a number")
                validateCost()
        validateCost()
        
        retail = wholesale * MARK_UP
        
        print('Retail price: $', format(retail, ',.2f'), sep=(""))
        
        another = input('Do you want to enter another item? (enter y for yes): ')


def test_score_average():
    studentNum = int(input("How many students?: "))
    testsNum = int(input("How many tests?: "))
    
    for student in range(1, studentNum+1):
        testAverage = 0
        print()
        print("Student", student)
        for test in range(1, testsNum+1):
            testScore = float(input("   Enter test #"+ str(test) + ": "))
            testAverage += testScore
        print("The average for student", student, " is:", format(testAverage/ testsNum, "0.2f"))
        
def rectangle_pattern():
    x = int(input("Enter an X value: "))
    y = int(input("Enter a Y value: "))
    value = ""
    value2 = "*"
    while x > 0:
        while y > 0:
            value += value2
            y = y - 1
        print(value)
        x = x - 1

#triangle_pattern takes no arguments
#outputs a triangle pattern
def triangle_pattern():
   stop = int(input("Enter a size: "))
   for num in range(1, stop + 1):
       print("*" * num)

#stair_pattern()
#outputs a stair pattern()
def stair_pattern():
    stop = int(input("Enter a size: "))
    for num in range(1, stop + 1):
        for num2 in range(1, num):
            print(" ", end="")
        print("@")

def concentric_circles():
    STARTING_RADIUS = 20
    OFFSET = 10
    circles = int(input("How many circles? : "))
    radius = STARTING_RADIUS
    trt.speed(0)
    for circle in range(0, circles):
        trt.penup()
        trt.goto(0, -OFFSET*circle)
        trt.pendown()
        trt.circle(radius)
        radius += OFFSET
    trt.done()
    
def spiral_circles():
    NUM_CIRCLES = 3600
    RADIUS = 100
    ANGLE = 1
    
    trt.delay(0)
    trt.speed(0)
    import random
    for circle in range(NUM_CIRCLES):
        red = random.randint(100,200)
        green = random.randint(100,200)
        blue = random.randint(100,200)
        trt.colormode(255)
        trt.pencolor(red, green, blue)
        trt.forward(1)
        trt.circle(RADIUS)
        trt.left(ANGLE)
    trt.done()

def starburst():
    NUM_POINTS = 30
    trt.speed(0)
    trt.delay(0)
    trt.goto(-100, 0)
    for point in range(NUM_POINTS):
        trt.forward(200)
        trt.left(180-NUM_POINTS*0.5)
    trt.done()
    