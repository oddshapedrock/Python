import sys, os
import discord
#go to main directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
from maze_generation import generate
#go to maze files directory
sys.path.insert(0, f"\\maze_files")

#go to maze graphics directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")
import generate_image
import display_image

#load maze takes two arguments (the message, and whether it was an interaction)
async def load_maze(message, interaction):
    grid_size = [11, 11]
    #generates a new maze
    grid_map = generate(grid_size)
    values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}
    
    #sets the file name
    if interaction:
        file_name = str(message.user.id)
        slash = True
    else:
        file_name = str(message.author.id)
        slash = False
    #try to save to file
    try:
        #save maze to file and or create new file
        with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + file_name + ".py"), "w") as file:
            file.write("data = " + str(grid_map) + "\nvalues = " + str(values) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")
    #could not save to file error
    except Exception:
        pass

    #call graphics generate_image
    generate_image.createMaze(file_name, True)
    #call grahics display_image
    await display_image.display(message, file_name, slash)

#callback takes two arguments (message, and the client)
#calls the main command
#creates a new maze game
async def callback(message, client):
    #load maze
    await load_maze(message, False)
    await message.channel.send("Game created!")

#init takes two arguments (the command tree, and the guild)
#initializes the slash command
async def init(tree, gld):
    @tree.command(name = "new-game", description = "Creates a new game", guild=(discord.Object(id=gld.id)))
    #slashback takes two arguments (message, and the client)
    #calls the main command
    #creates a new maze game
    async def slashback(interaction):
        #load maze
        await load_maze(interaction, True)
        return await interaction.response.send_message("Game created!")

#build takes one argument (the command tree)
#builds the Command object
def build(tree):
    return Command.Command("newgame", "Creates a new maze game", "Takes 0 arguments", callback, tree, init, max_args = 0)
