import numpy as np


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getDistanceBetweenPoints(point1:Position, point2: Position):
    x_diff = point1.x - point2.x
    y_diff = point1.y - point2.y

    return np.sqrt(x_diff^2 + y_diff^2)