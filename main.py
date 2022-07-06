# Main module of the program

from converter import Converter
from intersection import Solver

if __name__ == '__main__':
    converter = Converter('data\lines.svg')
    solver = Solver(converter.paths)
    intersections = solver.findIntersectionWithLib()
    converter.saveCurrentSvg('data\output.svg', nodes = intersections)