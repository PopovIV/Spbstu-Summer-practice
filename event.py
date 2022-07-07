# Module for event class

# Event class representing one point 
class Event:
    lines = []

    # Construcor
    # in : line - myLine instance
    def __init__(self, line : myLine):
        self.lines.append(line)