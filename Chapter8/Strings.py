import re

def count_t():
    print("The letter t appears: "+ str(input("Enter a word: ").lower().count("t")) + " time(s)")

def repetition():
    for count in range(1, 10):
        print("z" * count)
        
def split():
    string = "OneTwoThreeFour"
    string = re.findall("[A-Z][^A-Z]*", string)
    print(string)
    
    date = ""
    while date.count("/") < 2:
        date = input("Enter the date: ")
    date = date.split("/")
    print("Month:", date[0])
    print("Day:", date[1])
    print("Year:", date[2])