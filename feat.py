from prereq import Prereq

class Feat:
    def __init__(self, name: str, prerequisite: list[Prereq], description: str):
        self.id = self.__hash__
        self.name = name
        self.prerequisite = prerequisite #[Prereq]
        self.description = description

    def __str__(self):
      return f"NAME: {self.name}\nDESCRIPTION: {self.description}"
    
    def __hash__(self):
       return hash(self.name)
    
    


