import numpy as np
import math

# Gravitational constant
grav_const = 6.674 * 10**(-11)
# Global mass list
mass_list = np.empty(0, dtype = object)
# Timestamp
timestamp = 10
# Simulation length (in seconds) -> 1 years
sim_length = 31556926*1
# Screen max width and height (screen is square)
screen_size = 1080
max_dist = (10 ** 12) * 5
# Random mass objects number
rand_mass_num = 0
# Number of simulation iterations
iter_num = 0
