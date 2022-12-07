import sys, os
sys.path.insert(0, f"{os.path.dirname(__file__)}../")
import Command

async def callback(message):
    await message.channel.send("Pong!")

def build():
    return Command.Command("ping", "Pong!", callback, required_roles=["tole"])