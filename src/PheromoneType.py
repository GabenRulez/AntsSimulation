from enum import Enum


class PheromoneType(Enum):
    HOME = 0  # When going from home
    TRAIL = 1  # When found food
