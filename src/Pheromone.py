from Position import Position
from PheromoneType import PheromoneType


class Pheromone:
    def __init__(
        self,
        pheromoneType: PheromoneType,
        position: Position,
        startingStrength: int = 100,
    ):
        self.pheromoneType = pheromoneType
        self.position = position
        self.strength = startingStrength


def getUnitedPheromoneAtCenterOfGravity(pheromones, type=PheromoneType.TRAIL):
    if len(pheromones) == 0:
        return

    x_sum = 0
    y_sum = 0
    strength_sum = 0

    for pheromone in pheromones:
        if pheromone.type == type:
            x_sum += pheromone.x * pheromone.strength
            y_sum += pheromone.y * pheromone.strength
            strength_sum += pheromone.strength

    return Pheromone(
        type, Position(x_sum / strength_sum, y_sum / strength_sum), strength_sum
    )
