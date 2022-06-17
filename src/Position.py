from __future__ import annotations

import math


class Position:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Position: x=" + str(self.x) + ", y=" + str(self.y) + ">"

    def get(self) -> (float, float):
        return (self.x, self.y)

    def add(self, addedToX, addedToY) -> Position:
        self.x += addedToX
        self.y += addedToY
        return self

    def copy(self) -> Position:
        return Position(self.x, self.y)

    def distanceToObject(self, otherPosition) -> float:
        return math.dist([self.x, self.y], [otherPosition.x, otherPosition.y])

    def angleToPoint(self, otherPoint) -> float:
        try:
            tempAngle = math.atan((otherPoint.y - self.y) / (otherPoint.x - self.x))
            if otherPoint.x < self.x:
                return tempAngle + math.pi
            else:
                if otherPoint.y < self.y:
                    return tempAngle + 2 * math.pi
                else:
                    return tempAngle
        except ZeroDivisionError:
            if otherPoint.y > self.y:
                return math.pi / 2
            else:
                return 3 * math.pi / 2

    def pointAtAngle(self, angle: float, distance: float =1) -> Position:

        return Position(self.x + (distance * diff_x), self.y + (distance * diff_y))
