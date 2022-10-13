from random import choices

#lottery takes no arguments
#generates 7 lottery numbers
#outputs the lottery numbers
def lottery():
    print("Generating lotto numbers...")
    #get 7 random numbers from 0-9 list
    rand_list = choices(range(0,10), k=7)
    print("Your lotto numbers are:")
    #print the numbers
    for num in rand_list:
        print(num)

#rainfall takes no inputs
#asks for rainfall of each month
#returns the min and max months and total and average
def rainfall():
    #list of months
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfall_list = []
    for month in months:
        #try to convert input to int
        try:
            rainfall = int(input(f"Enter the rainfall for {month}: "))
            #input validation
            while rainfall < 0:
                print("Rainfall must be positive.")
                rainfall = int(input(f"Enter the rainfall for {month}: "))
            #populate list
            rainfall_list.append(rainfall)
        #can't convert to int error
        except ValueError:
            print("Invalid value. Exiting...")
            return
        #general exception error
        except Exception:
            print("Something went wrong. Exiting...")
            return 
    #month with least value and index        
    least_month_index = rainfall_list.index(min(rainfall_list))
    least_month = months[least_month_index]
    #month with greatest value and index 
    max_month_index = rainfall_list.index(max(rainfall_list))
    max_month = months[max_month_index]
    #output statements
    print(f"{least_month} had the least rain with {rainfall_list[least_month_index]} inches of rain.")
    print(f"{max_month} had the most rain with {rainfall_list[max_month_index]} inches of rain.")
    print(f"Total rain for the year: {sum(rainfall_list)}")
    print(f"Average rain per month: {sum(rainfall_list)/12}")
    
#----------------------------------------------------------------------------#
#charge_accts takes no arguments
#creates a loop until the user quits
#gets a number attempt from user ensuring it is numeric
#returns nothing
def charge_accts():
    #starts loop
    cont = "y"
    while cont == "y":
        charge_num = input("Enter an account number: ")
        #input validation
        while not charge_num.isnumeric():
            charge_num = input("Enter an account number (numeric only): ")
        #call validity check
        isValid(charge_num)
        #prompt for continuation
        cont = input("\nCheck another account number? (y/n) ")
        
#isValid takes one argument (account number)
#tests if account number is a valid account
#prints valid or invalid based on results
def isValid(attempt):
    #try to open and read from file
    try:
        #opens charge_accounts.txt
        with open("charge_accounts.txt", "r") as file:
            #creates a list of account numbers from lines in file
            accounts = [line.rstrip("\n") for line in file]
    #file was not found error (most likely in a deletion)
    except FileNotFoundError:
        print("File not found.")
        return
    #Input Output error when reading the file
    except IOError:
        print("Problem opening file.")
        return
    #general exception error
    except Exception:
        print("An error ocurred")
    #test for attempt in account numbers and outputs accordingly
    if attempt in accounts:
        print("The number is valid")
    else:
        print("The number is invalid")
#----------------------------------------------------------------------------#
def drivers_exam():
    #creates a possibly infinate loop
    while True:
        test_name = input("Please enter the name of the file to read: ")
        try:
            with open(test_name, "r") as file:
                tester_answers = [answer.rstrip("\n") for answer in file]
            with open("driver_test_key.txt", "r") as key:
                key_answers = [answer.rstrip("\n") for answer in key]
            if not len(tester_answers) == len(key_answers):
                print("The amount of answers in the file do not match that of the key.")
                continue
            score = len(key_answers)
            wrong_answers = []
            for index, answer in enumerate(tester_answers):
                if not answer == key_answers[index]:
                    wrong_answers.append(index + 1)
                    score -= 1
            print("\nTest Grading Complete\n")
            print(f"You answered {score} correctly out of {len(key_answers)}")
            print(f"You missed {len(wrong_answers)} questions. The minimum you could miss to pass is 5.")
            
            if not len(wrong_answers) is 0:
                if len(wrong_answers) > 5:
                    print(f"You failed the exam. Study and try again.")
                else:
                    print(f"You passed!")
                print("Here are the questions you missed \n{wrong_answers}\n")
            else:
                print(f"You passed!")
            
        except FileNotFoundError:
            print(f"There was an error opening a file.")
        except IOError:
            print(f"Error reading a file.")
        except Exception as err:
            print("There was an error." + str(err))
            
        cont = input("Check another test? (y/n): ")
        if cont == "n":
            break