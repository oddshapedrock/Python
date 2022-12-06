import sys, os
sys.path.insert(0, f"{os.path.dirname(__file__)}../")
import Command

async def callback(message):
    await message.channel.send("Pong2!")

def build():
    return Command.Command("ping2", "Pong2!", callback)