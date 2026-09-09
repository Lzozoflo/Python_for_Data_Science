from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):

    def __init__(self, name):
        super().__init__(name, True)

    def test(self):
        print("yes")

    def set_eyes(self, string):
        self.eyes = string

    def set_hairs(self, string):
        self.hairs = string

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
