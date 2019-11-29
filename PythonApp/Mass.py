import numpy as np
import math
import random
import globals
import sqlite3
import SQL_db

class mass:
    """Mass (mass, xcor, ycor, xvel, yvel, xacc, yacc)"""

    def __init__(self, mass, xcor, ycor, xvel, yvel, xacc, yacc, name, diameter):
        self.mass = mass
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.xacc = xacc
        self.yacc = yacc
        self.name = name
        self.diameter = diameter

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

def create_mass_list(new):
    """Create mass list"""

    # Make sure mass list is empty
    list = np.empty(0, dtype = object)

    if new == 1:
        sun = mass(1.989 * (10 ** 30), 0, 0, 0, 0, 0, 0, 'Sun', 10)
        # mercury = mass(0.330 * (10 ** 24), 57.9 * (10 ** 9), 0, 0, 47400, 0, 0, 'Mercury', 1)
        # venus = mass(4.87 * (10 ** 24), 108.2 * (10 ** 9), 0, 0, 35000, 0, 0, 'Venus', 3)
        earth = mass(5.972 * (10 ** 24), 149.6 * (10 ** 9), 0, 0, 29800, 0, 0, 'Earth', 3)
        # mars = mass(0.642 * (10 ** 24), 227.9 * (10 ** 9), 0, 0, 24100, 0, 0, 'Mars', 2)
        # jupiter = mass(1898 * (10 ** 24), 778.6 * (10 ** 9), 0, 0, 13100, 0, 0, 'Jupiter', 7)
        # saturn = mass(568 * (10 ** 24), 1433.5 * (10 ** 9), 0, 0, 9700, 0, 0, 'Saturn', 6)
        # uranus = mass(86.8 * (10 ** 24), 2872.5 * (10 ** 9), 0, 0, 6800, 0, 0, 'Uranus', 5)
        # neptune = mass(102 * (10 ** 24), 4495.1 * (10 ** 9), 0, 0, 5400, 0, 0, 'Neptune', 5)

        # Add Sun and Earth
        list = np.append(list, [sun, earth])

        # Add random objects
        for i in range(globals.rand_mass_num):
            list = np.append(list, mass(random.randint(10 ** 15,10 ** 23), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 4,10 ** 4), random.randint(-10 ** 4,10 ** 4), 0, 0, 'Object' + str(i + 1), 1))
        return list

    else:
        globals.iter_num = SQL_db.get_last_row('Sun')[0]
        sun = mass(1.989 * (10 ** 30), SQL_db.get_last_row('Sun')[1], SQL_db.get_last_row('Sun')[2], SQL_db.get_last_row('Sun')[3], SQL_db.get_last_row('Sun')[4], 0, 0, 'Sun', SQL_db.get_last_row('Sun')[6])
        # mercury = mass(0.330 * (10 ** 24), SQL_db.get_last_row('Mercury')[1], SQL_db.get_last_row('Mercury')[2], SQL_db.get_last_row('Mercury')[3], SQL_db.get_last_row('Mercury')[4], 0, 0, 'Mercury', SQL_db.get_last_row('Mercury')[6])
        # venus = mass(4.87 * (10 ** 24), SQL_db.get_last_row('Venus')[1], SQL_db.get_last_row('Venus')[2], SQL_db.get_last_row('Venus')[3], SQL_db.get_last_row('Venus')[4], 0, 0, 'Venus', SQL_db.get_last_row('Venus')[6])
        earth = mass(5.972 * (10 ** 24), SQL_db.get_last_row('Earth')[1], SQL_db.get_last_row('Earth')[2], SQL_db.get_last_row('Earth')[3], SQL_db.get_last_row('Earth')[4], 0, 0, 'Earth', SQL_db.get_last_row('Earth')[6])
        # mars = mass(0.642 * (10 ** 24), SQL_db.get_last_row('Mars')[1], SQL_db.get_last_row('Mars')[2], SQL_db.get_last_row('Mars')[3], SQL_db.get_last_row('Mars')[4], 0, 0, 'Mars', SQL_db.get_last_row('Mars')[6])
        # jupiter = mass(1898 * (10 ** 24), SQL_db.get_last_row('Jupiter')[1], SQL_db.get_last_row('Jupiter')[2], SQL_db.get_last_row('Jupiter')[3], SQL_db.get_last_row('Jupiter')[4], 0, 0, 'Jupiter', SQL_db.get_last_row('Jupiter')[6])
        # saturn = mass(568 * (10 ** 24), SQL_db.get_last_row('Saturn')[1], SQL_db.get_last_row('Saturn')[2], SQL_db.get_last_row('Saturn')[3], SQL_db.get_last_row('Saturn')[4], 0, 0, 'Saturn', SQL_db.get_last_row('Saturn')[6])
        # uranus = mass(86.8 * (10 ** 24), SQL_db.get_last_row('Uranus')[1], SQL_db.get_last_row('Uranus')[2], SQL_db.get_last_row('Uranus')[3], SQL_db.get_last_row('Uranus')[4], 0, 0, 'Uranus', SQL_db.get_last_row('Uranus')[6])
        # neptune = mass(102 * (10 ** 24), SQL_db.get_last_row('Neptune')[1], SQL_db.get_last_row('Neptune')[2], SQL_db.get_last_row('Neptune')[3], SQL_db.get_last_row('Neptune')[4], 0, 0, 'Neptune', SQL_db.get_last_row('Neptune')[6])
    
        # Add Sun and Earth
        list = np.append(list, [sun, earth])

        # Add random objects
        for i in range(globals.rand_mass_num):
            list = np.append(list, mass(float(SQL_db.get_last_row('Object' + str(i + 1))[5]), SQL_db.get_last_row('Object' + str(i + 1))[1], SQL_db.get_last_row('Object' + str(i + 1))[2], SQL_db.get_last_row('Object' + str(i + 1))[3], SQL_db.get_last_row('Object' + str(i + 1))[4], 0, 0, 'Object' + str(i + 1), 1))
        return list

def run_simulation(db_density):
    """Run simulation"""
    # Connect to database
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()

    density_iter = db_density - 1
    sim_iter = globals.iter_num + 1
    for _ in range(0, globals.sim_length, globals.timestamp):
        density_iter = density_iter + 1
        for obj in globals.mass_list:
            # Calculate accelerartions
            obj.calc_acceleration(globals.mass_list)

            # Update properties of each planet
            obj.update_velocity_and_coordinates()

            # Save data in SQL database
            if density_iter == db_density:
                c.execute("INSERT INTO solar_system VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sim_iter, obj.name, obj.xcor, obj.ycor, obj.xvel, obj.yvel, str(obj.mass), obj.diameter,))
        if density_iter == db_density:
            sim_iter = sim_iter + 1
            density_iter = 0

    # Commit changes and close connection
    conn.commit()
    c.close()
    conn.close()
    print("Simulation finished")