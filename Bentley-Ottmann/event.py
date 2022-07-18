# Module for event class
from geometry import myLine, Point
import enum

# Event class type(enum)
class EventType(enum.Enum):
    Start = 1
    Intersection = 2
    End = 3

# Event class holds point position, value, lines of this event and type
class Event:

    # Construcor
    # in : type - EventType
    #      point - instance of Point
    #      lines - List of myLine
    def __init__(self, point : Point, type : EventType, lines):
        self.point = point
        self.type = type
        self.lines = lines
        self.value = point.x

    # Overrides
    def __repr__(self):
        return str(self.type) + ' (x = %s, y = %s)' % (self.point.x, self.point.y)

    def __eq__(self, other):
        if self is None or other is None:
            return False
        if self.type == other.type and self.point == other.point:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)