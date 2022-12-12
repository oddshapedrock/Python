import sys, os
import discord

import importlib

app_commands = discord.app_commands
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
from maze_generation import generate
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")
import generate_image
import display_image

sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_files")

async def callback(message):
    maze = importlib.import_module(str(message.author.id))
    grid_map = maze.getData()
    values = maze.getValues()
    msg = message.content.split()
    if msg[1] == "down":
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][0]:
            values["player_pos"][1] += 1

        await message.channel.send("down")
    if msg[1] == "up":
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][1]:
            values["player_pos"][1] -= 1

        await message.channel.send("up")
    if msg[1] == "left":
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][2]:
            values["player_pos"][0] -= 1

        await message.channel.send("left")
    if msg[1] == "right":
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][3]:
            values["player_pos"][0] += 1

        await message.channel.send("right")
    if values["player_pos"] == values["exit_loc"]:
        await message.channel.send("Maze complete!\nGenerating new...")
        grid_size = [11, 11]

        grid_map = generate(grid_size)
        values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}
        
        file_name = str(message.author.id)

            
        with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + file_name + ".py"), "w") as file:
            file.write("data = " + str(grid_map) + "\nvalues = " + str(values) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")

        generate_image.createMaze(file_name, True)
    else:
        with open(os.path.join(os.path.dirname(__file__) + "..\\..\\..\\maze_files\\" + str(message.author.id) + ".py"), "w") as file:
            file.write("data = " + str(maze.getData()) + "\nvalues = " + str(maze.getValues()) + "\ndef getData():\n\treturn data\ndef getValues():\n\treturn values")
        generate_image.createMaze(str(message.author.id), False)
    await display_image.display(message, message.author.id, False)
    pass

async def init(tree, gld):
    @tree.command(name = "move", description = "Moves the location in the maze", guild=(discord.Object(id=gld.id)))
   
    async def slashback(interaction):
        return await interaction.response.send_message("THis command currently is unopporational")

def build(tree):
    return Command.Command("move", "moves location in the maze", "Takes 1 argument", callback, tree, init, max_args = 1, min_args = 1)