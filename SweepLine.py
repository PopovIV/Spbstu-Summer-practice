# Module for sweep line data structure
from queue import PriorityQueue
from sortedcontainers import SortedSet
from geometry import Point, myLine
from utility import approxEqual
from event import Event, EventType

# Class representing SweepLine - main class for Bentley-Ottmann algorithm
class SweepLine:

    # Constructor
    # In: lines - list of myLine instances
    def __init__(self, lines):
        self.Q = PriorityQueue()
        self.T = SortedSet()
        self.intersections = []
        # Fill queue with points 
        for line in lines:
            self.Q.put(Event(line.start, EventType.Start, [line]))
            self.Q.put(Event(line.end, EventType.End, [line]))

    # Function to find the greatest element in this set which is strictly less than the given element
    # in: line - instance of myLine
    # out: closest below line or None
    def nearestBelow(self, line):
        prev = None
        for seg in self.T:
            if line == seg:
                return prev
            else:
                prev = seg
        return None

    # Function to find the smallest element in this set which is strictly greater than the given element
    # In: line - instance of myLine
    # Out: closest below line or None
    def nearestHigher(self, line):
        prev = None
        for seg in self.T.__reversed__():
            if line == seg:
                return prev
            else:
                prev = seg
        return None

    # Function to recalculate values in lines
    # In: location - X-coordinate of point
    def recalculate(self, location : float):
        for line in self.T:
            line.calculateValue(location)
        self.T.update([])#

    # Function to find and end intersection to Q
    # In: line1, line2 - instances of myLine class
    #     location - current location of sweep line
    # Out: True, if there was intersection. False, otherwise
    def reportIntersection(self, line1 : myLine, line2 : myLine, location : float):
        intersection = line1.findIntersection(line2)
        if intersection != None and intersection.x > location:
            self.Q.put(Event(intersection, EventType.Intersection, [line1, line2]))
            return True
        return False

    # Function to remove duplicate intersections
    # In: line1, line2 - instances of myLine class
    # Out: True, if there was intersection. False, otherwise
    def removeEvent(self, line1 : myLine, line2 : myLine):
        for event in self.Q.queue:
            if event.type == EventType.Intersection:
                if (event.lines[0] == line1 and event.lines[1] == line2) or\
                    (event.lines[0] == line2 and event.lines[1] == line1):
                    self.Q.queue.remove(event)
                    return True
        return False

    # Function to swap two lines in T
    # In: line1, line2 - instances of myLine class
    def swap(self, line1, line2):
        #self.T.discard(line1)
        #self.T.discard(line2)
        # bad
        for line in self.T:
            if line == line1 or line2 == line:
                self.T.discard(line)
        value = line1.value
        line1.value = line2.value
        line2.value = value
        self.T.add(line1)
        self.T.add(line2)

    # Function to find all intersections:
    def sweepIntersections(self):
        while not self.Q.empty():
            event = self.Q.get()
            location = event.value

            if event.type == EventType.Start:
                self.recalculate(location)
                for line in event.lines:
                    self.T.add(line)
                    r = self.nearestBelow(line)
                    if r != None:
                        self.reportIntersection(r, line, location)
                    t = self.nearestHigher(line)
                    if t != None:
                        self.reportIntersection(t, line, location)
                    if t != None and r != None:
                        self.removeEvent(r, t)

            elif event.type == EventType.End:
                for line in event.lines:
                    r = self.nearestBelow(line)
                    t = self.nearestHigher(line)
                    if t != None and r != None:
                        self.reportIntersection(r, t, location)
                        self.T.discard(line)

            elif event.type == EventType.Intersection:
                line1 = event.lines[0]
                line2 = event.lines[1]
                self.swap(line1, line2)

                if line1.value < line2.value:
                    t = self.nearestHigher(line1)
                    r = self.nearestBelow(line2)
                    if t != None:
                        self.reportIntersection(t, line1, location)
                        self.removeEvent(t, line2)
                    if r != None:
                        self.reportIntersection(r, line2, location)
                        self.removeEvent(r, line1)
                else:
                    t = self.nearestHigher(line2)
                    r = self.nearestBelow(line1)
                    if t != None:
                        self.reportIntersection(t, line2, location)
                        self.removeEvent(t, line1)
                    if r != None:
                        self.reportIntersection(r, line1, location)
                        self.removeEvent(r, line2)
                self.intersections.append([event.point, line1, line2])





