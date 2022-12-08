import sys, os
sys.path.insert(0, f"{os.path.dirname(__file__)}../")
import Command

async def callback(message):
    await message.channel.send("Pong!")

async def init(tree):
    @tree.command(name = "ping", description = "Pong!")
    async def slashback(interaction):
        return interaction.response.send_message("Pong!")
    tree.sync()

def build(tree):
    return Command.Command("ping", "Pong!", "Takes 0 arguments", callback, tree, init, max_args = 0)
