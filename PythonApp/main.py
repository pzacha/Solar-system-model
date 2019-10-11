import numpy as np
import math
import matplotlib.pyplot as plt
import random
import sqlite3
from Mass import *
import SQL_fun

# Create database if none exists
SQL_fun.create_db()

# Connect to SQL database. (1 - start new db, 0 - load from db)
start_new = 0 
conn_earth = sqlite3.connect('earth.db')
conn_sun = sqlite3.connect('sun.db')
c_e = conn_earth.cursor()
c_s = conn_sun.cursor()
if start_new == 1:
    c_e.execute("INSERT INTO earth_data VALUES (0, 149600000000, 0, 0, 30000)")
    c_s.execute("INSERT INTO sun_data VALUES (0, 0, 0, 0, 0)")

earth = mass(5.972 * (10 ** 24), 149600000000, 0, 0, 30000, 0, 0)
sun = mass(1.989 * (10 ** 30), 0, 0, 0, 0, 0, 0)

# Add Sun and Earth
list_of_objects = np.append(list_of_objects, [sun, earth])

# Add random objects
for i in range(0):
    list_of_objects = np.append(list_of_objects, mass(random.randint(10 ** 15,10 ** 20), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 4,10 ** 4), random.randint(-10 ** 4,10 ** 4), 0, 0))

iter = 0
for time in range(0, sim_length, timestamp):
    iter = iter + 1
    for obj in list_of_objects:
        # Calculate accelerartions
        obj.calc_acceleration()
        # Update properties of each planet
        obj.update_velocity_and_coordinates()
    c_e.execute("INSERT INTO earth_data VALUES (?, ?, ?, ?, ?)", (iter, earth.xcor, earth.ycor, earth.xvel, earth.yvel))
    c_s.execute("INSERT INTO sun_data VALUES (?, ?, ?, ?, ?)", (iter, sun.xcor, sun.ycor, sun.xvel, sun.yvel))

conn_earth.commit()
conn_sun.commit()
c_s.close()
conn_earth.close()
conn_sun.close()

#TODO
