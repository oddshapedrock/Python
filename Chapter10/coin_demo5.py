from random import randint
class coin()
    def __init__(self):
        self.facing = "Heads"
    
    def __str__(self):
        return f"Landed on {self.facing}"
    
    def toss(self):
        if randint(0,1):
            self.facing = "Heads"
        else:
            self.facing = "Tails"

        