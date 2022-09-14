import circle
import rectangle
from colorama import Fore, Back, Style
#sets values 1-6
AREA_CIRCLE_CHOICE, CIRCUMFERENCE_CHOICE,\
AREA_RECTANGLE_CHOICE, PERIMETER_RECTANGLE_CHOICE,\
QUIT_CHOICE = range(1, 6)

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        print()
        try:
            choice = int(input(Fore.BLACK + "Enter your choice: "))
        except:
            print("Error: invalid selection")
            print()
            main()
        
        #perform the action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input(Fore.BLUE + "Enter the circle's radius: "))
            print(Fore.GREEN + "The area is:", circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input(Fore.BLUE + "Enter the circle's radius: "))
            print(Fore.GREEN + "The circumference is:", circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input(Fore.BLUE + "Enter the rectangle's width: "))
            length = float(input(Fore.BLUE + "Enter the rectangle's length: "))
            print(Fore.GREEN + "The area is:", rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input(Fore.BLUE + "Enter the rectangle's width: "))
            length = float(input(Fore.BLUE + "Enter the rectangle's length: "))
            print(Fore.GREEN + "The perimeter is:", \
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection")
        print()
            
def display_menu():
    print(Fore.BLACK + "        -MENU-")
    print(Fore.RED + "1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")
    
main()