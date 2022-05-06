from Position import Position


class Food:
    def __init__(self, position: Position):
        self.position = position

    def __str__(self):
        return "<Food: position={}>".format(self.position.__str__())
