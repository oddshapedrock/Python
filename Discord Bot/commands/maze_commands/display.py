import sys, os
import discord
app_commands = discord.app_commands
#move into the main directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
#move into the graphics directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\..\\maze_graphics")

import display_image

#call back takes two arguments (message, and the client)
#calls the main command function
#display calls graphics display_image module
async def callback(message, client):
    await display_image.display(message, message.author.id, False)
    
#init takes two arguments (the command tree, and the guild)
#initializes the slash command function
async def init(tree, gld):
    @tree.command(name = "display", description = "Displays current maze.", guild=(discord.Object(id=gld.id)))
    #slashback takes no arguments
    #calls the main slash command function
    #display calls graphics display_image module
    async def slashback(interaction):
        return await display_image.display(interaction, interaction.user.id, True)

#build takes one argument (the command tree)
#creates the Command object
def build(tree):
    return Command.Command("display", "Displays current maze.", "Takes 0 arguments", callback, tree, init, max_args = 0)
