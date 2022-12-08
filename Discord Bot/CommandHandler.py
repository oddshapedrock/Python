import importlib
import sys, os

def toList(item):
    if not type(item) == "list":
        return [item]
    return item

def main(Discord, client, tree):
    
    sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}/commands')
     
    root_dir = './commands'
    commandList = []
    for directory, subdirectories, files in os.walk(root_dir):
        sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}{directory[1:]}')
        for file in files:
            if file.endswith(".py"):
                file = file.rstrip(".py")
                command = importlib.import_module(file)
                commandList.append(command.build(tree))
                
    @client.event
    async def on_ready():
        for g in client.guilds:
            for command in commandList:
                await command.call_init(g)
                await tree.sync(guild=Discord.Object(id=g.id))
        print("Amazing Bot is ready")

    @client.event
    async def on_message(message):
        if not message.content.startswith("!") or message.author.bot:
            return
        
        string = message.content[1:].split()
        
        for command in commandList:
            name = command.get_name()
            aliases = command.get_aliases()
            min_args = command.get_min_args()
            max_args = command.get_max_args()
            required_perms = command.get_required_perms()
            required_roles = command.get_required_roles()
            description = command.get_description()
            helfen = command.get_help()
            
            commands = toList(name) + aliases
            
            for item in commands:
                if not item.lower() == string[0].lower():
                    return
                
                content = message.content
                guild = message.guild
                member =  message.author #.roles
                permissions = [perm[0] for perm in message.author.guild_permissions if perm[1]]
                roles = [role.name for role in member.roles]
                
                for permission in required_perms:
                    if not permission in permissions:
                        return await message.reply(f"You need the `{permission.lower()}` permission to use {name}.")
                
                for role in required_roles:
                    if not role in roles:
                        return await message.reply(f"You need the `{role.lower()}` role to use {name}.")
    
                string.pop(0)
                
                if len(string) > 0:
                    if string[0] == "help":
                        return await message.reply(helfen)
                    if string[0] == "description":
                        return await message.reply(description)
                    
                if len(string) < min_args or (max_args >= 0 and len(string) > max_args):
                    if min_args == max_args:
                        return await message.reply(f"{name} expects {min_args} arguments!")
                    if max_args == -1:
                        return await message.reply(f"{name} expects between {min_args} and ∞ arguments");
                    
                    return await message.reply(f"{name} expects between {min_args} and {max_args}");
                
                return await command.call(message)
            
    @client.event
    async def on_interaction(interaction):
        print(interaction)
