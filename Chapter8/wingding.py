userInput = input("What do you want to reverse: ")

#userInput

userInput = userInput[::-1]

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string = ""

for char in userInput:
    if char in alpha:
        offset = ord(char) - 107
        string += alpha[offset]

print(string)