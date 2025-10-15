from random import randint

class Die:
    def __init__(self, face_size=6):
        self.size = face_size

    def roll(self):
        return randint(1, self.size)
    
    def size_of_die(self):
        return self.size
    