import numpy as np
import math
import sqlite3
import matplotlib.pyplot as plt
import random
import globals
import SQL_db
from Mass import *
import display

# Create mass objects
globals.mass_list = create_mass_list(globals.mass_list)
# Create database with mass names
SQL_db.create_mass_names_db(globals.mass_list)

# Create database if none exists
SQL_db.create_solar_db()

# Connect to SQL database. (1 - start new db, 0 - load from db)
start_new = 1
[c, conn] = SQL_db.connect(start_new)

# Run simulation
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
SQL_db.commit_and_close(c, conn)

#TODO
#1. At the start of the program override database or continue from last point.
#2. Interface and workflow
