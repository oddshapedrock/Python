import random

#encode takes no arguments
#used to create an encoded message in a file
#outputs encrypted file
def encode():
    dictionary = {}
    #add uppercase letters to dictionary with symbol
    for letter in range(65, 65+26):
        dictionary[chr(letter)] = chr(letter+123)
    #add lowercase letters to dictionary with symbol
    for letter in range(97, 97+26):
        dictionary[chr(letter)] = chr(letter+123)
    #try to open twho different files    
    try:
        with open("encoded.txt", "w") as wfile:
            with open("plainText.txt", "r") as rfile:
                data = [*rfile]
                #for every letter of every word of every line
                #swap letter for corresponding symbol in dictionary
                for string in data:
                    for letter in string:
                        if letter in dictionary:
                            string = string.replace(letter, dictionary[letter])
                    #add line to file
                    wfile.write(string)
        print("Sucessfully written to file.")
    #could not open read or write to error
    except IOError:
        print("Failed to write data to file")

#decode takes no arguments
#decode takes an encrypted file and reverses it
#prints info decrypted
def decode():
    dictionary = {}
    #adds symbol to dictionary with corrosponding uppercase letter
    for letter in range(188, 188+26):
        dictionary[chr(letter)] = chr(letter-123)
    #adds symbol to dictionary with corrosponding lowercase letter
    for letter in range(220, 220+26):
        dictionary[chr(letter)] = chr(letter-123)
    #try to read from encoded.txt    
    try:
        with open("encoded.txt", "r") as file:
            data = [*file]
            #swap symbol for corresponding letter in dictionary
            for string in data:
                for letter in string:
                    if letter in dictionary:
                        string = string.replace(letter, dictionary[letter])
                #print line
                print(string, end="")
    #could not read from file error          
    except IOError:
        print("Failed read data from file")       
#----------------------------------------------------------------------------------------------#
#unique_words takes one argument (file to read from)
#calculates the usique words in file
#outputs all the unique words from the file
def unique_words(file):
    #try to open given file
    try:
        with open (file, "r") as f:
            data = [*f]
        #default set    
        wordSet = set()
        #add word to set
        for line in data:
            wordList = line.lower().split()
            for index, word in enumerate(wordList):
                #make word only contain alpha characters
                wordList[index] = "".join([letter for letter in word if letter.isalpha()])
            wordSet.update(set(wordList))
        #output message    
        print(file)
        print(list(wordSet))
    #could not open file error    
    except IOError:
        print("Failed to open file")
#un takes no arguments
#calls unique_words with given files
#has no output
def un():
    unique_words("text.txt")
    unique_words("mytxt.txt")
#---------------------------------------------------------------------------------------------------#
#world_series takes no arguments
#asks user for a year and gets that years winner with amount of total wins
#returns winner and amount of wins
def world_series():
    #try to open WorldSeries.txt
    try:
        with open("WorldSeries.txt", "r") as file: 
            data = [*file]
           
        blue = {} #stores year: team
        red = {} #stores team: wins
        
        #adds data to red and blue dictionaries
        for year in range(1903, 2008+1):
            team = data[year-1903].rstrip("\n")
            #adds the team
            blue[year] = team
            #adds the amount of times the team has won
            red[team] = data.count(team+"\n")
        #loop
        while True:
            #gets user input
            userInput = input("Enter a year: ")
            #checks that it is a number
            if userInput.isnumeric():
                #makes sure number is in valid range
                if 1903 <= int(userInput) <=2008:
                    userInput = int(userInput)
                    break
            #not in range statement
            print("Year must be between 1903 and 2008")
        #checks that year is not in the skip years
        if not userInput == 1904 and not userInput == 1998:
            #checks if year is a valid year in dictionary
            if userInput in blue:
                #output default message
                wins = red[blue[userInput].rstrip('\n')]
                print(f"{blue[userInput]} won in {userInput}. They have a total of {wins} wins.")
            else:
                print("We did not find that to be a valid year.")
        else:
            print("There was not a world series this year.")
    #could not open file error   
    except IOError:
        print("File could not be opened")
#----------------------------------------------------------------------------------------#
#blackJack takes no arguments
#runs a game of black jack
#has no output
def blackJack():
    #creates deck
    deck = {}
    types = ["Ace", "Jack", "Queen", "King", " of Spades", " of Hearts", " of Clubs", " of Diamonds"]
    #adds each value to deck
    for tpe in range(4, 8):
        #creates default cards
        for number in range(2, 10+1):
            deck[str(number) + types[tpe]] = number
        #adds ace jack queen king
        for tpe2 in range(0, 4):
            name = types[tpe2] + types[tpe]
            deck[name] = number
            #makes aces 11
            if tpe2 == 0:
                deck[name] = 11
    #create two players
    #Player takes no arguments
    #contains player information
    class Player():
        #set default values to a clear hand
        def __init__(self):
            self.clear_hand()
        #calculates the total of the hand
        def calc_total(self):
            self.total = sum([value[1] for value in self.hand])
        #clears the hand and and total of player    
        def clear_hand(self):
            self.hand = []
            self.total = 0
        #adds a value to the players hand and updates the total   
        def add(self, value):
            self.hand.append(value)
            self.calc_total()
    player1, player2 = Player(), Player()
    #continue looping games until deck is out of cards
    while len(deck) > 0:
        play(player1, player2, deck)
        player1.clear_hand()
        player2.clear_hand()

#play takes three arguments (player1, player2, and a deck of cards)
#simulates a single game of black jack
#prints winner and score
def play(player1, player2, deck):
    #try to add cards to player deck
    try:
        #while players are both  less than 21
        while player1.total <= 21 and player2.total <= 21:
            #add card if not == 21
            if not player1.total == 21:
                player1.add(getTup(deck))
            if not player2.total == 21:
                player2.add(getTup(deck))
        #attempt to shrink the player hand value
        shrink(player1, player2)
        #if player hand changed recall function to start over loop
        if player1.total < 21 and player2.total < 21:
            return play(player1, player2, deck)
    #if no more cards exist, continue
    except IndexError:
        pass
    #output messages
    print("Scores: ")
    if player1.total > 21 and player2.total > 21 or player1.total == player2.total:
        print("tie")
    elif player1.total < player2.total:
        if not player2.total == 21:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    else:
        print("Player 2 wins!")
    #scores
    print("p1", [card[0] for card in player1.hand], "sc", player1.total)
    print("p2", [card[0] for card in player2.hand], "sc", player2.total)

#getTup takes one argument (the deck to get the value from)
#gets a random card removes it from the deck
#adds card name and value to palyer hand
def getTup(deck):
    key = random.choice(list(deck.keys()))
    value = deck.pop(key)
    tup = (key, value)
    return tup

#shrink takes two arguments (player1, and player2)
#sets aces to 1 if total of hand is > 21
#returns nothing
def shrink(player1, player2):
    playerlist = [player1, player2]
    #fr every player
    for i in range(2):
        #check if score goes over 21
        if playerlist[i].total > 21:
            for idx, card in enumerate(playerlist[i].hand):
                #find an ace and set to 1 if not already
                if card[0].startswith("Ace") and not card[1] == 1:
                    playerlist[i].hand[idx] = (card[0], 1)
                    playerlist[i].calc_total()
                    break