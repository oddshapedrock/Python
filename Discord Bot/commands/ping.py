import sys, os
import discord
app_commands = discord.app_commands
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\")
import Command

async def callback(message, client):
    embed=discord.Embed(title="Pong! :ping_pong: ", description=f"```{round(client.latency * 1000)}ms```", color=0xFF5733)
    await message.channel.send(embed=embed)

async def init(tree, gld):
    @tree.command(name = "ping", description = "Pong!", guild=(discord.Object(id=gld.id)))
    async def slashback(interaction):
        embed=discord.Embed(title="Pong! :ping_pong: ", description=f"```{round(client.latency * 1000)}ms```", color=0xFF5733)
        return await interaction.response.send_message(embed=embed)

def build(tree):
    return Command.Command("ping", "Pong!", "Takes 0 arguments", callback, tree, init, max_args = 0)
