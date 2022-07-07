# Module with different methods to find intersections
from queue import PriorityQueue
from geometry import myLine
# Main class for finding curves intersections
class Solver:

    # Constructor
    # In: paths - svg's paths from converter
    def __init__(self, paths):
        self.curves = []
        for path in paths:
            #path.approximate_arcs_with_quads()# not a bad idea to generalize all curves with Bezie
            for seg in path:
                self.curves.append(seg)

    # Function to find intersection between curves using svgtool lib
    # Out: nodes - list of complex numbers, representing intersections points
    def findIntersectionWithLib(self):
        i = 1
        intersections = []
        for part1 in self.curves:
            for part2 in self.curves[i:]:
                for p in part1.intersect(part2):
                    intersections.append(part1.point(p[0]))
            i = i + 1
        return intersections

    # Function to find intersection between lines using Bentley-Ottman algorithm
    # Out: nodes - list of tuples (x,y) - intersection points
    def findIntersectionWithBentleyOttmann(self):
        intersections = []
        # Initialize priority queue
        q = PriorityQueue()
        for curve in self.curves:
            q.put((curve.start.real, curve))
            q.put((curve.end.real, curve))

        line = myLine(self.curves[0])
        intersections.append(line.start.asComplex())
        return intersections
