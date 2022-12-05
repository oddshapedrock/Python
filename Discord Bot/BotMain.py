import discord
import os

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f'AmazingBot is active')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
