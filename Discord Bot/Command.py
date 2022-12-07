class Command:
    def __init__(self, name, description, callback, **kwargs):
        self.name = name
        self.description = description
        self.callback = callback
        self.aliases = kwargs.get('aliases', [])
        self.min_args = kwargs.get('min_args', 0)
        self.max_args = kwargs.get('max_args', -1)
        self.required_roles = kwargs.get('required_roles', [])
        self.required_perms = kwargs.get('required_perms', [])
        
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
    
    async def call(self, message):
        await self.callback(message)