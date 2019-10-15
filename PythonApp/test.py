import sqlite3
import numpy as np
import SQL_db
import Mass

mass_list = np.empty(0, dtype = object)
mass_list = Mass.create_mass_list(mass_list)
SQL_db.create_mass_name_db(mass_list)


