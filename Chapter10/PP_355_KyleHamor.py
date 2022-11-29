#Kyle Hamor

from random import randrange #used to get random numbers

#get_numner_of_dials takes no arguments
#gets the number of dials per combonation based on user input
#returns an Integer -> the number of dials to generate
def get_number_of_dials():
    while True: #create a user validation loop
        #get user input
        dials = input("How many dials to you want to generate? ")
        
        #checks user input is a number
        if dials.isnumeric():
            #checks user input is >= 3 (the mininum required amount of dials)
            if int(dials) >= 3:
                #exits validation loop
                break
            else:
                #prints if user input is < 3
                print("Number should be at least 3")
        else:
            #prints if user input is not a number
            print("Input must be a number")
            
    #return user input as an integer  
    return int(dials)

#get_how_many_to_list takes no arguments
#gets the number of combos to generate based on user input
#returns an Integer -> the number of combos to generate
def get_how_many_to_list():
    while True: #creates user validation loop
        #gets user input number of combos
        combos = input("How many combos to you want to generate? ")
        #checks that combos are a number
        if combos.isnumeric():
            #exits validation loop
            break
        else:
            #prints if user input is not a number
            print("Input must be a number")
            
    #returns user input as an integer  
    return int(combos)

#get_number takes two arguments (the least possible number, and the greatest possible number)
#generates a random number in the range of the min and max values
#returns and Integer -> randomly generated number
def get_number(minimum, maximum):
    #generate number
    number = randrange(minimum, maximum+1) #offset max by 1 to include
    return number

#next_combo_number takes one argument (total numbers in combo)
#generates a random combonation with "total" numbers
#returns String -> combonation
def next_combo_number(total):
    #holds generated numbers
    number_list = []
    
    for _pass in range(total):
        #constants for value ranges
        MIN = 0
        MAX = 9
        #generate a new number
        new_number = str(get_number(MIN, MAX))
        #add number to list
        number_list.append(new_number)
        
    #join numbers to string
    as_string =  " ".join(number_list)
    
    return as_string

#main takes no arguments
#calls other functions
#prints out the data from the other functions as a display
def main():
    #call functions
    dials = get_number_of_dials()
    combos = get_how_many_to_list()
    #header
    print()
    print("----------------------------------")
    print()
    
    #body (combonations)
    #loop for total amount of combonations
    for combo in range(1, combos+1):
        #generate a combonation
        combonation = next_combo_number(dials)
        #print combonation
        print(f"Number {combo}: {combonation}")
        print() #spacer
        
    #footer  
    print("----------------------------------")
    print()
    
    #number of combos generated statement
    print(f"{combos} random combonations were generated")
        
main()