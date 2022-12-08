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
        
    def __str__(self):
        return self.description
        
    def get_name(self):
        return self.name
    
    def get_aliases(self):
        return self.aliases
    
    def get_min_args(self):
        return self.min_args
    
    def get_max_args(self):
        return self.max_args
    
    def get_required_roles(self):
        return self.required_roles
    
    def get_required_perms(self):
        return self.required_perms
    
    def get_description(self):
        return self.description
    
    def get_help(self):
        return self.helfen
    
    def run_init(self):
        return self.init
    
    async def call(self, message):
        await self.callback(message)