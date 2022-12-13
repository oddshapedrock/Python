import sys, os
import discord

import importlib

app_commands = discord.app_commands
#go to main directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
import leaderboard
from maze_generation import generate
#go to graphics directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")
import generate_image
import display_image
#go to maze files directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_files")

#callback takes two arguments (message, and the client)
#calls the main command
#moves the position in the maze
#displayes and updated image of the maze
async def callback(message, client):
    #try to import maze module and display image and save the maze
    try:
        #get the maze
        maze = importlib.import_module(str(message.author.id))
        #get data from maze
        grid_map = maze.getData()
        values = maze.getValues()
        msg = message.content.split()
        #get locations
        if msg[1] == "down":
            #test if position is available
            if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][0]:
                values["player_pos"][1] += 1

        if msg[1] == "up":
            if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][1]:
                values["player_pos"][1] -= 1

        if msg[1] == "left":
            if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][2]:
                values["player_pos"][0] -= 1

        if msg[1] == "right":
            if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][3]:
                values["player_pos"][0] += 1

        #test if player is at the exit
        if values["player_pos"] == values["exit_loc"]:
            await message.channel.send("Maze complete!\nGenerating new...")
            grid_size = [11, 11]
            
            #add score to the leaderboard
            leaderboard.add(message.author)
            
            #create a new maze
            grid_map = generate(grid_size)
            values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}
            
            file_name = str(message.author.id)
            
            #save the maze information with the user ID
            with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + file_name + ".py"), "w") as file:
                file.write("data = " + str(grid_map) + "\nvalues = " + str(values) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")
            
            #update the maze image
            generate_image.createMaze(file_name, True)
        else:
            #save the maze information with the user ID
            with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + str(message.author.id) + ".py"), "w") as file:
                file.write("data = " + str(maze.getData()) + "\nvalues = " + str(maze.getValues()) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")
            #update the maze image
            generate_image.createMaze(str(message.author.id), False)
            
        #call the graphics display image module
        await display_image.display(message, message.author.id, False)
    
    #in the case of an error -> most likly a maze file not existing
    except Exception as e:
        print(e)
        await message.channel.send("You do not have a saved maze.\n Please use !newGame first")


#init takes two arguments (the command tree, and a guild)
#initializes the slash command
async def init(tree, gld):
    @tree.command(name = "move", description = "Moves the location in the maze", guild=(discord.Object(id=gld.id)))
    #create the choices for the maze
    @app_commands.choices(choices=[
        app_commands.Choice(name="Up", value="Up"),
        app_commands.Choice(name="Down", value="Down"),
        app_commands.Choice(name="Left", value="Left"),
        app_commands.Choice(name="Right", value="Right"),
        ])
    #slashback takes no arguments
    #calls the main slash command
    #moves the position in the maze
    #displayes and updated image of the maze
    async def slashback(interaction, choices: app_commands.Choice[str]):
        #try to import maze module and display image and save the maze
        try:
            #get the maze
            maze = importlib.import_module(str(interaction.user.id))
            #get data from the maze
            grid_map = maze.getData()
            values = maze.getValues()
            
            #check the users choice
            if choices.value == "Down":
                #test if position is possible
                if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][0]:
                    values["player_pos"][1] += 1

            if choices.value == "Up":
                if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][1]:
                    values["player_pos"][1] -= 1

            if choices.value == "Left":
                if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][2]:
                    values["player_pos"][0] -= 1

            if choices.value == "Right":
                if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][3]:
                    values["player_pos"][0] += 1
            
            #check if player is at the exit
            if values["player_pos"] == values["exit_loc"]:
                await interaction.channel.send("Maze complete!\nGenerating new...")
                grid_size = [11, 11]
                
                #add score to the leaderboard
                leaderboard.add(interaction.user)

                grid_map = generate(grid_size)
                values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}
                
                file_name = str(interaction.user.id)

                #save the maze information with the user ID
                with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + file_name + ".py"), "w") as file:
                    file.write("data = " + str(grid_map) + "\nvalues = " + str(values) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")

                #update the maze image
                generate_image.createMaze(file_name, True)
            else:
                
                #save the maze information with the user ID
                with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + str(interaction.user.id) + ".py"), "w") as file:
                    file.write("data = " + str(maze.getData()) + "\nvalues = " + str(maze.getValues()) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")
                #update the maze image
                generate_image.createMaze(str(interaction.user.id), False)
            
            #call the graphics display_image module
            return await display_image.display(interaction, interaction.user.id, True)
        
        #in the case of an error -> most likly a maze file not existing
        except Exception as e:
            print(e)
            return await interaction.channel.send("You do not have a saved maze.\n Please use !newGame first")

#build takes one argument (the command tree)
#creates the Command object
def build(tree):
    return Command.Command("move", "moves location in the maze", "Takes 1 argument", callback, tree, init, max_args = 1, min_args = 1)
