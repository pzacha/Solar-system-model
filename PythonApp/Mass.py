import numpy as np
import math
import matplotlib.pyplot as plt
import random

# Gravitational constant
grav_const = 6.674 * 10**(-11)
# Global mass list
mass_list = np.empty(0, dtype = object)
# Timestamp
timestamp = 3600
# Simulation length (in seconds) -> 2 years
sim_length = 31556926*2
# Screen max width and height (screen is square)
screen_size = 640
max_dist = 10 ** 12
# Random mass objects number
rand_mass_num = 1

class mass:
    """Mass (mass, xcor, ycor, xvel, yvel, xacc, yacc)"""

    def __init__(self, mass, xcor, ycor, xvel, yvel, xacc, yacc, name):
        self.mass = mass
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.xacc = xacc
        self.yacc = yacc
        self.name = name

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

    def calc_acceleration(self, mass_list):
        sum_force_x = 0
        sum_force_y = 0
        for obj in mass_list:
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

def create_mass_list(list):
    """Create mass list"""
    earth = mass(5.972 * (10 ** 24), 149600000000, 0, 0, 30000, 0, 0, 'Earth')
    sun = mass(1.989 * (10 ** 30), 0, 0, 0, 0, 0, 0, 'Sun')
    
    # Add Sun and Earth
    list = np.append(list, [sun, earth])

    # Add random objects
    for i in range(rand_mass_num):
        list = np.append(list, mass(random.randint(10 ** 15,10 ** 20), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 4,10 ** 4), random.randint(-10 ** 4,10 ** 4), 0, 0, 'Object' + str(i + 1)))
    return list