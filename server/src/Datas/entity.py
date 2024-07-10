class Entity:
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name