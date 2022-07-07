# Module for sweep line data structure
from sortedcontainers import SortedSet, SortedDict
from geometry import Point, myLine, comparablePoint
from utility import approxEqual
from event import Event
from functools import cmp_to_key

# Class representing SweepLine - main class for Bentley-Ottmann algorithm
class SweepLine:

    @classmethod
    def fixDistances(self, point, T):
        comparablePoint = point
        T.update([])
        return T

    @classmethod
    def nearestLeft(self, line, T):
        prev = None
        for seg in T:
            if line == seg:
                return prev
            else:
                prev = seg
        return None

    @classmethod
    def nearestRight(self, line, T):
        prev = None
        for seg in T.__reversed__():
            if line == seg:
                return prev
            else:
                prev = seg
        return None

    @classmethod
    def nearestLeftForPoint(self, point, T):
        minDistance = None
        min = float('inf')
        for seg in T:
            if min > abs(seg.distance(point)) and seg.distance(point) >= 0:
                min = abs(seg.distance(point))
                minDistance = seg
        return minDistance

    @classmethod
    def nearestRightForPoint(self, point, T):
        minDistance = None
        min = float('inf')
        for seg in T:
            if min > abs(seg.distance(point)) and seg.distance(point) <= 0:
                min = abs(seg.distance(point))
                minDistance = seg
        return minDistance

    @classmethod
    def findNewEvent(self, line1, line2, point, SD):
        if line1 is not None and line2 is not None:
            intersectionPoint = line1.findIntersection(line2)
            if intersectionPoint is not None and intersectionPoint.y < point.y or \
                approxEqual(intersectionPoint.y, point.y) and intersectionPoint.x > point.x:
                if not SD.__contains__(intersectionPoint):
                    SD[intersectionPoint] = Event()
                return intersectionPoint
        return None

    @classmethod
    def sweepIntersections(self, lines):
        Q = SortedDict()
        for line in lines:
            if Q.__contains__(line.start):
                Q[line.start].lines.add(line)
            else:
                Q[line.start] = Event()
                Event.lines.append(line)
            if not Q.__contains__(line.end):
                Q[line.end] = Event()

        T = SortedSet()
        intersections = []
        while not len(Q) == 0:
            point, event = Q.popitem(index = 0)
            lower = []
            contain = []
            for line in T:
                if(line.end == point):
                    lower.append(line)
                elif line.checkPointIntersection(point) and line.start != point:
                    contain.append(line)
            #if len(event.lines) + len(lower) + len(contain) > 1:
            #    intersections.append(point)

            for line in lower:
                if line in T:
                    T.discard(line)

            contain.extend(event.lines)
            for line in event.lines:
                T.add(line)

            T = self.fixDistances(point, T)
            if len(contain) == 0:
                sl = self.nearestLeftForPoint(point, T)
                sr = self.nearestRightForPoint(point, T)
                i = self.findNewEvent(sl, sr, point, Q)
                intersections.append(i)
            else:
                comparablePoint = point
                contain.sort(key = cmp_to_key(lambda line1, line2: line1.findXCoord(comparablePoint) - line2.findXCoord(comparablePoint)))

                SP = contain[0]
                SPP = contain[-1]

                sl = self.nearestLeft(SP, T)
                sr = self.nearestRight(SPP, T)
                i = self.findNewEvent(SP, sl, point, Q)
                j = self.findNewEvent(SPP, sr, point, Q)
                if(i != j):
                    intersections.append(j)
                intersections.append(i)

        return intersections





