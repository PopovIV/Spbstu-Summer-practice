# Main module of the program

from converter import Converter
from intersection import Solver
from geometry import myLine, Point
from SweepLine import *

if __name__ == '__main__':
    #converter = Converter('data\lines.svg')
    #solver = Solver(converter.paths)
    #intersections = solver.findIntersectionWithBentleyOttmann()
    #converter.saveCurrentSvg('data\output.svg', nodes = intersections)
    lines = []
    lines.append(myLine(Point(-1,-1), Point(1,1)))
    lines.append(myLine(Point(-1,-2), Point(2,1)))
    lines.append(myLine(Point(-1,-5), Point(1,5)))
    lines.append(myLine(Point(0,1), Point(2,-1)))
    SL = SweepLine()
    print(SL.sweepIntersections(lines))
    