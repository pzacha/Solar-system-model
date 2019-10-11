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
start_new = 1 
conn = sqlite3.connect('earth.db')
c = conn.cursor()
if start_new == 1:
    c.execute("INSERT INTO earth_data VALUES (0, 149600000000, 0, 0, 30000)")

earth = mass(5.972 * (10 ** 24), 149600000000, 0, 0, 30000, 0, 0)
sun = mass(1.989 * (10 ** 30), 0, 0, 0, 0, 0, 0)

# Add Sun and Earth
list_of_objects = np.append(list_of_objects, [sun, earth])

# Add random objects
for i in range(2):
    list_of_objects = np.append(list_of_objects, mass(random.randint(10 ** 15,10 ** 20), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 11,10 ** 11), random.randint(-10 ** 4,10 ** 4), random.randint(-10 ** 4,10 ** 4), 0, 0))

iter = 0
for time in range(0, sim_length, timestamp):
    iter = iter + 1
    for obj in list_of_objects:
        # Calculate accelerartions
        obj.calc_acceleration()
        # Update properties of each planet
        obj.update_velocity_and_coordinates()
    c.execute("INSERT INTO earth_data VALUES (?, ?, ?, ?, ?)", (iter, earth.xcor, earth.ycor, earth.xvel, earth.yvel))

conn.commit()
c.close()
conn.close()
#c.execute("SELECT x FROM earth_data")

#TODO cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
# 1. Create variables for saving coordinates
# 2. Save coordinates to SQL db (pickle?)