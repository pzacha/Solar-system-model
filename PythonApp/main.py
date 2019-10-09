import numpy as np
import math
import matplotlib.pyplot as plt
import random
import sqlite3

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

#SQL database initialization
conn = sqlite3.connect('earth.db')
c = conn.cursor()
