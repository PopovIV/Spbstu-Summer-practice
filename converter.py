
#Module for parsing svg files into paths
#Currently using svgtool lib for that(will change later)

from svgpathtools import svg2paths2, concatpaths, Line, disvg
import json

# Class for data parsering and converting
class Converter:

    # Constructor
    # In: fileName - svg file name
    def __init__(self, fileName):
        self.paths, self.attributes, self.svg_attributes = svg2paths2(fileName)

    # Function to save svg with current paths
    # In: fileName - svg output file name
    #     nodes - list of complex numbers
    def saveCurrentSvg(self, fileName, nodes = None):
        # Delete inkscape json tags
        for attribute in self.attributes:
            if 'inkscape:path-effect' in attribute:
                del attribute ['inkscape:path-effect']
            if 'inkscape:original-d' in attribute:
                del attribute ['inkscape:original-d']
        # Save result
        disvg(self.paths, attributes = self.attributes, svg_attributes = self.svg_attributes, filename = fileName, nodes = nodes)
