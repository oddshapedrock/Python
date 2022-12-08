import discord

import os
from dotenv import load_dotenv

import CommandHandler

#create discord client
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

#initialize slash commands
tree = discord.app_commands.CommandTree(client)

#initialize the command handler
CommandHandler.main(discord, client, tree)

#Bot is ready to recieve commands
@client.event
async def on_ready():
    #initialize slash commands
    await tree.sync()
    print("AmazingBot is active")

#activate the bot
load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
