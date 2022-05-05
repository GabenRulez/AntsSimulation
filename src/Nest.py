from Position import Position
from WorldMap import WorldMap


class Nest:
    def __init__(self, position: Position):
        self.position = position
        self.worldMap = None

    def setMap(self, worldMap: WorldMap):
        self.worldMap = worldMap

    def update(self):
        # for every ant in radius - take it from the Map class
        # execute ant.putDownFood()
        pass
