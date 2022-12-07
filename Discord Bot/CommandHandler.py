import importlib
import sys, os

def toList(item):
    if not type(item) == "list":
        return [item]
    return item

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
        if message.content.startswith("!") and not message.author.bot:
            string = message.content[1:].split()
            
            for command in commandList:
                name = command.get_name()
                aliases = command.get_aliases()
                min_args = command.get_min_args()
                max_args = command.get_max_args()
                required_perms = command.get_required_perms()
                required_roles = command.get_required_roles()
                description = command.get_description()
                
                commands = toList(name) + aliases
                
                for item in commands:
                    if item.lower() == string[0].lower():
                        
                        content = message.content
                        guild = message.guild
                        member =  message.author #.roles
                        permissions = [perm[0] for perm in message.author.guild_permissions if perm[1]]
                        roles = [role.name for role in member.roles]
                        print(roles)
                        
                        for permission in required_perms:
                            if not permission in permissions:
                                return await message.reply(f"You need the `{permission.lower()}` permission to use {name}.")
                        
                        for role in required_roles:
                            if not role in roles:
                                return await message.reply(f"You need the `{role.lower()}` role to use {name}.")
            
            if message.content.lower() == "!ping":
                await message.channel.send("Pong!")
            if message.content.lower() == "!ping2":
                await commandList[1].call(message)
