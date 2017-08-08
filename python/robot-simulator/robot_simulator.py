
SOUTH = "SOUTH"
NORTH = "NORTH"
EAST = "EAST"
WEST = "WEST"

class Robot(object):
    def __init__(self,bearing=NORTH,coordinates1=0,coordinates2=0):
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2
        self.bearing = bearing
        self.coordinates = (self.coordinates1 , self.coordinates2)
    def turn_left(self):
        if self.bearing==NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = NORTH
    def turn_right(self):
        if self.bearing==NORTH:
            self.bearing = EAST
        elif self.bearing == WEST:
            self.bearing = NORTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == EAST:
            self.bearing =SOUTH

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates2 = self.coordinates2 + 1
        elif self.bearing == SOUTH:
            self.coordinates2 = self.coordinates2 - 1
        elif self.bearing == WEST :
            self.coordinates1 = self.coordinates1 - 1
        elif self.bearing == EAST :
            self.coordinates1 = self.coordinates1 + 1
        self.coordinates = (self.coordinates1 , self.coordinates2)

    def simulate(self,s):
        for i in s:
            if i == "L":
                self.turn_left()
            elif i == "R":
                self.turn_right()
            elif i == "A":
                self.advance()
        
        
