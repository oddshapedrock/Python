import sys, os
import discord
app_commands = discord.app_commands
#move to main directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\")
import Command

#call back takes two arguments (a message, and the client)
#calls the main commands function
#ping sents an embed with pong and the bot letency
async def callback(message, client):
    embed=discord.Embed(title="Pong! :ping_pong: ", description=f"```{round(client.latency * 1000)}ms```", color=0xFF5733)
    await message.channel.send(embed=embed)

#init takes two arguments (the slash command tree, and the guild)
#initializes the slash command
async def init(tree, gld):
    @tree.command(name = "ping", description = "Pong!", guild=(discord.Object(id=gld.id)))
    #slashback takes no arguments
    #calls the main slash command
    #ping sents an embed with pong and the bot letency
    async def slashback(interaction):
        embed=discord.Embed(title="Pong! :ping_pong: ", description=f"```{round(client.latency * 1000)}ms```", color=0xFF5733)
        return await interaction.response.send_message(embed=embed)

#build takes one argument (the slash command tree)
#builds the Command object for ping
def build(tree):
    return Command.Command("ping", "Pong!", "Takes 0 arguments", callback, tree, init, max_args = 0)
