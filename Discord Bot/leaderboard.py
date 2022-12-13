import pickle
global leaderBoard

#loadData takes no arguments
#loads the data from lb.dat file
#saves data as leaderboard
def loadData():
    global leaderBoard
    with open("lb.dat", "rb") as file:
        leaderBoard = pickle.load(file)
 
#saves Data takes no arguments
#saves data to lb.dat
def saveData():
    with open("lb.dat", "wb") as file:
        pickle.dump(leaderBoard, file)

#add takes on argument (user name)
#adds the user to the leader board
#if user already exists adds one to score
def add(ID):
    loadData()
    ID = str(ID)
    #check if id already exists in the userboard
    if ID in leaderBoard:
        leaderBoard[ID] += 1
    else:
        leaderBoard[ID] = 1
    
    saveData()

#reutrn the data
def getData():
    global leaderBoard
    return leaderBoard