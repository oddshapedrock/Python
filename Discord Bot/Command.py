#used in the creation of a command
#takes 6+ arguments (name of command, description, help statement, command callback, tree of commands, slash command init statement)
#optional arguments (aliases of the command, mininum number of arguments, maximum number of arguments, required roles to use, required perms to use)
class Command:
    def __init__(self, name, description, helfen, callback, tree, init, **kwargs):
        self.name = name
        self.description = description
        self.helfen = helfen
        self.callback = callback
        self.aliases = kwargs.get('aliases', [])
        self.min_args = kwargs.get('min_args', 0)
        self.max_args = kwargs.get('max_args', -1)
        self.required_roles = kwargs.get('required_roles', [])
        self.required_perms = kwargs.get('required_perms', [])
        self.init = init
        self.tree = tree
    
    #return commands description
    def __str__(self):
        return self.description
        
    #return the name of the command
    def get_name(self):
        return self.name
    
    #return the aliases of the command
    def get_aliases(self):
        return self.aliases
    
    #return the mininum args needed for the command
    def get_min_args(self):
        return self.min_args
    
    #return the max args needed for the command
    def get_max_args(self):
        return self.max_args
    
    #return the required roles for the command
    def get_required_roles(self):
        return self.required_roles
    
    #return the required permissions for the command
    def get_required_perms(self):
        return self.required_perms
    
    #return the description of the command
    def get_description(self):
        return self.description
    
    #return the help statement of the command
    def get_help(self):
        return self.helfen
    
    #call_init takes one argument (a guild id)
    #calls the function to initialize the slash command for the guild
    async def call_init(self, guild):
        await self.init(self.tree, guild)
    
    #call takes two arguments (the message, and the client)
    #calls the commands callback
    async def call(self, message, client):
        await self.callback(message, client)
