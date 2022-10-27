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
            data = [*file]
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

#-------------------------------------------------------------------------------------------#
#pb_main takes no arguments
#calculates and most and least frequent numbers
#outputs most and least frequent numbers
def pb_main2():
    #call frequency
    freq = frequency()
    #get last 10 in list
    least_common = freq[:-11:-1]
    #get fisrt 10 in list
    most_common = freq[:10]
    #output most common numbers
    print("Most common numbers (most - least frequent): ")
    for num in most_common:
        print(num)
    #output least common numbers
    print("\nLeast common numbers (least frequent - most): ")
    for num in least_common:
        print(num)
        
#frequency takes no arguments
#calculates the frequency of numbers that occur in the powerball
#returns a sorted list of numbers in order of their occurance most - least common
def frequency():
    #try to open pbnumbers.txt
    try:
        with open("pbnumbers.txt", "r") as file:
            data = [*file]
    #could not read file error
    except IOError:
        print("Could not open file.")
        return
    #remove the powerball number and "\n" character
    for index, _ in enumerate(data):
        data[index] = data[index].rsplit(" ", 1)[0]
    #join all lines into one large list
    number_list = " ".join(data).split()
    #create a dictionary to later sort
    dictionary = {}
    #check each number > is in dictionary increase value by 1
    #> is not in dictionary add it to dictionary with starting value of 1
    for num in number_list:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    #sort the dictionary first by the reverse of the value
    #if values are the same sort then by the key number
    dictionary = dict(sorted(dictionary.items(), key= lambda item: (-int(item[1]), item[0])))
    #return a list of the dictionary values
    return list(dictionary)
#----------------------------------------------------------------------------------------------------------#
def gas_prices():
    timeline = create_timeline()
    compiled_data = get_year_data(timeline)
    output_message(compiled_data)
    sort_list(timeline)
    
def create_timeline():
    try:
        with open("GasPrices.txt", "r") as file:
            data = [*file]
    #could not read file error
    except IOError:
        print("Could not open file.")
        return
    
    timeline = []
    
    for line in data:
        date = line[:10]
        year = line[6:10]
        price = line[11:].rstrip("\n")
        timeline.append({"date": date, "year": year, "price": price})
        
    return timeline

def get_year_data(timeline):
    compiled_data = {}
    for year in range(1993, 2013+1):
        of_year = list(filter(lambda time: time["year"] == str(year), timeline))
        average = format(sum(float(item["price"]) for item in of_year) / len(of_year), "0.2f")
        highest = max([(time["price"]) for time in of_year])
        date_high = [value for index, value in enumerate(of_year) if value["price"] == highest]
        lowest = min([time["price"] for time in of_year])
        date_low = [value for index, value in enumerate(of_year) if value["price"] == lowest]
        compiled_data[year] = ({"average": average, "highest": date_high[0], "lowest": date_low[0]})
    return compiled_data

def sort_list(timeline):
    sorted_timeline = list(sorted(timeline, key=lambda value: value["price"]))
    with open("Low-to-High.txt", "w") as file:
        for date in sorted_timeline:
            file.write(f'{date["date"]}:{date["price"]}\n')
    sorted_timeline.reverse()
    with open("High-to-Low.txt", "w") as file:
        for date in sorted_timeline:
            file.write(f'{date["date"]}:{date["price"]}\n')
#comment
def output_message(compiled_data):
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The average price in {year} was: ${data["average"]}')
        
    print()
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The highest price in {year} was on {data["highest"]["date"]} with a value of ${float(data["highest"]["price"]):0.2f}')
        
    print()
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The lowest price in {year} was on {data["lowest"]["date"]} with a value of ${float(data["lowest"]["price"]):0.2f}')