import pickle
global leaderBoard

def loadData():
    global leaderBoard
    with open("lb.dat", "rb") as file:
        leaderBoard = pickle.load(file)
        
def saveData():
    with open("lb.dat", "wb") as file:
        pickle.dump(leaderBoard, file)

def add(ID):
    loadData()
    ID = str(ID)
    if ID in leaderBoard:
        leaderBoard[ID] += 1
    else:
        leaderBoard[ID] = 1
    
    saveData()

def getData():
    global leaderBoard
    return leaderBoard