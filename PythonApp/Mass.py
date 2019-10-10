import numpy as np
import math
import matplotlib.pyplot as plt
import random

# Gravitational constant
grav_const = 6.674 * 10**(-11)
# Global list of objects
list_of_objects = np.empty(0, dtype = object)
# Timestamp
timestamp = 60
# Simulation length (in seconds) -> 2 years
sim_length = 31556926*2
# Screen max width and height (screen is square)
screen_size = 640
max_dist = 10 ** 12

class mass:
    """Mass (mass, xcor, ycor, xvel, yvel, xacc, yacc)"""

    def __init__(self, mass, xcor, ycor, xvel, yvel, xacc, yacc):
        self.mass = mass
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.xacc = xacc
        self.yacc = yacc

    def calc_radius(self, obj):
        radius_x = obj.xcor - self.xcor
        radius_y = obj.ycor - self.ycor
        radius = math.sqrt(radius_x ** 2 + radius_y ** 2)
        return [radius_x, radius_y, radius]

    def calc_force(self, obj):

        [radius_x, radius_y, radius] = self.calc_radius(obj)
        force = grav_const * self.mass * obj.mass / (radius ** 2)
        force_x = force * (radius_x / radius)
        force_y = force * (radius_y / radius)
        return [force_x, force_y]

    def calc_acceleration(self):
        sum_force_x = 0
        sum_force_y = 0
        for obj in list_of_objects:
            if obj is self:
                continue
            [force_x, force_y] = self.calc_force(obj)
            sum_force_x = sum_force_x + force_x
            sum_force_y = sum_force_y + force_y
        self.xacc = sum_force_x / self.mass
        self.yacc = sum_force_y / self.mass


    def update_velocity_and_coordinates(self):
        self.xvel = self.xvel + self.xacc * timestamp
        self.yvel = self.yvel + self.yacc * timestamp
        self.xcor = self.xcor + self.xvel * timestamp
        self.ycor = self.ycor + self.yvel * timestamp

def norm_coords(coord):
    """ Adjust coordinates to screen (0,0) = middle of the screen """
    if coord == 0:
        # Middle of the screen
        coord = screen_size/2
    elif coord >= 0:
        # Right/top side of the screen
        # If absolute distance is bigger than max_dist show the planet on the edge of the screen
        if abs(coord) > max_dist:
            coord = screen_size
        else:
            coord = screen_size/2 + coord/max_dist*screen_size/2
    else:
        # Left/bottom side of the screen
        # If absolute distance is bigger than max_dist show the planet on the edge of the screen
        if abs(coord) > max_dist:
            # If distance is bigger than max_dist show the planet on the edge of the screen
            coord = 0
        else:           
            coord = screen_size/2 - abs(coord)/max_dist*screen_size/2       
    return int(round(coord))