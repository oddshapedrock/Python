import sys, os
import discord
app_commands = discord.app_commands
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")

import display_image


async def callback(message):
    await display_image.display(message, message.author.id, False)
    pass

async def init(tree, gld):
    @tree.command(name = "display", description = "Displays current maze.", guild=(discord.Object(id=gld.id)))
   
    async def slashback(interaction):
        return await interaction.response.send_message("THis command currently is unopporational")

def build(tree):
    return Command.Command("display", "Displays current maze.", "Takes 0 arguments", callback, tree, init, max_args = 0)
