# Main module of the program

from converter import Converter
from intersection import Solver
from geometry import myLine, Point
from SweepLine import SweepLine

if __name__ == '__main__':
    converter = Converter('data\lines.svg')
    solver = Solver(converter.paths)
    intersections = solver.findIntersectionWithExhaustive()
    converter.saveCurrentSvg('data\output.svg', nodes = intersections)

    #lines = []
    #lines.append(myLine(Point(-5, -5), Point(5,5)))
    #lines.append(myLine(Point(-5,5), Point(5,-5)))
    #lines.append(myLine(Point(-2,0), Point(0,2)))
    #lines.append(myLine(Point(0,0), Point(1,-1)))
    #lines.append(myLine(Point(-1,0), Point(2,-3)))
    #SL = SweepLine(lines)
    #SL.sweepIntersections()
    #print(SL.intersections)
    