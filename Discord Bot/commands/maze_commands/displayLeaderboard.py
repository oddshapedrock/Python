import sys, os
import discord
app_commands = discord.app_commands
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
import leaderboard

async def callback(message, client):
    leaderboard.loadData()
    data1 = leaderboard.getData()
    data = list(sorted(data1, key= lambda x : int(data1[x]), reverse=True))
    top10 = data[:10]
    ts = ""
    for player in top10:
        ts += player + "\t solves:" + str(data1[player]) + "\n"
    embed=discord.Embed(title="Top 10", description=ts, color=0xFF5733)
    await message.channel.send(embed=embed)

async def init(tree, gld):
    @tree.command(name = "leaderboard", description = "Displays leaderboard", guild=(discord.Object(id=gld.id)))
    async def slashback(interaction):
        leaderboard.loadData()
        data1 = leaderboard.getData()
        data = list(sorted(data1, key= lambda x : int(data1[x]), reverse=True))
        top10 = data[:10]
        ts = ""
        for player in top10:
            ts += player + "\t solves:" + str(data1[player]) + "\n"
        embed=discord.Embed(title="Top 10", description=ts, color=0xFF5733)
        return await interaction.response.send_message(embed=embed)

def build(tree):
    return Command.Command("leaderboard", "Displays leaderboard", "Takes 0 arguments", callback, tree, init, max_args = 0)