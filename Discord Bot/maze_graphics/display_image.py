import discord
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
async def display(message, ID, slash):
    if slash == False:
        rel_path = "..\\maze_images\\i" + str(ID) + ".png"
        abs_file_path = os.path.join(script_dir, rel_path)
        try:
            with open(abs_file_path, 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
                file.close()
        except Exception:
            await message.channel.send("You do not have a saved maze.\n Please use !newGame first")