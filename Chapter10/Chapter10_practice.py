class Car():
    #car object has 5 attributes -> year, make, model, color, mileage
    
    #--attributes--#
    def __init__(self, year, make, model, color, mileage):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage
    
    #return string of vehicle descriptor
    def __str__(self):
        return f"The {self.year} {self.color} {self.make} {self.model} has {self.mileage} miles"
    
    #takes one argument an number of miles
    #adds miles to total mileage
    #returns a message
    def add_miles(self, miles):
        self.mileage = self.mileage + miles
        return f"The mileage for {self.year} {self.color} {self.make} {self.model} is {self.mileage} miles"
    