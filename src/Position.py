import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distanceToObject(self, otherPosition):
    return math.dist([self.x, self.y], [otherPosition.x, otherPosition.y])


def angleToPoint(self, otherPoint):
    return math.atan((otherPoint.y - self.y) / (otherPoint.x - self.x))
