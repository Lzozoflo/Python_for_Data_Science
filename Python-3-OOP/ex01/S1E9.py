from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = True
        self.hairs = None
        self.eyes = None

    def die(self):
        self.is_alive = False

    def __str__(self):
        pass
    
    def __repr__(self):
        return f"Vector: ('{self.__class__.__name__}', '{self.hairs}', '{self.eyes}')"

class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)


    def die(self):
        """Your docstring for Method"""
        super().die()
