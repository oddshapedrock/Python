import datetime

#sum_of_digits takes no arguments
#adds one digit numbers in string
#returns sum value
def sum_of_digits():
    #get user input
    String = input("Enter a string of single digit numbers without spaces: ")
    #input validation
    while not String.isnumeric():
        String = input("Please only enter numbers: ")
    #list of characters as integers
    numbers = [int(num) for num in [*String]]
    #print sum of the list
    print(f"The sum of your string is: {sum(numbers)}")

#date_converter takes no arguments
#checks if is valid date
#uses datetime import to get day of week and month name
#prints user input date in date format
def date_converter():
    #input with validation
    while True:
        #get user input
        dateInput = input("Enter a date (mm/dd/yyyy): ")
        #split input at "/" and store value as int. Only if it is numeric!
        date = [int(time) for time in dateInput.split("/") if time.isnumeric()]
        #check that both "/" characters were used and total date has length of 10 with 3 split arguments
        #breaks loop if all are true
        if dateInput.count("/") == 2 and len(dateInput) == 10 and len(date) == 3:
            #ensures proper distripution of chars between "/"
            split_date = dateInput.split("/")
            if len(split_date[2]) == 4 and len(split_date[1]) == 2 and date[2] > 999:
                break
        #inform user that something is wrong with their string
        print("Sorry that is not properly formatted.")
    #try to create a date
    try:
        datetime_date = datetime.datetime(date[2], date[0], date[1])
    #date was unable to be created as it is not an actual existing calendar date
    except ValueError:
        print("Sorry that is not a valid date.")
        date_converter()
    #print message
    else:
        print(datetime_date.strftime("The date is: %B, %d %Y. It lies on a %A."))
        
#morse_code takes no arguments
#encodes a message to morse code
#displays the morse code message to user
def morse_code():
    #list of all alphacharacters to replace
    alphabet = [" "]
    #add alphabet to list
    for letter in range(26):
        alphabet.append(chr(letter + 97))
    #add 0-9 to list
    for num in range(10):
        alphabet.append(str(num))     
    #list of all characters to morse code in same order as alphabet list
    morse_code = ['/', '•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--', '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••', '-----', '•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•']
    #input validation loop
    while True:
        canContinue = True
        #gets the message and sepperates the characters with a four-per-em space
        string = input("Message to encode: ")
        string = " ".join([*string]).lower()
        #checks if every letter is in the alphabet dictionary, and is not the space
        for letter in string:
            if not letter in alphabet and not letter == " ":
                canContinue = False
        #if every character is good break the loop
        if canContinue:
            break
        print("Message can only contain alphabet, number characters, and space.")
    #replace every character with corresponding morse_code value
    for index, char in enumerate(alphabet):
        string = string.replace(char, morse_code[index])
    print(string)
    
#phone_converter takes no arguments
#takes a phone number with numbers and or characters and converts it to phone number
#displays phone number
def phone_converter():
    while True:
        #get user input
        numberInput = input("Enter a number. Format (XXX-XXX-XXXX): ")
        #split input at "-" and store value as int. Only if it is numeric!
        number = numberInput.split("-")
        #checks input is required length and "-" = 2
        if len(numberInput) == 12 and len(number) == 3:
            #ensures proper distripution of chars between "-"
            if len(number[2]) == 4 and len(number[1]) == 3 and not number[0][0] == "0":
                #checks that all characters are alphabet or number
                if all(char.isalnum() or char == "-" for char in [character for character in numberInput]):
                    break
        #inform user that something is wrong with their string
        print("Sorry that is not properly formatted.")
    #get a list of numbers corresponding with keypad numbers and alphabet locations
    num_list = []
    #for all numbers 2-9
    for integer in range(2, 10):
        #add number 3 times
        for _ in range(3):
            num_list.append(str(integer))
        #add additional time if 7 or 9
        if integer == 7 or integer == 9:
            num_list.append(str(integer))
    #make lowercase
    number = numberInput.lower() 
    #replace each non alpha letter with number in corresponting point of numlist
    for char in number:
        if char.isalpha():
            number = number.replace(char, num_list[ord(char) - 97])
    #output phone number        
    print("Here is your telephone number: " + number)
    
#avg_num_words takes no arguments
#gets the average words per line in text.txt
#outputs total words, total lines, and average
def avg_num_words():
    #try to open file
    try:
        with open("text.txt", "r") as file:
            data = [line for line in file]
    #could not open the file
    except IOError:
        print("Could not open the file.")
        return
    #split every line into words    
    for index, line in enumerate(data):
        data[index] = line.split()
    #get values from data    
    total_words = sum([len(line) for line in data])
    total_sent = len(data)
    average_words = total_words / total_sent
    #output messages
    print(f"The file text.txt has {total_words} words.")
    print(f"The file text.txt has {total_sent} lines.")
    print(f"The average words per sentence is: {average_words}")
    
#igpay_atinlay takes no arguments
#converts a message to a form of pig latin
#outputs pig latin message
def igpay_atinlay():
    string = input("Message: ")
    #ensures alpha and space chars only
    while not all(letter.isalpha() or letter.isspace() for letter in string):
        print("Message can only contain alphabet characters.")
        string = input("Message: ")
    #split string to letters
    string = string.split()
    #rearange the letters
    for index, word in enumerate(string):
        #put first letter at end of word add "ay"
        word_arrange = word[1:] + word[0]
        pig_latin = word_arrange + "ay"
        string[index] = pig_latin
    #join the string
    string = " ".join(string).upper()
    #print output
    print(string)
    
def pb_main():
    try:
        with open("pbnumbers.txt", "r") as file:
            data = [line for line in file]
    except IOError:
        print("Could not open file.")
        return
    
    pb_most_common(data)
    pb_least_common(data)
    
def pb_most_common(data):
    for index, _ in enumerate(data):
        data[index] = data[index].replace("\n", "").split()
        data[index].pop()
        data[index] = " ".join(data[index])
    number_list = " ".join(data).split()
    frequent_nums = []
    for x in range(10):
        most_frequent = max(set(number_list), key=number_list.count)
        frequent_nums.append(most_frequent)
        number_list = [number for number in number_list if not number == most_frequent]
    print(frequent_nums)

def pb_least_common(data):
    for index, _ in enumerate(data):
        data[index] = data[index].replace("\n", "").split()
        data[index].pop()
        data[index] = " ".join(data[index])
    number_list = " ".join(data).split()
    frequent_nums = []
    for x in range(10):
        most_frequent = min(set(number_list), key=number_list.count)
        frequent_nums.append(most_frequent)
        number_list = [number for number in number_list if not number == most_frequent]
    frequent_nums.reverse()
    print(frequent_nums)
    
def pb_frequency():
    pass