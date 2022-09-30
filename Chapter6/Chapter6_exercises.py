#<FunctionName> accepts ____ arguments
#it <what does it do>
#it <what does it output or return>
from random import randint as random

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
    #attempt to open the file and total the numbers
    try:
        file = open("numbers.txt", "r")
        #loop through items in line
        for line in file:
            number = float(line)
            total += number
            divisor += 1
        #divide total by amount of items
        average = total / divisor
    #file opening error
    except IOError:
        print("Error: There was an error with the file.")
    #divide by 0 error
    except ZeroDivisionError:
        print("Looks like there was nothing in the file")
    #not a number error
    except ValueError:
        print("Error: Something in the file may not have been a number.")
    #any unlisted erros
    except Exception:
        print("Error: an error occured")
    #output
    else:
        print(f"There were {divisor} items with an average value of {average}")
    #close file
    finally:
        file.close()
        
#ran_num_writer takes no arguments
#writes a series of random numbers 1 - 500 to a file
#user determines the amount of numbers
#outputs statement confirming numbers are written
def ran_num_writer():
    #attempt to make user input int and try to open file
    try:
        loopNum = int(input("How many numbers do you want to generate?: "))
        file = open("ran_num", "w")
    #catch value errors
    except ValueError:
        print(f"Invalid literal for int() with base 10: {loopNum}")
    #catch file errors
    except IOError:
        print("Looks like the file was not found.")
    #catch unlisted exceptions
    except Exception:
        print("An Error occured.")
    #output to file
    else:
        #create the specified amount of random numbers
        for _ in range(loopNum):
            randomNum = random(1, 500)
            file.write(f"{randomNum}\n")
    #close file
    finally:
        file.close()
        
#ran_num_reader takes no arguments
#reads the random number file
#displays numbers total amount of numbers and total of numbers
def ran_num_reader():
    total = 0
    numberOfNumbers = 0
    #attempt to open file and convert lines to ints
    try:
        file = open("ran_num", "r")
        #loop through the lines of the file and output them
        for line in file:
            number = int(line)
            total += number
            numberOfNumbers += 1
            print(line, end="")
        #final output statement
        print(f"The total of the {numberOfNumbers} random numbers is: {total}")
    #opening file error
    except IOError:
         print("Looks like the file was not found.")
    #something can't change to an int
    except ValueError:
        print("Error: Something in the file may not have been a number.")
    #other exeptions
    except Exception:
        print("Error: something went wrong")
    #close file
    finally:
        file.close()

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
#golf_main takes no arguments
#calls other functions based on menu choice
#outputs a welcome statement
def golf_main():
    print("Welcome to Hole in Twelve golf management system.")
    print("Please choose from the following commands...\n")
    choice = golf_menu()
    functionHolder = [golf_read, golf_write, exit]
    functionHolder[choice-1]()
    
#golf_menu takes no arguments
#displays the menu and prompts user for input
#returns user choice
def golf_menu():
    choice = False
    #creates a loop until a valid choice is selected
    while not choice:
        #try to convert user choice to int
        try:
            choice = int(input("1) Read golf data\n2) Append golf data\n3) Exit\nChoice: "))
            #ensures user choice is within parameters of 1-3
            while choice < 1 or choice > 3:
                print("\nMust enter number from 1-3")
                golf_menu()
        #catch value errors
        except ValueError:
            print("User input was Invalid! Reloading...\n")
    #returns the users choice
    return choice

#golf_read takes no arguments
#reads the contents of the golf file
#displays the contents of the golf file
def golf_read():
    #try to read file
    try:
        file = open("golf_stuff", "r")
        print()
        #print out lines in the file
        for line in file:
            print(line, end="")
        #final print statement
        print("All records successfully read!\n")
    #cant open file error
    except IOError:
        print("There was an error opening the file.")
    #general exception catching
    except Exception:
        print("There was an error.")
    #close file
    finally:
        file.close()
    #go back to main function
    golf_main()

#golf_write takes no arguments
#writes a user input name and score to the golf file
#appends golf file and displays a successful message
def golf_write():
    #try to open file
    try:
        cont = "y"
        #loop til user says no
        while cont == "y":
            file = open("golf_stuff", "a")
            print()
            #get name and score
            name = input("Golfer's name: ")
            score = input("Score: ")
            #write name and score data to file
            file.write(f"{name}\n{score}\n\n")
            #prompt to continue
            cont = input("Add another golfer? (y/n): ").lower()
        #final print statement
        print("Golf data written to golf_stuff.\n")
    #file cant open error
    except IOError:
        print("There was an error opening the file.")
    #general exception error
    except Exception:
        print("There was an error.")
    #close file
    finally:
        file.close()
    #return to main function
    golf_main()

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
#web_page takes no arguments
#creates the html for a simple web page
#writes the html to a file
def web_page():
    name = input("Enter your name(first, last): ")
    splitName = name.split()
    while not len(splitName) == 2:
        print("Only enter a First and Last Name.\nBoth are required!")
        name = input("Enter your name(first, last): ")
        splitName = name.split()
    sentence = input("Write a description of yourself: ")
    
    try:
        file = open(f"{name}.html", "x")
        file.write("<html><head>hi</head></html>")
        file.close()
    except FileExistsError:
        print("That file already exists.")
    