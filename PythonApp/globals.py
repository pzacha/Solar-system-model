import numpy as np
import math

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
# Number of simulation iteration
#global iter_num
iter_num = 0
