import discord
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

#display takes three arguments (the message, the user id, and whether it is a slash command)
async def display(message, ID, slash):
    rel_path = "..\\maze_images\\i" + str(ID) + ".png"
    #gets teh path of the image file
    abs_file_path = os.path.join(script_dir, rel_path)
    #try to open the image file
    try:
        #try to open image file
        with open(abs_file_path, 'rb') as file:
            #send the image in discord
            picture = discord.File(file)
            await message.channel.send(file=picture)
            file.close()
    #could not open image file
    except Exception:
        await message.channel.send("You do not have a saved maze.\n Please use !newGame first")

