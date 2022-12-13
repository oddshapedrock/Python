import sys, os
import discord
app_commands = discord.app_commands
#move to main directory
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\")
import Command
import leaderboard

#callback takes two arguments (message, and the client)
#calls the main command
#gets the top 10 maze completers
#sends message with leaderboard embed
async def callback(message, client):
    #load leaderboard
    leaderboard.loadData()
    #get data from leaderboard
    data1 = leaderboard.getData()
    #sorts data
    data = list(sorted(data1, key= lambda x : int(data1[x]), reverse=True))
    #gets top 10 from data
    top10 = data[:10]
    ts = ""
    #create embed with top 10
    for player in top10:
        ts += player + "\t solves:" + str(data1[player]) + "\n"
    embed=discord.Embed(title="Top 10", description=ts, color=0xFF5733)
    #send message
    await message.channel.send(embed=embed)

#init takes two arguments (the command tree, and a guild)
#initializes the slash command
async def init(tree, gld):
    @tree.command(name = "leaderboard", description = "Displays leaderboard", guild=(discord.Object(id=gld.id)))
    #callback takes no arguments
    #calls the main slash command
    #gets the top 10 maze completers
    #sends message with leaderboard embed
    async def slashback(interaction):
        #load leaderboard
        leaderboard.loadData()
        #get data from leaderbaord
        data1 = leaderboard.getData()
        #sorts data
        data = list(sorted(data1, key= lambda x : int(data1[x]), reverse=True))
        #gets top 10 from data
        top10 = data[:10]
        ts = ""
        #create embed with top 10
        for player in top10:
            ts += player + "\t solves:" + str(data1[player]) + "\n"
        embed=discord.Embed(title="Top 10", description=ts, color=0xFF5733)
        #send message
        return await interaction.response.send_message(embed=embed)

#build takes one argument (the command tree)
#builds the Commands object
def build(tree):
    return Command.Command("leaderboard", "Displays leaderboard", "Takes 0 arguments", callback, tree, init, max_args = 0)
