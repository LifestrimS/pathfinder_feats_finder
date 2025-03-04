class Prereq:
   def __init__(self, isFeat: bool, name: str, featId: int):
      self.isFeat = isFeat 
      self.name = name 
      self.featId = featId 

   def __str__(self):
      if self.isFeat:
         return f'{self.name} ({self.featId})'
      else:
         return f'{self.name}'