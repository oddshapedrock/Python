class Command:
    def __init__(self, name, description, callback, **kwargs):
        self.name = name
        self.description = description
        self.callback = callback
        self.required_roles = kwargs.get('required_roles', [])
        self.required_perms = kwargs.get('required_perms', [])
        
    def __str__(self):
        return self.description
        
    async def call(self, message):
        await self.callback(message)