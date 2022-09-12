import turtle as tur
#<FunctionName> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>


#bug_collector takes no arguments
#takes the users collection of bugs over a five day period
#outputs the total number of bugs
def bug_collector():
    #initializing variables
    day = 0
    totalBugs = 0
    #loops for a total of five days
    while day < 5:
        day += 1
        #user input
        bugs = int(input("How many bugs did you collect on day " + str(day) + ": "))
        #input validation
        while bugs < 0:
            print("That does not look like a positive number.")
            bugs = int(input("How many bugs did you collect on day " + str(day) + ": "))
        #calculates total  
        totalBugs += bugs
    #output
    print("You collected", str(totalBugs) + ". You are the bug master")

#distance_traveled takes no arguments
#calculates the distance traveled at a certain speed
#after a certain amount of hours
#ouputs the distance after each hour
def distance_traveled():
    #user inputs
    speed = int(input("What is your speed? : "))
    time = int(input("How many hours are you traveling? : "))
    #input validation
    while speed < 0:
        print("Speed must be a positive value!!!")
        speed = int(input("What is your speed? : "))
    while time < 1:
        print("You must specify a time greater than 0 hours!!!")
        time = int(input("How many hours are you traveling? : "))
    #print initial header
    print("Hour\tDistance Traveled")
    print("_______________________")
    time2 = 1
    #calculate distance
    for point in range(1, time+1):
        distance = speed * time2
        #out put print statement
        print(str(time2), "\t", f'{distance:10.0f}')
        time2 += 1

#pennies takes no arguments
#takes a number of days and calculates the number of pennies
#doubles the pennies after each day
#outputs the pennies after each day
def pennies():
    #user input days
    days = int(input("How many days do you wnat to accure pennies? : "))
    #input validation
    while days < 1:
        print("Please enter a new value. Days must be greater than 0")
        days = int(input("How many days do you wnat to accure pennies? : "))
        
    pennies = .01
    time = 1
    #print initial header
    print("Day\t      Salary")
    print("------------------------")
    #main loop
    for point in range(1, days+1):
        #output print statement
        print(str(time), "\t", f"{'$' : >6}", format(pennies, "0.2f"))
        #increase vars
        pennies = pennies * 2
        time += 1

#hogwarts_tuition takes no arguments
#calculates the hogwarts tuition at a 3% increase for 5 years
#outputs the yearly tuition
def hogwarts_tuition():
    OLD_TUITION = 8000
    tuition = (OLD_TUITION * 2)
    #main header
    print("Year\t     Tuition Cost")
    print("------------------------")
    #main loop loops 5 times
    for year in range(1, 6):
        #adds 3% tuition increase
        tuition *= 1.03
        #output print statement
        print(str(year), "\t", f"{'$' : >6}", format(tuition, "0.2f"))
        
#population takes no arguments
#simulates the population growth from starting organsims
#percent daily growth and number of days
def population():
    #user input days
    population = int(input("Enter the starting population: "))
    growthRate = float(input("Enter the percent of daily growth: "))
    days = int(input("Enter the number of days to simulate: "))
    #input validation
    while population < 1:
        print("Please enter a new value. Population must be greater than 0")
        population = int(input("Enter the starting population: "))
    while days < 0:
        print("Please enter a new value. Days must be greater than 1")
        days = int(input("Enter the number of days to simulate: "))
    while growthRate < 0:
        print("Please enter a new value. Growth rate must be greater than 0")
        growthRate = float(input("Enter the percent of daily growth: "))
    
    #main header
    print("Day\t     Projected Population")
    print("------------------------------")
    #main loop
    for day in range(1, days+1):
        #output print statement
        print(str(day), "\t\t", str(population))
        #adds the population growth without float error
        population *= growthRate + 100
        population /= 100

#reverse_triange takes no arguments
#creates a triangle in reverse based on base size
#outputs triange to console
def reverse_triangle():
    #user input
    baseSize = int(input("Enter the base size of the triangle: "))
    #input validation
    while baseSize < 1:
        print("Base size must be 1+")
        baseSize = int(input("Enter the base size of the triangle: "))
    #main loop
    for point in range(baseSize, 0, -1):
        #creates point number of *
        line = "*" * point
        #output
        print(line)

#reverse_triange takes no arguments
#creates a stair pattern
#outputs pattern to console
def stair_pattern2():
    #user input
    numStair = int(input("Enter the number of stairs: "))
    #input validation
    while numStair < 1:
        print("Base size must be 1+")
        numStair = int(input("Enter the base size of the triangle: "))
    #main loop
    for point in range(0, numStair):
        #calculate space
        space = " " * point
        #output print
        print("@"+space+"@")
        
#repeating_squares takes no arguments
#makes squares in side of squares
#outputs squares in turtle
def repeating_squares():
    #turtle setup
    tur.ht()
    tur.delay(0)
    tur.speed(0)
    #user input
    numSquare = int(input("Enter the number of squares: "))
    #inpout validation
    while numSquare < 1:
        print("The number of squares should be 1+")
        numSquare = int(input("Enter the number of squares: "))
    #drawSquare takes one argument (square size)
    #draws a square based on the size in turtle
    def drawSquare(size):
        #calculates turtle square size
        distance = 10 + (5 * size)
        #draws a square
        for rot in range(4):
            tur.left(90)
            tur.forward(distance)
    #creates an offset to center image
    offset = ((numSquare * 5) + 10 ) /2
    tur.penup()
    tur.goto(offset, -offset)
    tur.pendown()
    #main loop
    for square in range(0, numSquare):
        #calls draw square function with square size
        drawSquare(square)
    tur.done()

#hypnotic_pattern takes no arguments
#makes a spiral pattern
#outputs pattern in turtle
def hypnotic_pattern():
    #turtle set up
    tur.ht()
    tur.delay(0)
    tur.speed(0)
    tur.left(90)
    #user input
    distance = int(input("Enter the distance (amount of turns): "))
    #input validation
    while distance < 0:
        print("Distance can not be a negative number.")
        distance = int(input("Enter the distance (amount of turns): "))
    #main loop draws spiral
    for turn in range(1,distance+2): #distance +2 to account for first iteration not creating a corner
        tur.forward(turn*3)
        tur.left(90)
    tur.done()