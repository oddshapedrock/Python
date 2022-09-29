import random
choices = []
def game():
    #greeting
    print("You are now playing ultimate rock paper scissors")
    again = "y"
    #main loop
    while again == "y":
        #call functions
        global choices
        gameSetting = 0
        while gameSetting <= 0 or gameSetting > 4 :
            try: 
                gameSetting = int(input("Would you like to play\n1)Rock paper scissors\n2)Rock paper scissors lizard spock\n3)Ultimate rock paper scissors\n4)Ultimate Ultimate Rock paper scissors\nChoice:"))
            except:
                print("The input must be a number...")
                print("Refreshing game...")
                game()
        if gameSetting == 1:
            choices = ["rock", "paper", "scissors"]
        elif gameSetting == 2:
            choices = ["paper", "lizard", "scissors", "rock", "spock"]
        elif gameSetting == 3:
            choices = ["wolf", "cockroach", "tree", "man", "woman", "monkey", "snake", "axe", "scissors", "fire", "sun", "rock", "gun", "dynamite", "nuke", "lightning", "devil", "dragon", "alien", "water", "bowl", "air", "moon", "paper", "sponge"]
        elif gameSetting == 4:
            choices =["dynamite", "tornado", "quicksand", "pit", "chain", "gun", "law", "whip", "sword", "rock", "death", "wall", "sun", "camera", "fire", "chainsaw", "school", "scissors", "poison", "cage", "axe", "peace", "computer", "castle", "snake", "blood", "porcupine", "vulture", "monkey", "king", "queen", "prince", "princess", "police", "woman", "baby", "man", "home", "train", "car", "noise", "bicycle", "tree", "turnip", "duck", "wolf", "cat", "bird", "fish", "spider", "cockroach", "brain", "community", "cross", "money", "vampire", "sponge", "church", "butter", "book", "paper", "cloud", "airplane", "moon", "grass", "film", "toilet", "air", "planet", "guitar", "bowl", "cup", "beer", "rain", "water", "tv", "rainbow", "ufo", "alien", "prayer", "mountain", "satan", "dragon", "diamond", "platinum", "gold", "devil", "fence", "video game", "math", "robot", "heart", "electricity", "lightning", "medusa", "power", "laser", "nuke", "sky", "tank", "helicopter"]
            choices.reverse()
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
    number = random.randint(1, len(choices)) - 1
    computerChoice = choices[number]
    return computerChoice, number

#player_choice takes no arguments
#prompts for the players weapon
#returns the players choice
def player_choice():
    global choices
    choice = input("Choose your weapon of choice"+ str(choices)+ ": ").lower()
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
    global choices
    if not playerChoice in choices:
        print("Computer Wins! You entered an invalid weapon! Cheater!")
        return
    playerNum = choices.index(playerChoice)
    #checks for tie
    if playerChoice == computerChoice:
        print("Its a tie!", playerChoice, "=", computerChoice)
    #checks if player lost
    elif playerNum < computerNum and playerNum > computerNum - ((len(choices) - 1) / 2):
        print("You lost!", computerChoice, ">", playerChoice)
    #only other option is win
    else:
        print("You won!", playerChoice, ">", computerChoice)
        
game()