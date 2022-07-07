# Module with different geometry classes(Point, Line, Bezier curves and Arcs)

from svgpathtools import Line
from utility import approxEqual

# Class representing point
class Point:

    # Constructor
    # In: x - X-coordinate
    #     y - Y-coordinate
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overrides
    def __repr__(self):
        return 'Point (x = %s, y = %s)' % (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        if self is None or other is None:
            return False
        if approxEqual(self.x, other.x) and approxEqual(self.y, other.y):
            return True

    def __lt__(self, other):
        if self.y > other.y or approxEqual(self.y, other.y) and self.x < other.x:
            return True
        return false

    def __ne__(self, other):
        return not (self == other)

    # Function to transform point to complex format
    # x + iy
    # out: complex number
    def asComplex(self):
        return complex(self.x, self.y)

    # Function to calculate magnitude of point
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

# Function to calculate vector product of two vectors(Points)
# in: first, second - Points
def vecProduct(first : Point, second : Point):
    return first.x * second.y - first.y * second.x

# Class representing Line
class myLine:

    # Constructors
    # In: start - start Point
    #     end - end Point
    def __init__(self, start : Point, end : Point):
        # Firstly compare y's
        if (start.y > end.y or approxEqual(start.y, end.y)) and start.x < end.x:
            self.start = start
            self.end = end
        else:
            self.end = start
            self.start = end

    # In: Line - svgtoolslib Line class instance
    def __init__(self, line : Line):
        start = Point(line.start.real, line.start.imag)
        end = Point(line.end.real, line.end.imag)
        if (start.y > end.y or approxEqual(start.y, end.y)) and start.x < end.x:
            self.start = start
            self.end = end
        else:
            self.end = start
            self.start = end

    # Overrides
    def __repr__(self):
        return 'myLine (start = (%s, %s), end = (%s, %s))' % (self.start.x, self.start.y, self.end.x, self.end.y)

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not (self == other)

    #def __lt__(self, other):
    #    if self.

    # Function to find X-coordinate by Point p y's coordinate
    # in: point - Point instance
    #     below - step
    # out: closest X-coordinate
    #def findXCoord(self, point : Point, below = 0.00005):
    #    y = point.y - below
    #    p = self.end - self.start
    #    t = (y - self.start.y) / p.y
    #    return t * p.x + start.x

    # Function to find distance between line and point
    # in: point - Point instance
    # out: distance between line and point
    def distance(point):
        p1 = self.end - self.start
        p2 = point - self.start
        return vecProduct(p1, p2) / p1.length()

    # Function to check intersection with other line
    # in: other - instance of myLine to check intersection with
    # out: bool - True, if there is intersection. False, otherwise
    def checkIntersection(self, other):
        p1 = self.end - self.start
        p2 = other.end - other.start
        # here happens linear magic with checking for collinear using smth like this
        # t = (other.start - start) * p1 / (p1 * p2)
        # u = (other.start - start) * p2 / (p1 * p2)
        rxs = vecProduct(p1, p2)
        if approxEqual(rxs, 0):
            return False
        u = vecProduct(self.start - other.start, p1) / -rxs
        t = vecProduct(other.start - self.start, p2) / rxs
        return u >= 0 and u <= 1 and t >= 0 and t <= 1

    # Function to check if point is on line
    # in: point - Point instance
    # out: bool - True, if tpoint is on line. False, otherwise
    def checkPointIntersection(self, point):
        p1 = self.end - self.start
        p2 = point - self.start
        # Firstly check for collinear
        if (approxEqual(p1.x, 0) and pproxEqual(p2.x, 0) and p1.y > point.y) or \
            (approxEqual(p1.y, 0) and pproxEqual(p2.y, 0) and p1.y > point.y):
            return True
        return (p2.x / p1.x, p2.y / p1.y)

    # Function to find intersection point with other line
    # in: other - instance of myLine to check intersection with
    # out: intersection point, if there is intersection. None, otherwise
    def findIntersection(self, other):
        if other is None or not checkIntersection(other):
            return None
        p1 = self.end - self.start
        p2 = other.end - other.start
        rxs = vecProduct(p1, p2)
        t = vecProduct(other.start - self.start, p2) / rxs
        return self.start + Point(t * p1.x, t * p1.y)