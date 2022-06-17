import numpy as np
import WorldMap
from Pheromone import (
    Pheromone,
    calculatePheromonesStrength,
)
import Position
from PheromoneType import PheromoneType


class Ant:
    def __init__(self, position: Position, worldMap: WorldMap):
        self.position = position
        self.direction = np.random.uniform(low=-np.pi, high=np.pi)
        self.walkingSpeed = 10

        self.seeing_radius = 200
        self.seeing_angle = 150

        self.eating_radius = 10
        self.holding_food = False

        self.markingCycle = 4
        self.lifeCounter = np.random.randint(self.markingCycle)

        self.worldMap = worldMap

    def __str__(self):
        return "<Ant: walkingSpeed={0}, direction={1}, seeingRadius={2}, seeingAngle={3}, eatingRadius={4}, holdingFood={5}, lifeCounter={6}, position={7}>".format(
            self.walkingSpeed,
            self.direction,
            self.seeing_radius,
            self.seeing_angle,
            self.eating_radius,
            self.holding_food,
            self.lifeCounter,
            self.position.__str__(),
        )

    def update(self) -> None:
        """
        Life cycle function of the `Ant`. Triggered every simulation frame to let the `Ant` think, move, eat, etc.
        """
        self.tryToTakeFood()
        self.move(self.decide())
        self.lifeCounter += 1

        if self.lifeCounter % self.markingCycle == 0:
            self.mark_pheromones()

    def decide(self) -> float:
        """
        Calculate an angle with a bit of randomness. Moving in this direction should yield a big chance of encountering the requested type of `Pheromones`.
        """

        # Base your decision on whether you're holding food or not.
        # If you are, then you should try to find a way to the nest.
        # Otherwise, try to find a way to get closer to the food.

        if self.holding_food:
            pheromoneToTrack = PheromoneType.HOME
        else:
            # If you can detect food, then this is the direction you should go. If you can't, then you should follow the pheromones.
            detectedFood = self.worldMap.getFoodInRadius(
                self.position, self.seeing_radius
            )
            if detectedFood is not None:
                return self.position.angleToPoint(detectedFood.position)
            else:
                pheromoneToTrack = PheromoneType.FOOD

        # Search in 3 circular shapes: on the left, in front of and on the right.
        # Choose direction which has the most pheromones.

        a = np.sin(np.radians(self.seeing_angle / 6)) * self.seeing_radius

        frontSensorAngle = self.direction
        frontSensorPosition = self.position.pointAtAngle(
            frontSensorAngle, self.seeing_radius
        ).pointAtAngle(frontSensorAngle + np.pi, a / 2)
        frontSensorPheromones = self.worldMap.getPheromonesInCircle(
            frontSensorPosition, a / 2
        )
        frontSensorStrength = calculatePheromonesStrength(
            startingPosition=self.position,
            pheromones=frontSensorPheromones,
            trackedType=pheromoneToTrack,
        )

        leftSensorAngle = frontSensorAngle + np.radians(self.seeing_angle) / 3
        leftSensorPosition = self.position.pointAtAngle(
            leftSensorAngle, self.seeing_radius
        ).pointAtAngle(leftSensorAngle + np.pi, a / 2)
        leftSensorPheromones = self.worldMap.getPheromonesInCircle(
            leftSensorPosition, a / 2
        )
        leftSensorStrength = calculatePheromonesStrength(
            startingPosition=self.position,
            pheromones=leftSensorPheromones,
            trackedType=pheromoneToTrack,
        )

        rightSensorAngle = frontSensorAngle - np.radians(self.seeing_angle) / 3
        rightSensorPosition = self.position.pointAtAngle(
            rightSensorAngle, self.seeing_radius
        ).pointAtAngle(rightSensorAngle + np.pi, a / 2)
        rightSensorPheromones = self.worldMap.getPheromonesInCircle(
            rightSensorPosition, a / 2
        )
        rightSensorStrength = calculatePheromonesStrength(
            startingPosition=self.position,
            pheromones=rightSensorPheromones,
            trackedType=pheromoneToTrack,
        )

        if (
            frontSensorStrength > leftSensorStrength
            and frontSensorStrength > rightSensorStrength
        ):
            return frontSensorAngle + np.random.uniform(
                low=-np.pi / 16, high=np.pi / 16
            )

        elif leftSensorStrength > rightSensorStrength:
            return leftSensorAngle + np.random.uniform(low=-np.pi / 16, high=np.pi / 16)

        elif rightSensorStrength > leftSensorStrength:
            return rightSensorAngle + np.random.uniform(
                low=-np.pi / 16, high=np.pi / 16
            )

        else:
            return self.direction + np.random.uniform(low=-np.pi / 8, high=np.pi / 8)

    def move(self, moveDirection) -> None:
        """
        Change the `Ant`'s position, by supplying the "move vector angle". The length of the vector will be `self.walkingSpeed`.
        :param moveDirection: The angle in radians.
        """
        self.position = self.position.pointAtAngle(moveDirection, self.walkingSpeed)
        self.worldMap.limitAntPosition(self)
        # self.worldMap.leapAntPosition(self)
        self.direction = moveDirection

    def mark_pheromones(self) -> None:
        """
        Function that marks with the correct type of `Pheromone` based on `Ant`'s `holding_food` state.
        """
        if self.holding_food:
            self.mark_food_trail()
        else:
            self.mark_return_trail()

    def mark_food_trail(self) -> None:
        """
        Triggers the `worldMap` to spawn a `FOOD` type pheromone at current position.
        """
        self.worldMap.addPheromones(Pheromone(PheromoneType.FOOD, self.position))

    def mark_return_trail(self) -> None:
        """
        Triggers the `worldMap` to spawn a `HOME` type pheromone at current position.
        """
        self.worldMap.addPheromones(Pheromone(PheromoneType.HOME, self.position))

    def tryToTakeFood(self) -> None:
        """
        Looks for food in a circle around the `Ant`. The radius is defined as `self.eating_radius`. If the food is found, the `Ant`'s state changes to `holding_food = True`.
        """
        # foodToEat = self.map.getFoodInRadius(self, position:Position, radius:float)
        # if the foodToEat is not null - change your type to "carrying food= true"
        # else do nothing
        foodToEat = self.worldMap.getFoodInRadius(self.position, self.eating_radius)

        if foodToEat:
            self.holding_food = True
            self.direction += np.pi

    def putDownFood(self) -> None:
        """
        Changes the state of the `Ant` to `holding_food = False`.
        """
        self.holding_food = False
