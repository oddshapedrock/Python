import sys, os
import discord
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
from maze_generation import generate
sys.path.insert(0, f"\\maze_files")

sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")
import generate_image
import display_image

async def load_maze(message, interaction):
    grid_size = [11, 11]

    grid_map = generate(grid_size)
    values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}
    
    if interaction:
        file_name = str(message.user.id)
        slash = True
    else:
        file_name = str(message.author.id)
        slash = False
        
    with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + file_name + ".py"), "w") as file:
        file.write("data = " + str(grid_map) + "\nvalues = " + str(values) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")

    generate_image.createMaze(file_name, True)
    await display_image.display(message, file_name, slash)

async def callback(message):
    await load_maze(message, False)
    await message.channel.send("Game created!")

async def init(tree, gld):
    @tree.command(name = "new-game", description = "Creates a new game", guild=(discord.Object(id=gld.id)))
    async def slashback(interaction):
        await load_maze(interaction, True)
        return await interaction.response.send_message("Game created!")

def build(tree):
    return Command.Command("newgame", "Creates a new maze game", "Takes 0 arguments", callback, tree, init, max_args = 0)