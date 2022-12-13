import random

__all__ = [
"generate",
"generate_tiny",
"generate_3d"
]

#stores the maze generation functions
#generates a dictionary containing the maze values
class GenerateMaze():
    def __init__(self):
        self.maze_size = [0, 0]
        self.grid_map = []
        self.snake = {"direction": 0, "location": [0, 0], "number": 1}

    #generate takes one argument (the size of the maze as a list [x, y])
    #main generation function creates a maze based on maze size
    #returns the generated maze
    def generate(self, maze_size):
        self.maze_size = maze_size

        self.grid_map = []

        #creates grid rows
        for x_pos in range(maze_size[0]):
            self.grid_map.append([])
            #creates grid columns
            for y_pos in range(maze_size[1]):
                #stores dictionary of generation values in grid map
                self.grid_map[x_pos].append({
                    "walls": [True, True, True, True], #[top, bottom, left, right]
                    "visited": False,
                    "location": [x_pos, y_pos] #[top, bottom]
                    })
                
        #calls function to create maze path
        self.__make_path()
        
        #return completed maze
        return self.grid_map

    #__new_direction takes one argument (list of possible moves)
    #choses a random direction to travel [0: up, 1: down, 2: left, 3: right]
    #returns directin as a number or -1 if no directions exist
    def __new_direction(self, possible_moves):
        #test if list is empty
        if possible_moves:
            random_number = random.randint(0, len(possible_moves) - 1)
            self.snake["direction"] = possible_moves[random_number]
        else:
            self.snake["direction"] = -1

    #__get_pos takes two arguments (an x and a y position)
    #returns the cell from the gridmap at the disired location
    def __get_pos(self, x_pos, y_pos):
        return self.grid_map[x_pos][y_pos]

    #__get_possible_moves takes no arguments
    #determines the possible directions of travel
    #returns a list of the possible moves [0: up, 1: down, 2: left, 3: right]
    def __get_possible_moves(self):
        moves_list = []
        snake_x = self.snake["location"][0]
        snake_y = self.snake["location"][1]
        
        #checks if cell in direction is within grid
        if snake_y + 1 < self.maze_size[0]:
            dir_up = self.__get_pos(snake_x, snake_y +1)
            #add direction to list
            if not dir_up["visited"]:
                moves_list.append(0)
                
        #checks if cell in direction is within grid
        if snake_y -1 >= 0:
            dir_down = self.__get_pos(snake_x, snake_y -1)
            #add direction to list
            if not dir_down["visited"]:
                moves_list.append(1)
                
        #checks if cell in direction is within grid
        if snake_x -1 >= 0:
            dir_left = self.__get_pos(snake_x -1, snake_y)
            #add direction to list
            if not dir_left["visited"]:
                moves_list.append(2)
                
        #checks if cell in direction is within grid
        if snake_x + 1 < self.maze_size[0]:
            dir_right = self.__get_pos(snake_x +1, snake_y)
            #add direction to list
            if not dir_right["visited"]:
                moves_list.append(3)
                
        return moves_list

    #__new_visit takes 4 argumets ([x, y] location of current possition, x position of new location, y position of new location, [direction of trave, opposite of direction of travel])
    #updates the cells in the maze and updates the snake location to the new location
    #returns nothing
    def __new_visit(self, location, x_pos2, y_pos2, path):
        direction, opposite = path
        #sets walls inbetween locations to false
        self.__get_pos(location[0], location[1])["walls"][direction] = False
        self.__get_pos(x_pos2, y_pos2)["walls"][opposite] = False\
        #sets new cell to visited
        self.__get_pos(x_pos2, y_pos2)["visited"] = True
        #updates snake location
        self.snake["location"] = [x_pos2, y_pos2]

    #__make_path takes no arguments
    #generates the maze path
    #returns nothing
    def __make_path(self):
        starting_location = [0, 0]
        self.__get_pos(starting_location[0], starting_location[1])["visited"] = True
        
        #lists of all visisted locations
        saved_locations = [starting_location]
        
        #set up the snake
        snake = self.snake
        snake["location"] = starting_location
        index = 0
        
        #creates number of times to loop = maze size -1
        loop_number = (self.maze_size[0] * self.maze_size[1]) -1
        
        #visit cells
        for _ in range(loop_number):
            #get a direction
            self.__new_direction(self.__get_possible_moves())
            #back tracks cells until a move is possible
            while self.snake["direction"] == -1:
                if index == 0:
                    random.shuffle(saved_locations)
                self.snake["location"] = saved_locations[index]
                self.__new_direction(self.__get_possible_moves())
                index += 1
            #call visits based on the snakes new location
            location = snake["location"]
            if snake["direction"] == 0:
                self.__new_visit(location, location[0], location[1] + 1, [0, 1])
            if snake["direction"] == 1:
                self.__new_visit(location, location[0], location[1] - 1, [1, 0])
            if snake["direction"] == 2:
                self.__new_visit(location, location[0] -1, location[1], [2, 3])
            if snake["direction"] == 3:
                self.__new_visit(location, location[0] +1, location[1], [3, 2])
            #add location to saved locations
            saved_locations.append(snake["location"])

#create variables to call
_inst = GenerateMaze()
generate = _inst.generate
