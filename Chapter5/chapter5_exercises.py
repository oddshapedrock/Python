#<FunctionName> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>

import math
import random
import turtle
import my_graphics
from time import sleep
import keyboard

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
#math_quiz takes no arguments
#math quiz calls get numbers and prints the math equation
#prompts for an answer then checks answer
#outputs if answer was correct and prompts for another go
def math_quiz():
    keepGoing = 'y'
    #main loop
    while keepGoing == 'y':
        #deconstructs get_numbers
        num1, num2, total = get_numbers()
        #prints math problem
        print("\t "+ f"{num1:>3}" + "\n\t+" + f"{num2:>3}" + "\n\t‾‾‾‾")
        #asks for answer
        answer = int(input("Answer:  "))
        #checks answer
        if answer == total: 
            print("\nCorrect!")
        else:
            print("\nYou're wrong fool!\nThe answer was", total)
        print()
        #checks whether to continue
        keepGoing = input("Do you want to solve another? (y/n) : ").lower()
    
#get_numbers takes no arguments
#generates two random numbers 1-200 with random
#gets the total of the numbers
#returns the larger number followed by the 
#smaller number followed by the total
def get_numbers():
    #generate numbers
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    #find total (answer)
    total = num1 + num2
    #return larger number first then smaller number then total
    if num1 > num2:
        return num1, num2, total
    return num2, num1, total
    
# ----------------------------------------------------------------------------------------------- #
#time_loop takes no arguments
#displays the distance fellen in t seconds
#ouputs chart of falling after t seconds
def time_loop():
    #prints main headder
    print("Here is the distance an object will fall for 10 seconds")
    print("-------------------------------------------------------")
    #main loop loop loops 10 times
    for second in range(1, 11):
        distance = falling_distance(second)
        #output
        print(second, "sec\t\t", format(distance, "0.2f") + "m")
        
#falling_distance accepts one argument (time)
#calculates the distance fallen after time seconds
#returns the distance traveled
def falling_distance(time):
    distance = 1/2 * 9.8 * time ** 2
    return distance

# ----------------------------------------------------------------------------------------------- #
#game takes no arguments
#calls computer_choice, player_choice, and determine winner
#creates a game loop
#after loop ends says good bye
def game():
    #greeting
    print("You are now playing RPSLS")
    again = "y"
    #main loop
    while again == "y":
        #call functions
        computer = computer_choice()
        player = player_choice()
        #display weapons
        print("\nYou chose ...", player)
        print("The computer chose ...", computer[0], "\n")
        determine_winner(computer, player)
        #possible break loop
        again = input("Would you like to play again? (y/n) : ")
    #closing statement
    print("Thank you for playing.")

#computer choice takes no arguments
#generates a random number 1-5
#subrtacts 1 from that number for list iteration
#uses the number to pick the computers choice from a list
#returns (computer choice, number)
def computer_choice():
    number = random.randint(1, 5) - 1
    choices = ["paper", "lizard", "scissors", "rock", "spock"]
    computerChoice = choices[number]
    return computerChoice, number

#player_choice takes no arguments
#prompts for the players weapon
#returns the players choice
def player_choice():
    choice = input("Choose your weapon of choice (rock, paper, scissors, lizard, spock): ").lower()
    return choice
    
#determine_winner takes two arguments (computers choice and players choice)
#checks if player input is valid, or matches computer choice
#checks if computers choice is equal to player choice's two loss conditions
#other wise determines a win
#outputs who won
def determine_winner(computer, playerChoice):
    #deconstruct computer
    computerChoice, computerNum = computer
    #test the validity of the player's input
    choices = ["paper", "lizard", "scissors", "rock", "spock"]
    if not playerChoice in choices:
        print("Computer Wins! You entered an invalid weapon! Cheater!")
        return
    #all the possible sayings for each win condition. Ordered Winner choice -> loser choice
    slogans = {"paper":{"rock":"Paper covers rock.", "spock":"paper disproves spock."},\
               "lizard":{"paper":"Lizard eats paper.", "spock":"lizard poisons Spock."},\
               "scissors":{"paper":"Scissors cuts paper.", "lizard":"Scissors decapitates lizard."},\
               "rock":{"lizard":"Rock crushes lizard", "scissors":"Rock crushes scissors"},\
               "spock":{"scissors":"Spock crushes scissors.", "rock":"Spock vaporises rock."}}
    #checks for tie
    if playerChoice == computerChoice:
        print("Its a tie!", playerChoice, "=", computerChoice)
    #checks if player lost
    elif playerChoice == choices[computerNum - 1] or playerChoice == choices[computerNum - 2]:
        print("You lost!", slogans.get(computerChoice).get(playerChoice))
    #only other option is win
    else:
        print("You won!", slogans.get(playerChoice).get(computerChoice))
        
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
#draw snowman takes no arguments
#calls all other functions
#has no output
def drawSnowman():
    turtle.ht()
    #draws the body
    drawBase()
    drawMidSection()
    drawHead()
    #arm features
    drawArms()
    #extra features
    drawHat()
    drawFace()
