import importlib
import sys, os
def main(Discord, client):
    
    sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}\commands')
     
    root_dir = '.\commands'
    commandList = []
    for directory, subdirectories, files in os.walk(root_dir):
        sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}{directory[1:]}')
        for file in files:
            if file.endswith(".py"):
                file = file.rstrip(".py")
                command = importlib.import_module(file)
                commandList.append(command.build())
    
    @client.event
    async def on_message(message):
        if message.content.lower() == "!ping":
            await message.channel.send("Pong!")
        if message.content.lower() == "!ping2":
            await commandList[1].call(message)
