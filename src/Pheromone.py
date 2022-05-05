from Position import Position
from PheromoneType import PheromoneType

class Pheromone:
    def __init__(self, pheromoneType:PheromoneType, position:Position, startingStrength:int=100):
        self.pheromoneType = pheromoneType
        self.position = position
        self.strength = startingStrength
