import sys, os
import discord
app_commands = discord.app_commands
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\")
import Command

async def callback(message):    
    await message.channel.send("Pong!")

async def init(tree, gld):
    @tree.command(name = "ping", description = "Pong!", guild=(discord.Object(id=gld.id)))
   
    async def slashback(interaction, one: int, two: int):
        print(one)
        add = one + two
        return await interaction.response.send_message(add)

def build(tree):
    return Command.Command("ping", "Pong!", "Takes 0 arguments", callback, tree, init, max_args = 0)
