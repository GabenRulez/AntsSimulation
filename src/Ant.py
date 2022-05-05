from AntsSimulation.src.Pheromone import getUnitedPheromoneAtCenterOfGravity
from WorldMap import WorldMap
from Position import Position
import math


class Ant:
    def __init__(self, position: Position, worldMap: WorldMap):
        self.pos = position
        self.sense_angle = 60
        self.walking_speed = 100
        self.direction = 0
        # self.age = 0
        self.holding_food = False
        self.worldMap  =  worldMap

    def update(self):
        # Na podstawie czy self.holding_food = True - wybierz kierunek do domu lub kierunek do jedzenia
        # Rusz się self.move(kierunek)
        # Spróbuj podnieść jedzenie
        # Na podstawie tego, czy TERAZ masz jedzenie, stwórz odpowiedniego feromona
        # self.age +=1
        pass

    def setMap(self, worldMap: WorldMap):
        self.worldMap = worldMap

    def decide(self, pheromoneList):
        # take self.holding_food = False into consideration
        # Detect pheromones in cone shape in front of the ant.
        # Take the angle from ant's `self.sense_angle`.
        sensedPheromones = self.worldMap.getPheromonesInCircularSector()
        pheromoneCenter = getUnitedPheromoneAtCenterOfGravity(sensedPheromones)



        # Roll a dice and depending on the result:
        # Go right
        # Go left
        # Go towards the center of trail pheromones (towards food)
        # - this option should have the biggest chance of happening
        # If you have food go towards the center of "return to base pheromones"

        # Return the angle of "desired movement"
        # Use this getPheromonesInCircularSector(self, startingPoint, direction, range)


        pass

    def move(self, direction):
        # wywołaj move na mapie

        # (Possible in the future) Check for obstacles on your path.

        # Create a "move" vector depending on the "direction" and "walking_speed" constant.
        # The "walking_speed" depends on whether the ant holds food.
        # (Possible in the future) The "walking_speed" depends on the ant's age.
        # (Possible in the future) The "walking_speed" depends on the angle of the terrain.
        # (Possible in the future) The "walking_speed" depends on the wind.

        # Spawn a "ReturnPheromone" or "FoodPheromone" depending on the current state of "holding_food".

        # self.map.updateAntPosition(self, wantedPosition)
        pass

    def mark_food_trail(self):
        # Invoke when you have found food.
        # It will be used in order for other ants to find the food more optimally.

        # Spawn a "FoodPheromone" object.
        # This object will have lifespan that will gradually go down until it disappears.

        # self.map.addPheromone(typ ...
        pass

    def mark_return_trail(self):
        # Invoke when you are looking for food.
        # It will be used in order to find optimal return path to the nest.

        # Spawn a "ReturnPheromone" object.
        # This object will have lifespan that will gradually go down until it disappears.
        # self.map.addPheromone(typ ...
        pass

    def takeFood(self):
        # foodToEat = self.map.getFoodInRadius(self, position:Position, radius:float)
        # if the foodToEat is not null - change your type to "carrying food= true"
        # else do nothing
        pass

    def putDownFood(self):
        self.holding_food = False
