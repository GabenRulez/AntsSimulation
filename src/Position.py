import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Position: x=" + str(self.x) + ", y=" + str(self.y) + ">"

    def add(self, x, y):
        self.x += x
        self.y += y

    def distanceToObject(self, otherPosition):
        return math.dist([self.x, self.y], [otherPosition.x, otherPosition.y])

    def angleToPoint(self, otherPoint):
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

    def pointAtAngle(self, angle, distance):
        diff_x = distance * math.cos(angle)
        diff_y = distance * math.sin(angle)

        return Position(self.x + (distance*diff_x), self.y + (distance*diff_y))
