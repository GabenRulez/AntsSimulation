import Pheromone
import Ant
import Position

class WorldMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pheromones = []
        self.ants = []
        self.foods = []

    def getPheromonesInCircularSector(
        self, startingPoint: Position.Position, direction: float, range: float, rangeAngle: float
    ):
        # "direction" is a direction the ant is looking at.
        # We query points "range/2" to the left and to the right.
        pass
        # return [] - the list of pheromones

    def addPheromones(self, pheromone: Pheromone.Pheromone):
        self.pheromones.append(pheromone)

    def updatePheromones(self):
        for pheromone in self.pheromones:
            # Walk over all pheromones and update their strength.
            # Later we can change their position.
            pass

    def addAnt(self, ant: Ant.Ant):
        self.ants.append(ant)
        # Update the structure

    def updateAntPosition(self, ant: Ant.Ant, wantedPosition: Position.Position):
        # Limit the position by map borders.
        pass

    def spawnFoodClump(self, position: Position.Position, amount: int, recoil: float = 1.0):
        for _ in range(amount):
            pass
            # self.foods.append(Food(random position))
            # select random location in a circle around "position" in range "recoil"
            # add food there

    def getFoodInRadius(self, position: Position.Position, radius: float):
        # return single piece of food and delete it from self.foods
        pass
