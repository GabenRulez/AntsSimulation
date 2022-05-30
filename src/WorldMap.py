import random
from Food import Food
import Pheromone
import Ant
import Position
import numpy as np


class WorldMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pheromones = []
        self.ants = []
        self.foods = []

    def __str__(self):
        return "<WorldMap: width={0}, height={1}, pheromonesAmount={2}, antsAmount={3}, foodsAmount={4}>".format(
            self.width,
            self.height,
            len(self.pheromones),
            len(self.ants),
            len(self.foods),
        )

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

    def limitAntPosition(self, ant: Ant.Ant):
        # Limit the position by map borders.
        wantedPosition = ant.position
        realisticPosition = Position.Position(
            min(max(wantedPosition.x, 0), self.width),
            min(max(wantedPosition.y, 0), self.height),
        )
        ant.position = realisticPosition

    def leapAntPosition(self, ant: Ant.Ant):
        '''If an Ant went over the border, teleport it to the other side of the map.'''
        wantedPosition = ant.position
        realisticPosition = Position.Position(
            wantedPosition.x%self.width,
            wantedPosition.y%self.height,
        )
        ant.position = realisticPosition

    def spawnFoodClump(
        self, position: Position.Position, amount: int, recoil: float = 25.0
    ):
        for _ in range(amount):
            food_x = position.x + np.random.uniform(low=-recoil, high=recoil)
            food_y = position.y + np.random.uniform(low=-recoil, high=recoil)

            food_position = Position.Position(food_x, food_y)
            self.foods.append(Food(food_position))

    def getFoodInRadius(self, midpoint: Position.Position, radius: float):
        # return single piece of food and delete it from self.foods
        for food in self.foods:
            if midpoint.distanceToObject(food.position) <= radius:
                self.foods.remove(food)
                return food

        return None
