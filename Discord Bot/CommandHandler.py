import importlib
import sys, os

#toList takes one argument (an item to convert)
#converts and item to a list if it isn't already
#returns the item as a list
def toList(item):
    if not type(item) == "list":
        return [item]
    return item

#main takes 3 arguments (The discord module, the active client, and the command tree)
#sets up commands to be run in discord
#returns nothing
def main(Discord, client, tree):
    #move into the commands folder
    sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}\\commands')
     
    root_dir = '.\\commands'
    commandList = []
    #get all files in commands folder and subdirectories that end in .py
    for directory, subdirectories, files in os.walk(root_dir):
        sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}{directory[1:]}')
        for file in files:
            if file.endswith(".py"):
                file = file[:-3]
                #import the file as a module
                command = importlib.import_module(file)
                #build the slash Command object and append it to the command list
                commandList.append(command.build(tree))
                
    #on bot start up
    @client.event
    async def on_ready():
        #for every guild and every command
        for g in client.guilds:
            for command in commandList:
                #initialize the slash command in the guild
                await command.call_init(g)
            #sync the commands with discord
            await tree.sync(guild=Discord.Object(id=g.id))
        print("Amazing Bot is ready")

    #when a message is sent
    @client.event
    async def on_message(message):
        #check message starts with prefix and message author is not a bot
        if not message.content.startswith("!") or message.author.bot:
            return
        
        #get the content of the message as a string
        string = message.content[1:].split()
        
        #for every command
        for command in commandList:
            #get the ways to call the command
            name = command.get_name()
            aliases = command.get_aliases()
            
            commands = toList(name) + aliases
            
            for item in commands:
                #check if message command was command
                if not item.lower() == string[0].lower():
                    continue
                
                #get arguments of command
                min_args = command.get_min_args()
                max_args = command.get_max_args()
                required_perms = command.get_required_perms()
                required_roles = command.get_required_roles()
                description = command.get_description()
                helfen = command.get_help()
                
                #get the message content, guild and member
                content = message.content
                guild = message.guild
                member =  message.author #.roles
                
                #gets permissions of user
                permissions = [perm[0] for perm in message.author.guild_permissions if perm[1]]
                #gets roles of user
                roles = [role.name for role in member.roles]
                
                #checks that user has required permissions
                for permission in required_perms:
                    if not permission in permissions:
                        return await message.reply(f"You need the `{permission.lower()}` permission to use {name}.")
                
                #checks that user has requried roles
                for role in required_roles:
                    if not role in roles:
                        return await message.reply(f"You need the `{role.lower()}` role to use {name}.")
    
                string.pop(0)
                
                #checks if argument == help or description to print those messages instead
                if len(string) > 0:
                    if string[0] == "help":
                        return await message.reply(helfen)
                    if string[0] == "description":
                        return await message.reply(description)
                    
                #makes sure message has required amount of arguments
                if len(string) < min_args or (max_args >= 0 and len(string) > max_args):
                    if min_args == max_args:
                        return await message.reply(f"{name} expects {min_args} arguments!")
                    if max_args == -1:
                        return await message.reply(f"{name} expects between {min_args} and ∞ arguments");
                    
                    return await message.reply(f"{name} expects between {min_args} and {max_args}");
                
                #call the commands callback
                return await command.call(message, client)
