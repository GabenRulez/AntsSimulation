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
                if (
                    angleBetweenPoints >= direction - rangeAngle / 2
                    and angleBetweenPoints <= direction + rangeAngle / 2
                ):
                    queriedPheromones.append(pheromone)

        # "direction" is a direction the ant is looking at.
        # We query points "range/2" to the left and to the right.
        return queriedPheromones

    def addPheromones(self, pheromone: Pheromone.Pheromone):
        self.pheromones.append(pheromone)

    def updatePheromones(self):
        pheromonesToDiscard = []
        for pheromone in self.pheromones:
            pheromone.strength -= 1
            if pheromone.strength <= 0:
                pheromonesToDiscard.append(pheromone)
            # Walk over all pheromones and update their strength.
            # Later we can change their position.

        for pheromone in pheromonesToDiscard:
            self.pheromones.remove(pheromone)

    def addAnt(self, ant: Ant.Ant):
        self.ants.append(ant)
        # Update the structure

    def updateAntPosition(self, ant: Ant.Ant, wantedPosition: Position.Position):
        # Limit the position by map borders.
        realisticPosition = Position.Position(
            min(max(wantedPosition.x, -self.width / 2), self.width / 2),
            min(max(wantedPosition.y, -self.height / 2), self.height / 2),
        )
        ant.pos = realisticPosition

    def spawnFoodClump(
        self, position: Position.Position, amount: int, recoil: float = 1.0
    ):
        for _ in range(amount):
            food_x = random.random(position.x - recoil, position.x + position)
            food_y = random.random(position.y - recoil, position.y + position)

            food_position = Position(food_x, food_y)
            self.foods.append(Food(food_position))

    def getFoodInRadius(self, midpoint: Position.Position, radius: float):
        # return single piece of food and delete it from self.foods
        for food in self.foods:
            if midpoint.distanceToObject(food.position) <= radius:
                self.foods.pop(food)
                return food

        return None