#drawBase takes no arguments
#draws the base of the snowman
#outputs the bottom circle of the snowman
def drawBase():
    turtle.pencolor("BLACK")
    my_graphics.circle(0, -200, 80, "WHITE")
#drawMidSection takes no arguments
#draws the middle of the snowman
#outputs the middle circle
def drawMidSection():
    my_graphics.circle(0, -55, 65, "WHITE")
#drawHead takes no argumetns
#draws the head of the snowman
#outputs the top circle
def drawHead():
    my_graphics.circle(0, 50, 40, "WHITE")
#drawArms takes no arguments
#draws the arms of the snowman
#outputs 7 lines representing arms
def drawArms():
    turtle.pensize(3)
    #arm right
    midX = 115
    midY = 5
    my_graphics.line(65, -55, midX, midY, "BROWN")
    my_graphics.line(midX, midY, midX, 20, "BROWN")
    my_graphics.line(midX, midY, midX + 15, -10, "BROWN")
    #arm left
    midX = -130
    midY = 10
    my_graphics.line(-65, -55, -100, -35, "BROWN")
    my_graphics.line(-100, -35, midX, midY, "BROWN")
    my_graphics.line(midX, midY, midX - 5, 25, "BROWN")
    my_graphics.line(midX, midY, midX - 20, -5, "BROWN")
    turtle.pensize(1)
#drawHat takes no arguments
#draws a hat
#outputs two rectangles for a hat
def drawHat():
    width = 60
    turtle.color("BLACK")
    my_graphics.square(-.5 * width, 85, width, "BLACK")
    my_graphics.rectangle(-.5 * width - 20, 85, width + 40, 15, "BLACK")
#drawFace takes no arguments
#draws the snowmans face and pipe with smoke
#outputs two circle eyes a line mouth a pipe shape and loops for smoke
def drawFace():
    #eyes
    my_graphics.circle(-15, 65, 5, "BLACK")
    my_graphics.circle(15, 65, 5, "BLACK")
    #mouth
    my_graphics.line(-20, 40, 20, 40, "BLACK")
    #pipe
    turtle.pensize(3)
    my_graphics.line(15, 40, 50, 0, "BROWN")
    #tip of pipe
    turtle.pensize(3)
    turtle.setheading(45)
    my_graphics.square(turtle.xcor(), turtle.ycor(), 8, "BROWN")
    #smoke setup
    turtle.setheading(45)
    turtle.pencolor("GRAY")
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(turtle.xcor()+ 5, turtle.ycor() + 10)
    turtle.pendown()
    #smoke draw
    for smoke in range(3):
        turtle.forward(15)
        turtle.circle(2)
        turtle.right(10)
    turtle.forward(20)

# ----------------------------------------------------------------------------------------------- #
#this section is not part of the assignment, but I wanted to add my own creative
#liberties to this project, so I added a setting with animated snow

