#<FunctionName> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>

#line_numbers accepts no arguments
#displays contents of file
#prints line number plus line content
def line_numbers():
    userInput = input("What file would you like to open?: ")
    #try opening file
    try:
        file = open(f"{userInput}.txt", "r")
    except IOError:
        print("There was an error opening the file")    
    else:
        #loop through file lines
        for index, line in enumerate(file):
            #offset index to start at 1
            index += 1
            #print index: line content
            print(f"{index}: {line}", end="")
    #close file
    finally:
        file.close()
    
#line counter takes no arguments
#prompts user for a file to read and gets the total number of lines
#outputs the line total for the file
def line_counter():
    TextFile = input("What file would you like to open?: ")
    #try opening the file
    try:
        data = open(f"{TextFile}.txt", "r")
        #put the file into an array
        data = [line for line in data]
    except IOError:
        print("There was an error opening the file")
    else:
        #print number of lines
        print(f"There are {len(data)} lines in {TextFile}.txt.")
    #close file
    finally:
        data.close()
        
#average_of_numbers takes no arguments
#gets the average of all the numbers in a text file
#outputs the average
def average_of_numbers():
    total = 0
    divisor = 0
    try:
        file = open("numbers.txt", "r")
        for line in file:
            number = float(line)
            total += number
            divisor += 1
        average = total / divisor
    except IOError:
        print()
    except ValueError:
        print()
    else:
        print()