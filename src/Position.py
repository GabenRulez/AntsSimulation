import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distanceToObject(self, otherPosition):
        return math.dist([self.x, self.y], [otherPosition.x, otherPosition.y])


    def angleToPoint(self, otherPoint):
        tempAngle = math.atan((otherPoint.y - self.y)/(otherPoint.x - self.x))
        if otherPoint.x < self.x:
            return tempAngle + math.pi
        else:
            if otherPoint.y < self.y:
                return tempAngle + 2*math.pi
            else:
                return tempAngle
