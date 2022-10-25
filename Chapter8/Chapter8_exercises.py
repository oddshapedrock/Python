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
#prints user input date in date format
def date_converter():
    dateInput = input("Enter a date (mm/dd/yyyy): ")
    date = dateInput.split("/")
    datetime_date = datetime.datetime(date[2], date[0], date[1])
    
    print(datetime_date.strftime("%B"))