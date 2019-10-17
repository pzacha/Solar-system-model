import numpy as np
import math
import matplotlib.pyplot as plt
import random
import globals
import sqlite3

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
        force = globals.grav_const * self.mass * obj.mass / (radius ** 2)
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
        self.xvel = self.xvel + self.xacc * globals.timestamp
        self.yvel = self.yvel + self.yacc * globals.timestamp
        self.xcor = self.xcor + self.xvel * globals.timestamp
        self.ycor = self.ycor + self.yvel * globals.timestamp

def create_mass_list(list):
    """Create mass list"""
    earth = mass(5.972 * (10 ** 24), 149600000000, 0, 0, 30000, 0, 0, 'Earth')
    sun = mass(1.989 * (10 ** 30), 0, 0, 0, 0, 0, 0, 'Sun')
    
    # Add Sun and Earth
    list = np.append(list, [sun, earth])

    # Add random objects
    for i in range(globals.rand_mass_num):
        list = np.append(list, mass(random.randint(10 ** 15,10 ** 20), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 4,10 ** 4), random.randint(-10 ** 4,10 ** 4), 0, 0, 'Object' + str(i + 1)))
    return list

def run_simulation():
    """Run simulation"""
    # Connect to database
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()

    iter = 0
    for time in range(0, globals.sim_length, globals.timestamp):
        iter = iter + 1
        for obj in globals.mass_list:
            # Calculate accelerartions
            obj.calc_acceleration(globals.mass_list)

            # Update properties of each planet
            obj.update_velocity_and_coordinates()

            # Save data in SQL database
            c.execute("INSERT INTO solar_system VALUES (?, ?, ?, ?, ?, ?)", (iter, obj.name, obj.xcor, obj.ycor, obj.xvel, obj.yvel,))

    # Commit changes and close connection
    conn.commit()
    c.close()
    conn.close()
    print("Simulation finished")