from dataclasses import dataclass
@dataclass
class AnimalClass:
    name:str
    habitat:str
    teeth: int =0
    def print(self):
        return f'''
name is {self.name}.
habitat is {self.habitat}.
teeth is {self.teeth}. '''
snowman = AnimalClass('Yeti','Himalayas')

print(snowman.print())
