import turtle as tur
#<program_name> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>

# hot dog time

#day_converter accepts no arguments
#it prompts the user for a number 1-7
#error message for numbers outside 1-7
#outputs the corresponding day of the week in spanish
def day_converter():
    #user input prompt
    numberInput = int(input("Enter a number 1-7: "))
    #checks if number is in range
    if (numberInput < 1 or numberInput > 7):
        return print("Error: Number is out of 1-7 range")
    #days of the week in order
    spanishDays = ["Lunes", "Martes", "Miércoles",
                   "Jueves", "Viernes", "Sábado", "Domingo"]
    #output day of the week
    print("The day of the week is", spanishDays[numberInput - 1]) #offsets input to start at 0

#roman_numerals accepts no arguments
#it prompts the user for a number 1-10
#converts the number to roman numerals
#outputs new roman numeral number
def roman_numerals():
    number = int(input("Enter a number 1-10: "))
    #initialize numeral var
    numeral = ""
    #checks if number is in range
    if (number < 1 or number > 10):
        return print("Error: Number is out of 1-10 range")

    if number < 4:
        numeral = "I" * number #for 1-3 types I number times
    elif number == 4:
        numeral = "IV"
    elif number > 4 and number < 9:
        numeral = "V" + ("I" * (number - 5)) #for every number 6-9 takes v and adds an I
    elif number == 9:
        numeral = "IX"
    else:
        numeral = "X"
        
    print(numeral)

#color_mixer takes no arguments
#takes a user input red, blue, or yellow
#outputs the mix of the two colors
def color_mixer():
	#user inputs
	color1 = input("Enter your first color: ").lower()
	color2 = input("Enter your second color: ").lower()
	
	#takes one argument (the users input) and determines if it equals the predetermined
	#red blue or yellow values. If true returns True, if false returns error message and False.
	def testInput(userInput):
		if userInput == "red" or userInput == "blue" or userInput == "yellow":
			return True
		else:
			print("Whoops looks like this is not a primary color: ", userInput)
			return False
	
	#ensures that both colors are satisfactory before continuing
	if testInput(color1) and testInput(color2):
		#takes two arguments (color 1 and color 2)
		#returns the mix of the two colors
		def mixer(c1, c2):
			if c1 == c2:
				return c1
			if c1 == "red":
				if c2 == "blue":
					#red + blue
					return "purple"
				if c2 == "yellow":
					#red + yellow
					return "orange"
			elif c1 == "blue":
				if c2 == "yellow":
					#blue + yellow
					return "green"
				if c2 == "red":
					#flips the input of the colors to cycle all posible arangements
					return "purple"
			else:
				#flips the input of the colors to cycle all posible arangements
				return mixer(c2, c1)
		
		mixedColor = mixer(color1, color2)
		
		#output
		print("Your color is", mixedColor)

