from Position import Position
import WorldMap


class Nest:
    def __init__(self, position: Position, worldMap: WorldMap.WorldMap):
        self.position = position
        self.worldMap = worldMap


    def update(self):
        # for every ant in radius - take it from the Map class
        # execute ant.putDownFood()
        ants = self.worldMap.ants
        for ant in ants:
            if self.position.distanceToObject(ant.position):
                ant.putDownFood()
