import discord
import os
import sys
from dotenv import load_dotenv

import importlib

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}\commands')

root_dir = './commands'
commandList = []
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            file = file.rstrip(".py")
            command = importlib.import_module(file)
            commandList.append(command.build())

print("List: ", commandList)
@client.event
async def on_ready():
    print("AmazingBot is active")

@client.event
async def on_message(message):
    if message.content == "!ping":
        await commandList[0].call(message)
    
load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
