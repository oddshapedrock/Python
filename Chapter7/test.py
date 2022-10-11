import matplotlib

def IsValid(string):
    return string.isnumeric()

def WaysToFilter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = [num for num in numbers if num > 5 or num is 2]
    print(numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = list(filter(lambda x: x > 5 or x is 2, numbers))
    print(numbers)
    


def sales_list():
    sales = []
    days = int(input("How many days? : "))
    origonal_days = days
    while days:
        sale = input(f"Day{(0-(days -1))+ origonal_days}: ")
        sales.append(sale)
        days -= 1
    print("Here are your sales")
    for sale in sales:
        print(sale)

def in_list():
    lis = ["V45", "V65", "VF750", "VFR1100", "VTX1300"]
    user_input = input("what do you want to find: ").upper()
    if user_input in lis:
        print(f"Part number {user_input} was found in the list of part numbers.")
    else:
        print("Part number not found")

def list_append():
    names = []
    cont = "y"
    while cont is "y":
        name = input("Enter a name: ")
        names.append(name)
        cont = input("continue?: ")
    for name in names:
        print(name)

def list_index():
    lis = ["pizza", "hotdog", "fries"]
    search = input("What do you want to search for?: ")
    if search in lis:
        index = lis.index(search)
        new_food = input("Item found. New food: ")
        lis[index] = new_food
    else:
        print("did not find the food")
    print()
    print(lis)

def list_insert():
    list_before = [1, 2, 4]
    list_before.insert(2, 3)
    print(list_before)
    
def sort():
    jenny = [8, 6 ,7, 5, 3, 0, 9]
    print(jenny)
    jenny.sort()
    print()
    
def list_remove():
    lis = ["pizza", "hotdog", "fries"]
    search = input("What do you want to remove for?: ")
    if search in lis:
        lis.remove(search)
    else:
        print("did not find the food")
    print()
    print(lis)

def barista_pay():
    #accepts no argumebts
    #prompts the user for number of emplyees and hours worked
    #hourly rate for all emplyees
    employee_wages = []
    employees = int(input("How many employees do you have?: "))
    for number in range(employees):
        hours = int(input("Enter the amount of hours worked: "))
        employee_wages.append(hours)
    wage = int(input("Enter the hourly wage: "))
    employee_wages = [x * wage for x in employee_wages]
    for employee in employee_wages:
        print("pay: " + str(employee))
        
def list_total():
    nums = list(range(2, 12, 2))
    total = sum(nums)
    print(f"The sum of the numbers: {nums} is: {total}")
    
def list_average():
    nums = list(range(2, 12, 2))
    average = sum(nums) / len(nums)
    print(f"The sum of the numbers: {nums} is: {average}")
    
def list_total(nums):
    return sum(nums)
    
def list_function():
    nums = list(range(2, 12, 2))
    total = list_total(nums)
    print(f"The sum of the numbers: {nums} is: {total}")
    
def get_values():
    num_list = []
    while True:
        user_input = input("What number do you want to add? (or x to exit): ")
        if user_input is "x":
            break
        try:
            num_list.append(int(user_input))
        except ValueError:
            print("NAN entered. Exiting...")
            break
    list_return(num_list)
    
def list_return(num_list):
    print(f"You entered: {num_list}")
    
def tests_calc():
    score_list = []
    while True:
        user_input = input("Enter a test score. (x to stop): ")
        if user_input is "x":
            break
        try:
            score_list.append(float(user_input))
        except ValueError:
            print("NAN entered. Try another value.")
    if score_list:
        score_list.remove(min(score_list))
        average = sum(score_list) / len(score_list)
        print("The score average is", format(average, "0.2f"))
    else:
        print("You input no scores")
        