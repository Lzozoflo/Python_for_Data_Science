from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = True

    def die(self):
        self.is_alive = False

class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)

    def die(self):
        """Your docstring for Method"""
        super().die()

    def is_alive(self):
        return super().is_alive()