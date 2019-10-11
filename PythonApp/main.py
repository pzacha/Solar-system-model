import numpy as np
import math
import matplotlib.pyplot as plt
import random
import sqlite3
from Mass import *
import SQL_fun

#Create mass objects
mass_list = create_mass_list(mass_list)

# Create database if none exists
SQL_fun.create_db()

# Connect to SQL database. (1 - start new db, 0 - load from db)
start_new = 1 
conn = sqlite3.connect('solar_system.db')
c = conn.cursor()
if start_new == 1:
    #c.execute("INSERT INTO solar_system VALUES (0, Earth , 149600000000, 0, 0, 30000)")
    c.execute("DELETE FROM solar_system")
#else:
    # Add last row values (iter and coords)
#iter = 0
for time in range(0, sim_length, timestamp):
    iter = iter + 1
    for obj in mass_list:
        # Calculate accelerartions
        obj.calc_acceleration(mass_list)
        # Update properties of each planet
        obj.update_velocity_and_coordinates()
        c.execute("INSERT INTO solar_system VALUES (?, ?, ?, ?, ?, ?)", (iter, obj.name, obj.xcor, obj.ycor, obj.xvel, obj.yvel))

#Commit changes and close connection
SQL_fun.commit_and_close(c, conn)

#TODO
#1. At the start of the program override database or continue from last point.