#hot_dog takes no arguments
#hot dog takes the number of people attending a party and
#calculates the number of hotdog and bun packages needed
#returns the needed amount of packages and the left overs
def hot_dog():
    #number of product in a pack
	HOTDOGS = 10
	BUNS = 8

	#user input #of people
	numPeople = float(input("How many people will be attending your party? : "))
	
	numHotdogsPerson = float(input("How many hotdogs a person? : "))
	
	#calculates the number of people divided by the amount in a package. +1 if their is a remainder
	hotDogPackages =  (numPeople * numHotdogsPerson // HOTDOGS) + (numPeople * numHotdogsPerson % HOTDOGS > 0) #numPeople % HOTDOGS > 0 == True -> # + True == number + 1
	bunPackages =  (numPeople * numHotdogsPerson // BUNS) + (numPeople % BUNS > 0)
	
	#gets the total amount of product and subtracts the amount of people
	leftOverHotDogs = hotDogPackages * HOTDOGS - numPeople * numHotdogsPerson
	leftOverBuns = bunPackages * BUNS - numPeople * numHotdogsPerson
	
	#output packages and leftovers
	print("You need", format(hotDogPackages, "0.0f"), "packages of hotdogs.")
	print("You need", format(bunPackages, "0.0f"), "packages of buns.")
	print("You will have", format(leftOverHotDogs, "0.0f"), "hotdogs left over.")
	print("You will have", format(leftOverBuns, "0.0f"), "buns left over.")
	
#time_calculator accepts no arguments
#takes a user inputed number of seconds and calculates in the format of days, hours, minutes, seconds.
#outputs the time in days hours minutes seconds if not = 0
def time_calculator():
	#user input seconds
	userSeconds = int(input("Enter a time in seconds: "))
	
	#gets turns seconds to days
	days = userSeconds // 86400
	#turns what is leftover to hours
	hours = (userSeconds % 86400) // 3600
	#turns what is left over to minutes
	minutes = ((userSeconds % 86400) % 3600) // 60
	#turns what is left over into seconds
	seconds = ((userSeconds % 68400) % 3600) % 60 
	
	
	#outputs with the first non zero time frame.
	if(days):
		print(userSeconds, "seconds is", days, "day(s),", hours, "hour(s),", minutes, "minute(s),", seconds, "second(s)")
	elif(hours):
		print(userSeconds, "seconds is", hours, "hour(s),", minutes, "minute(s),", seconds, "second(s)")
	elif(minutes):
		print(userSeconds, "seconds is", minutes, "minute(s),", seconds, "second(s)")
	else:
		print(userSeconds, "seconds is", seconds, "second(s)")
	
#leap year takes no arguments
#uses a user input year and displays the amount of days in febuary for that year
#outputs if is leap year and number of days in febuary
def leap_year():
	#user input year
	year = int(input("Enter a year: "))
	
	#leapYear takes no arguments
	#prints out a leap year statement
	def leapYear():
		print(year, "is a leap year. There are 29 days in the month of February")
	
	#checks if divisable by 100 and 400
	if (year % 100 == 0 and year % 400 == 0):
		leapYear()
	#checks if not divisable by 100 but still divisable by 4
	elif(year % 100 != 0 and year % 4 == 0):
		leapYear()
	else:
		print(year, "is a not leap year. There are 28 days in the month of February")
	
#sir_fix_alot takes no arguments
#goes through a step by step WI-FI conection troubleshooter
#asks if the problem was fixed
#when fixed or never fixed outputs what the person should do
def sir_fix_alot():
	
	#didFix takes no arguments
	#prompts the user asking if the problem was fixed
	#returns True if problem was fixed False if it wasn't
	def didFix():
		print("Did that fix the problem?")
		yesNo = input("Y/N ").lower()
		if(yesNo == "y" or yesNo == "yes"):
			print("Glad I could help")
			print("Time to Netflix and Chill")
			return True
		elif(yesNo == "n" or yesNo == "no"):
			print()
			return False
		else:
			didFix()
			
	#introductory greeting
	print("Hello I am sir fix alot here to diagnose your problem")
	
	#path to attempt to fix stops any time user states problem is fixed
	print("Reboot computer and try to reconnect.")
	if not didFix():
		print ("Reboot router and try to reconnect.")
		if not didFix():
			print("Verify cables are firmly attatched.")
			if not didFix():
				print("Move router to better location.")
				if not didFix():
					print("Sorry I could not help.")
					print("Looks like you need a new router.")
					
#can_we_just_eat takes no arguments
#asks whether party members are vegitarian, vegan, or glutrn-free
#returns the possible resturaunts you can eat at
def can_we_just_eat():
	vegi = False
	vegan = False
	gluten = False
	
	#check takes one arguments (user input)
	#check if yes
	#returns true if yes
	def check(userInput):
		if userInput.lower() == "yes":
			return True
	
	#prompts user and checks checks if user said yes to any prompt
	#if user says yes value = true
	if check(input("is anyone in your party a vegetarian? (yes/no) : ")):
		vegi = True
	if check(input("is anyone in your party a vegan? (yes/no) : ")):
		vegan = True
	if check(input("is anyone in your party gluten intolerant? (yes/no) : ")):
		gluten = True
	
	#output the restraunt choices
	print("Here are your restaurant choices: ")
	if (not vegi and not vegan and not gluten):
		print("Joe's Gormet Burgers")
	if (not vegan):
		print("Main Street Pizza Company")
	if (not vegan and not gluten):
		print("Mama's Fine italian")
	print("Corner Café")
	print("The Chef's Kitchen")
	
#hit_the_target_mod takes no arguments
#takes a user input for angle and force
#moves the turtle based on the angle and force to see if it is inside the target
def hit_the_target_mod():
	#set constants
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 600
	TARGET_LLEFT_X = 100
	TARGET_LLEFT_Y = 250
	TARGET_WIDTH = 25
	FORCE_FACTOR = 30
	PROJECTILE_SPEED = 1
	NORTH = 90
	SOUTH = 270
	EAST = 0
	WEST = 180
	
	#setup window
	tur.clear()
	tur.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
	
	#draw target
	tur.hideturtle()
	tur.speed(0)
	tur.penup()
	tur.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
	tur.pendown()
	tur.setheading(EAST)
	tur.forward(TARGET_WIDTH)
	tur.setheading(NORTH)
	tur.forward(TARGET_WIDTH)
	tur.setheading(WEST)
	tur.forward(TARGET_WIDTH)
	tur.setheading(SOUTH)
	tur.forward(TARGET_WIDTH)
	tur.penup()
	
	#reset turtle
	tur.goto(0, 0)
	tur.setheading(EAST)
	tur.speed(PROJECTILE_SPEED)

	#user inputs
	angle = float(input("Enter the projectile's angle: "))
	force = float(input("Enter the launch force: (1-10) "))

	#set distance and angle
	dist =  force * FORCE_FACTOR
	tur.setheading(angle)

	#move turtle
	tur.pendown()
	tur.forward(dist)

	#check if inside target
	turX = tur.xcor()
	turY = tur.ycor()

    #checks if the player hit the target
	if (turX >= TARGET_LLEFT_X and turX <= TARGET_LLEFT_X + TARGET_WIDTH
	   and turY >= TARGET_LLEFT_Y and turY <= TARGET_LLEFT_Y + TARGET_WIDTH):
		print("hit")
	else:
		print("miss")
		#helps the player hit the target
		#checks if angle is in range
		if angle < 63.45:
			print("Try increasing your angle")
		elif angle > 70:
			print("Try decreasing your angle")
        #checks if player went past the lines
		elif angle >= 63.45 and angle <= 70:
			if(turX > TARGET_LLEFT_X + TARGET_WIDTH or turY > TARGET_LLEFT_Y + TARGET_WIDTH):
				print("Try decreasing your force")
		else:
			print("Try increasing your force")


	
	#to hit 63.45 <= angle <= 70
	#to hit middle about 66.61, 9.5
	#to hit 9. <= force <= 10
	
	
		