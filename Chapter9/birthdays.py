def bd_main():
    bd_dict = {"kyle": "10/27/2005"}
    while True:
        choice = get_menu_choice()
        options = {
            1: look_up,
            2: add_new,
            3: change,
            4: delete,
            5: quit
            }
        options.get(choice)(bd_dict)
        print()
    
    
def look_up(bd_dict):
    person = input("Who to look up? ").lower()
    day = bd_dict.get(person, "not found")
    print(f"The birth day for {person} is {day}")

def add_new(bd_dict):
    name = input("Enter a name: ").lower()
    date = input("Enter date: ")
    if name in bd_dict:
        print("Person already exists")
    else:
        bd_dict[name] = date
        print("added")

def change(bd_dict):
    name = input("Enter a name: ").lower()
    if name in bd_dict:
        date = input("Enter date: ")
        bd_dict[name] = date
        print("Changed B-day")
    else:
        print("Person does not exist")

def delete(bd_dict):
    name = input("Enter a name: ").lower()
    if name in bd_dict:
        date = input("Enter date: ")
        del bd_dict[name]
        print("Person no longer exists")
    else:
        print("Person does not exist")

def get_menu_choice():
    print("Do you want to:\n1) Lookup\n2) Add new\n3) Change B-day\n4) Delete B-day\n5) quit")
    while True:
        choice = input(":: ")
        if choice.isnumeric():
            choice = int(choice)
            if 0 < choice < 6:
                break
    return choice
bd_main()