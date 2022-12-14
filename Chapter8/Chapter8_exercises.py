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
    morse = ['/', '???-', '-?????????', '-???-???', '-??????', '???', '??????-???', '--???', '????????????', '??????', '???---', '-???-', '???-??????', '--', '-???', '---', '???--???', '--???-', '???-???', '?????????', '-', '??????-', '?????????-', '???--', '-??????-', '-???--', '--??????', '-----', '???----', '??????---', '?????????---', '????????????-', '???????????????', '-????????????', '--?????????', '---??????', '----???']
    #input validation loop
    while True:
        canContinue = True
        #gets the message and sepperates the characters with a four-per-em space
        string = input("Message to encode: ")
        string = "???".join([*string]).lower()
        #checks if every letter is in the alphabet dictionary, and is not the space
        for letter in string:
            if not letter in alphabet and not letter == "???":
                canContinue = False
        #if every character is good break the loop
        if canContinue:
            break
        print("Message can only contain alphabet, number characters, and space.")
    #replace every character with corresponding morse_code value
    for index, char in enumerate(alphabet):
        string = string.replace(char, morse[index])
    print(string)
    
#phone_converter takes no arguments
#takes a phone number with numbers and or characters and converts it to phone number
#displays phone number
def phone_converter():
    while True:
        #get user input
        numberInput = input("Enter a number. Format (XXX-XXX-XXXX): ").lower()
        #checks input is required length and "-" = 2
        if len(numberInput) == 12 and numberInput.count("-") == 2:
            #ensures proper distripution of chars between "-" and alpha numericy
            if numberInput[8:].isalnum() and numberInput[0:3].isalnum() and numberInput[4:7].isalnum() and not numberInput[0] == "0":
                break
        #inform user that something is wrong with their string
        print("Sorry that is not properly formatted.")
    #list of numbers corresponding with keypad numbers and alphabet locations
    num_list = ["2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6",
                "6", "6", "7", "7", "7", "7", "8", "8", "8", "9", "9", "9", "9"]
    #replace each non alpha letter with number in corresponting point of numlist
    for char in numberInput:
        if char.isalpha():
            numberInput = numberInput.replace(char, num_list[ord(char) - 97])
    #output phone number        
    print("Here is your telephone number: " + numberInput)
    
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
def pb_main():
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
        return None
    #remove the powerball number and "\n" character
    for index, _ in enumerate(data):
        data[index] = data[index].rsplit(" ", 1)[0]
    #join all lines into one large list
    number_list = " ".join(data).split()
    #create a dictionary to later sort
    dictionary: dict = {}
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
#gas_prices takes no arguments
#used as a main function to call other functions
#returns nothing
def gas_prices():
    #get data
    timeline = create_timeline()
    #modify data
    compiled_data = get_year_data(timeline)
    output_message(compiled_data)
    sort_list(timeline)
    
#create_timeline takes no arguments
#used to split data in GasPrices.txt into usable chunks
#returns list of data   
def create_timeline():
    #try to open GasPrices.txt
    try:
        with open("GasPrices.txt", "r") as file:
            data = [*file]
    #could not read file error
    except IOError:
        print("Could not open file.")
        return None
    timeline = []
    #seperate data in the file
    for line in data:
        date = line[:10]
        year = line[6:10]
        price = line[11:].rstrip("\n")
        #add data to list
        timeline.append({"date": date, "year": year, "price": price})
    #return list    
    return timeline

#get_year_data takes one argument (list of data to go through)
#creates a dictionary of data, sorted by year
#returns the dictionary
def get_year_data(timeline):
    compiled_data = {}
    #gets data for every year 1993 - 2013
    for year in range(1993, 2013+1):
        #filters the data to only that of desired year
        of_year = list(filter(lambda time: time["year"] == str(year), timeline))
        #gets average gas price of the year
        average = format(sum(float(item["price"]) for item in of_year) / len(of_year), "0.2f")
        #gets the highest gas price of the year
        highest = max([(time["price"]) for time in of_year])
        #gets the date information of the date with highest gas price
        date_high = [value for index, value in enumerate(of_year) if value["price"] == highest]
        #gets the lowest gas price of the year
        lowest = min([time["price"] for time in of_year])
        #gets the date information of the date with lowest gas price
        date_low = [value for index, value in enumerate(of_year) if value["price"] == lowest]
        #stores the data into a dictionary to go through later
        compiled_data[year] = ({"average": average, "highest": date_high[0], "lowest": date_low[0]})
    #return dictionary of data
    return compiled_data

#sort_list takes one argument (list of data to go through)
#sorts the list by price high to low and outputs to file
#sorts the list by price low to high and outputs to file
def sort_list(timeline):
    #sort by price
    sorted_timeline = list(sorted(timeline, key=lambda value: value["price"]))
    #try to wite data to files
    try:
        #ouput low to high to Low-to-High.txt
        with open("Low-to-High.txt", "w") as file:
            #format data lines
            for date in sorted_timeline:
                file.write(f'{date["date"]}:{date["price"]}\n')
        #reverse the list
        sorted_timeline.reverse()
        #output High-to-low
        with open("High-to-Low.txt", "w") as file:
            #format data lines
            for date in sorted_timeline:
                file.write(f'{date["date"]}:{date["price"]}\n')
    #could not write to files error
    except IOError:
        print("Failed to write data to files.")
        
#output_message takes one argument (data of each year compiled to dictionary)
#gets the messages to output
#ouputs the messages
def output_message(compiled_data):
    #print (1993-2013) averages
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The average price in {year} was: ${data["average"]}')   
    print()
    #print (1993-2013) highest value and date
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The highest price in {year} was on {data["highest"]["date"]} with a value of ${float(data["highest"]["price"]):0.2f}')    
    print()
    #print (1993-2013) lowest value and date
    for year in range(1993, 2013+1):
        data = compiled_data[year]
        print(f'The lowest price in {year} was on {data["lowest"]["date"]} with a value of ${float(data["lowest"]["price"]):0.2f}')