#animatedSnowman takes no arguments
#sets up the turtle and draws the background color
#creates instances of snowflakes with x, y positions
#calls animation
#has no output
def animatedSnowman():
    #turtle instantanious speed setup
    turtle.speed(0)
    turtle.delay(0)
    turtle.tracer(0, 0)
    turtle.ht()
    turtle.setup(600, 600)
    turtle.bgcolor("#93E7FB") #E0FFFF
    #snowflake calss takes 4 arguments (x position, y position, animation number, falling speed)
    #used to keep track of multiple snowflake positions
    #has no return functions
    class snowflake: 
        def __init__(self, posX, posY, anim, speed):
            self.posX = posX
            self.posY = posY   
            self.anim = anim
            self.animRight = True
            self.speed = speed
    #placeholder array
    snowflakes = []
    #creates 40 instances of snowflake with a random x and y position
    #appends each snowflake to snowflakes list
    for point in range(30):
        posX = random.randint(-300, 300)
        posY = random.randint(-300, 300)
        anim = random.randint(0, 7)
        speed = round(random.uniform(1.5, 3), 1)
        snowflakes.append(snowflake(posX, posY, anim, speed))
    #calls the animation    
    animation(snowflakes)
#animation takes no one argument (list of snowflakes)
#calls the draw functions to draw things to the screen
#uses an loop that continues until q key pressed
#no output
def animation(snowflakes):
    #starts an "infinate" loop
    while True:
        #clears the turtle screen
        turtle.clear()
        #checks if keyboard key is pressed (q)
        #stops the loop if true
        if keyboard.is_pressed("q"):
            turtle.done()
            break
        #iterates through each snowflake calls drawSnowflake
        #then changes its poition
        #increases the snowflakes animation, or decreases animation
        #if it is off the screen it moves it back on
        for flake in snowflakes:
            drawSnowflake(flake.posX, flake.posY, flake.anim)
            #wind speed
            flake.posX += .5
            #falling speed
            flake.posY -= flake.speed
            #snowflake is too low
            if flake.posY < - 265:
                flake.posY = 290
                flake.posX = random.randint(-300, 300)
            #snow flake goes off right of screen
            if flake.posX > 300:
                flake.posX = -300
            #cycles the animation loop
            if flake.anim == 7:
                flake.animRight = False
            if flake.anim == 0:
                flake.animRight = True
            #rotation speed
            if flake.animRight:
                flake.anim += .5
            else:
                flake.anim -= .5       
        #calls other draw functions
        drawGround()
        drawSnowman()
        #updates the screen
        turtle.update()
#drawSnowflake takes three arguments (x position, y position, anmiation point)
#draws a snowflake at given position with given animation rotation
#outputs snowflake
def drawSnowflake(x, y, anim):
    #sets upturtle pen
    turtle.pencolor("WHITE")
    turtle.pensize(1)
    turtle.setheading(0)
    #draws the four total lines
    my_graphics.line(x - (10 - anim), y, x + (10 - anim), y, "WHITE")
    my_graphics.line(x, y - 10, x, y + 10, "WHITE")
    my_graphics.line(x - (7 - (anim - 3)), y + (7 - (anim - 3)), x + (7 - (anim - 3)), y - (7 - (anim - 3)), "WHITE")
    my_graphics.line(x + (7 - (anim - 3)), y + (7 - (anim - 3)), x - (7 - (anim - 3)), y - (7 - (anim - 3)), "WHITE")
    #resets pen
    turtle.setheading(0)
    turtle.pencolor("black")
#drawGround takes no arguments
#creates the ground shape
#outputs something that looks like the ground
def drawGround():
    #set up turtle
    turtle.color("BLACK", "WHITE")
    turtle.penup()
    turtle.goto(300, -300)
    turtle.setheading(90) ## up
    turtle.pendown()
    #begin shape
    turtle.begin_fill()
    turtle.forward(40)
    #curve 1
    turtle.setheading(160)
    turtle.circle(300, 40)
    #curve 2
    turtle.setheading(160)
    turtle.circle(400, 45)
    #curve 3
    turtle.setheading(160)
    turtle.circle(300, 17.4)
    turtle.goto(-300, -300)
    #end shape
    turtle.end_fill()
    #reset pen
    turtle.setheading(0)
    turtle.pencolor("black")


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
#checkerboard takes no arguments
#chekcerboard makes a checkerboard
#outputs the checkerboard in turtle
def checkerboard():
    isBlack = True
    #5x5 grid
    for x in range(5):
        for y in range(5):
            #black square
            if isBlack:
                my_graphics.square((x * 30) - 75, (y * 30) - 75, 30, "BLACK")
                isBlack = False
            #white square
            else:
                my_graphics.square((x * 30) - 75, (y * 30) - 75, 30, "WHITE")
                isBlack = True
    