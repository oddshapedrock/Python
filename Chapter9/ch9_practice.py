import random
phonebook = {"Chris": "555-1111", "Eliot": "867-5390", "Katie": "555-0000"}
for key, value in phonebook.items():
    print(f"{key} has a phone number of {value}")
    del key
    del value
    
person = random.choice(list(phonebook))
del phonebook


