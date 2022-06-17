from __future__ import annotations

from Ant import Ant
from Position import Position
import WorldMap


class Nest:
    def __init__(
        self,
        position: Position,
        radius: float,
        worldMap: WorldMap.WorldMap,
        antsToSpawn: int = 0,
    ):
        self.position = position
        self.worldMap = worldMap
        if self.worldMap is not None:
            self.worldMap.nestPosition = self.position
        self.radius = radius
        self.antsToSpawn = antsToSpawn
        self.lifeCounter = 4

    @classmethod
    def emptyObject(self) -> Nest:
        return Nest(None, None, None, None)

    def __str__(self):
        return "<Nest: radius={0}, position={1}>".format(
            self.radius, self.position.__str__()
        )

    def update(self) -> None:
        ants = self.worldMap.ants
        for ant in ants:
            if ant.holding_food:
                if self.position.distanceToObject(ant.position) < self.radius:
                    ant.putDownFood()
                    print("Food delivered to the Nest by " + str(ant))

        self.lifeCounter += 1
        if self.lifeCounter % 4 == 0 and self.antsToSpawn > 0:
            self.spawnAnt(1)
            self.antsToSpawn -= 1

    def spawnAnt(self, amount=1) -> None:
        self.worldMap.addAnt(Ant(self.position.copy(), self.worldMap))
