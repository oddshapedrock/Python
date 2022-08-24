import random

#rockPaperScissors takes no arguments
#recieves a user input rock paper or scissors
#generates a random play by the computer and determines who won
#outputs win tie or loss
def rockPaperScissors():
    #user input to lowercase
    RPS = input("Rock Paper or Scissors: ").lower()
    #default computer value
    value = ""
    
    #gives computer a value rock paper or scissors, 1/3 chance
    mystery_number = random.randint(1, 3)
    if mystery_number == 1:
        value = "rock"
    if mystery_number == 2:
        value = "paper"
    if mystery_number == 3:
        value = "scissors"

    #checks win status
    if(RPS == "rock" and value == "scissors" or
       RPS == "paper" and value == "rock" or
       RPS == "scissors" and value == "paper"):
        print("You won", RPS, "VS", value) #win statement
    elif RPS == value:
        print("You lost", RPS, "VS", value) #loss statement
    else:
        print("You tied", RPS, "VS", value) #tie statement

#takes no arguments
#gets average of three scores
#outputs average
#if average > 95 congratulate
def test_average():
    #user inputs, get the test scores
    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third score: "))
    #add and average test scores
    average = (score1 + score2 + score3) / 3
    #print average
    print("The average score is: ", format(average, "0.2f"))
    if average > 95: #score > 95
        print("Congratulations!\nYou got a high score!")

#takes no arguments
#calculates the pay rate with overtime
#outputs total pay
def auto_repair_payroll():
    #user input hours and rate
    hours = float(input("How many hours did you work: "))
    payRate = float(input("What is your pay per hour: "))
    totalPay = 0
    if hours > 40:
        totalPay = 40 * payRate
        totalPay += (hours - 40) * payRate * 1.5
    else:
        totalPay = hours * payRate
    print ("You will get paid: $"+ format(totalPay, "0.2f"))

#takes no arguments
#tests if number is even
#outputs true or false statement
def even_number():
    try:
        number = int(input("Please enter an even number: "))
    
        if number % 2 == 0: #modulus to determine even
            print("The number is even!")
        else:
            print("The number is odd!")
    except:
        print("That was not a number")
    
#takes no arguments
#gets input from user and sees if it matches the password
#outputs validity message
def password_verifier():
    PASSWORD = "prospero"
    userInput = input("Enter your password: ")
    if PASSWORD == userInput.lower(): #compares password to user input
        print("password accepted")
    else:
        print("password denied")

#takes no arguments
#organizes names alphabetically
#outputs names organized
def sort_names():
    name1 = input("Enter the first name (last, first) ")
    name2 = input("Enter the second name (last, first) ")
    print("Here are the names alphabetically")
    if name1 < name2:
        print(name1 + "\n" + name2)
    else:
        print(name2 + "\n" + name1)

#takes no argumentes
#prompt user for a number 1 to 10
#outpt if hte number is <> 5
#and output if the number is out of range
def range_of_numbers():
    #get user input
    number = int(input("Enter a number 1-10: "))
    
    #check grater than 10
    if number > 10 or number < 1:
        print("Only enter a nummber 1-10")
    elif number <= 5:
        print("your number is between 1 and 5")
    else:
        print("your number is between 6 and 10")
        
#takes no arguments
#checks if aplicable for loan
#must have >= 30000 salary
#must have >= 2 years on the job
def qualify_loan():
    salary = int(input("what is your slary: "))
    years = int(input("how long have you worked: "))
    
    #checks salary > 30000
    if salary >= 30000:
        #checks years > 2
        if years >= 2:
            print("You quailify for the loan")
        else:
            print("You must work for a total of 2 years to qualify")
    else:
        print("You must earn at leas $30,000 dollars per year to qualify")