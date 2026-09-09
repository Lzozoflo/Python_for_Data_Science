from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
        
    def __init__(self, name : str, is_alive : bool = True):
        super().__init__(name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
        
class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, name: str, is_alive:bool = True):
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def create_lannister(name: str, is_alive: bool):
        return Lannister(name, is_alive)
