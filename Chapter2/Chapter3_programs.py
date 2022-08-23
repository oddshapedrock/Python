import random

def play():
    value = int(input("Pick a #1-10: "))
    mystery_number = random.randint(0, 10)

    if value == mystery_number:
        print("Correct the number was", value)

    else:
        print("You picked", value, "but the computer picked", mystery_number)
        
def rockPaperScissors():
    RPS = input("Rock Paper or Scissors: ")
    value = ""
        
    mystery_number = random.randint(1, 3)
    if mystery_number == 1:
        value = "rock"
    if mystery_number == 2:
        value = "paper"
    if mystery_number == 3:
        value = "scissors"

    def win():
        print("You won", RPS, "VS", value)
    def loss():
        print("You lost", RPS, "VS", value)
    def tie():
        print("You tied", RPS, "VS", value)

    if RPS == value:
        tie()
    if RPS == "paper":
        if value == "rock":
            win()
        if value == "scissors":
            loss()
    if RPS == "rock":
        if value == "paper":
            loss()
        if value == "scissors":
            win()
    if RPS == "scissors":
        if value == "rock":
            loss()
        if value == "paper":
            win()

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