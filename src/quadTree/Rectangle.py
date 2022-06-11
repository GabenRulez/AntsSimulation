from src import Position


class Rectangle:
    """A rectangle centred at (`xCenter`, `yCenter`) with `width` and `height`."""

    def __init__(self, xCenter, yCenter, width, height):
        self.xCenter, self.yCenter = xCenter, yCenter
        self.width, self.height = width, height
        self.leftEdge, self.rightEdge = xCenter - width / 2, xCenter + width / 2
        self.topEdge, self.bottomEdge = yCenter - height / 2, yCenter + height / 2

    def __str__(self):
        return "<Rectangle: leftEdge={0}, topEdge={1}, rightEdge={2}, bottomEdge={3}>".format(
            self.leftEdge,
            self.topEdge,
            self.rightEdge,
            self.bottomEdge,
        )

    def contains(self, position: Position.Position):
        """Is a `position` inside the span of this Rectangle?"""
        return (
            self.leftEdge <= position.x < self.rightEdge
            and self.topEdge <= position.y < self.bottomEdge
        )
