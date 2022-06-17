from Position import Position
from quadTree.Rectangle import Rectangle


class QuadTree:
    def __init__(self, boundary, max_points=4, depth=0):
        """Initialize this node of the quadtree.

        boundary is a Rect object defining the region from which points are
        placed into this node; max_points is the maximum number of points the
        node can hold before it must divide (branch into four more nodes);
        depth keeps track of how deep into the quadtree this node lies.

        """

        self.boundary = boundary
        self.max_points = max_points
        self.points = []
        self.depth = depth
        # A flag to indicate whether this node has divided (branched) or not.
        self.divided = False

    def __str__(self):
        """Return a string representation of this node, suitably formatted."""
        sp = " " * self.depth * 2
        s = str(self.boundary) + "\n"
        s += sp + ", ".join(str(point) for point in self.points)
        if not self.divided:
            return s
        return (
            s
            + "\n"
            + "\n".join(
                [
                    sp + "nw: " + str(self.upperLeft),
                    sp + "ne: " + str(self.upperRight),
                    sp + "se: " + str(self.bottomRight),
                    sp + "sw: " + str(self.bottomLeft),
                ]
            )
        )

    def divide(self):
        """Divide the node by spawning four children nodes.

        The nodes are: `upperLeft`, `upperRight`, `bottomLeft`, `bottomRight`.
        """

        xCenter, yCenter = self.boundary.xCenter, self.boundary.yCenter
        width, height = self.boundary.width / 2, self.boundary.height / 2

        self.upperLeft = QuadTree(
            Rectangle(xCenter - width / 2, yCenter - height / 2, width, height),
            self.max_points,
            self.depth + 1,
        )
        self.upperRight = QuadTree(
            Rectangle(xCenter + width / 2, yCenter - height / 2, width, height),
            self.max_points,
            self.depth + 1,
        )
        self.bottomRight = QuadTree(
            Rectangle(xCenter + width / 2, yCenter + height / 2, width, height),
            self.max_points,
            self.depth + 1,
        )
        self.bottomLeft = QuadTree(
            Rectangle(xCenter - width / 2, yCenter + height / 2, width, height),
            self.max_points,
            self.depth + 1,
        )
        self.divided = True

    def insert(self, object):
        """Try to insert Object into this QuadTree.

        Object HAS to have a `.position` parameter of type `Position`.

        :returns: success of inserting the object into the node
        :rtype: boolean
        """

        if not self.boundary.contains(object.position):
            # The point does not lie inside boundary: bail.
            return False
        if len(self.points) < self.max_points:
            # There's room for our point without dividing the QuadTree.
            self.points.append(object)
            return True

        # No room: divide if necessary, then try the sub-quads.
        if not self.divided:
            self.divide()

        return (
            self.upperRight.insert(object)
            or self.upperLeft.insert(object)
            or self.bottomRight.insert(object)
            or self.bottomLeft.insert(object)
        )

    def query(self, boundary, found_objects, delete_condition_function=None):
        """Find the points in the quadtree that lie within boundary."""

        objectsToDelete = []

        # Search this node's points to see if they lie within boundary ...
        for objectA in self.points:
            point = objectA.position
            if boundary.contains(point):
                found_objects.append(objectA)
                if delete_condition_function is not None and delete_condition_function(
                    objectA
                ):
                    objectsToDelete.append(objectA)

        for objectA in objectsToDelete:
            self.points.remove(objectA)

        # ... and if this node has children, search them too.
        if self.divided:
            self.upperLeft.query(
                boundary,
                found_objects,
                delete_condition_function=delete_condition_function,
            )
            self.upperRight.query(
                boundary,
                found_objects,
                delete_condition_function=delete_condition_function,
            )
            self.bottomRight.query(
                boundary,
                found_objects,
                delete_condition_function=delete_condition_function,
            )
            self.bottomLeft.query(
                boundary,
                found_objects,
                delete_condition_function=delete_condition_function,
            )
        return found_objects

    def query_circle(
        self, boundary, centre, radius, found_objects, findAmount=999999, pop=False
    ):
        """Find the points in the quadtree that lie within radius of centre.

        boundary is a Rect object (a square) that bounds the search circle.
        There is no need to call this method directly: use query_radius.

        """

        # Search this node's points to see if they lie within boundary
        # and also lie within a circle of given radius around the centre point.
        pointsToDelete = []
        for objectA in self.points:
            point = objectA.position
            if (
                boundary.contains(point)
                and point.distanceToObject(Position(centre[0], centre[1])) <= radius
                and findAmount > 0
            ):
                findAmount -= 1
                found_objects.append(objectA)
                if pop:
                    pointsToDelete.append(objectA)

        for objectA in pointsToDelete:
            self.points.remove(objectA)

        # Recurse the search into this node's children.
        if self.divided and findAmount > 0:
            self.upperLeft.query_circle(
                boundary, centre, radius, found_objects, findAmount, pop
            )
            self.upperRight.query_circle(
                boundary, centre, radius, found_objects, findAmount, pop
            )
            self.bottomRight.query_circle(
                boundary, centre, radius, found_objects, findAmount, pop
            )
            self.bottomLeft.query_circle(
                boundary, centre, radius, found_objects, findAmount, pop
            )
        return found_objects

    def query_radius(self, centre, radius, found_objects, findAmount=999999, pop=False):
        """Find the points in the quadtree that lie within radius of centre."""

        # First find the square that bounds the search circle as a Rect object.
        boundary = Rectangle(*centre, 2 * radius, 2 * radius)
        return self.query_circle(
            boundary, centre, radius, found_objects, findAmount=findAmount, pop=pop
        )

    def __len__(self):
        """Return the number of points in the quadtree."""

        npoints = len(self.points)
        if self.divided:
            npoints += (
                len(self.upperLeft)
                + len(self.upperRight)
                + len(self.bottomRight)
                + len(self.bottomLeft)
            )
        return npoints

    def draw(self, ax):
        """Draw a representation of the quadtree on Matplotlib Axes ax."""

        self.boundary.draw(ax)
        if self.divided:
            self.upperLeft.draw(ax)
            self.upperRight.draw(ax)
            self.bottomRight.draw(ax)
            self.bottomLeft.draw(ax)
