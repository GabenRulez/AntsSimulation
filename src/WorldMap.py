import random
from Food import Food
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
        self,
        startingPoint: Position.Position,
        direction: float,
        range: float,
        rangeAngle: float,
    ):
        queriedPheromones = []
        for pheromone in self.pheromones:
            if pheromone.position.distanceToObject(startingPoint) <= range:
                angleBetweenPoints = startingPoint.angleToPoint(pheromone.position)
                if angleBetweenPoints >= direction - rangeAngle/2 and angleBetweenPoints <= direction + rangeAngle/2:
                    queriedPheromones.append(pheromone)

        # "direction" is a direction the ant is looking at.
        # We query points "range/2" to the left and to the right.
        return queriedPheromones


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

    def spawnFoodClump(
        self, position: Position.Position, amount: int, recoil: float = 1.0
    ):
        for _ in range(amount):
            pass
            # self.foods.append(Food(random position))
            # select random location in a circle around "position" in range "recoil"
            # add food there

    def removeFood(self, food: Food):
        self.foods.pop(food)

    def getFoodInRadius(self, midpoint: Position.Position, radius: float):
        # return single piece of food and delete it from self.foods
        foodInRadius = []
        for food in self.foods:
            if midpoint.distanceToObject(food.position) <= radius:
                foodInRadius.append(food)

        if len(foodInRadius) >= 1:
            return random.choice(foodInRadius)
        else:
            return None
