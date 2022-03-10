from distutils.util import change_root


class Character(object):
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True
    
    def smack(self, character):
        character.health = character.health - 100
        if character.health == 0:
            character.alive = False
