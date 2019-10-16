import numpy as np
import sqlite3

import globals

def create_solar_db():
    """SQL solar_system database creation"""
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS solar_system (
                iter INT,
                name CHAR,
                x FLOAT,
                y FLOAT,
                xvel FLOAT,
                yvel FLOAT
        )""")
    c.close()
    conn.close()

def commit_and_close(c, conn):
    """Commit changes and close connection"""
    conn.commit()
    c.close()
    conn.close()

def connect(start_new):
    """Connect to solar system database"""
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()
    if start_new == 1:
        #c.execute("INSERT INTO solar_system VALUES (0, Earth , 149600000000, 0, 0, 30000)")
        c.execute("DELETE FROM solar_system")
    #else:
        # Add last row values (iter and coords)
    return [c, conn]

def create_mass_names_db(mass_list):
    """SQL mass_name database creation"""
    conn = sqlite3.connect('mass_names.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS mass_names (name TEXT)""")
    # Make sure database is empty
    c.execute("DELETE FROM mass_names")
    # Save data in SQL database
    for obj in mass_list:
        c.execute("INSERT INTO mass_names VALUES (?)", (obj.name,))
    # Close connection and save database
    conn.commit()
    c.close()
    conn.close()

def get_mass_names():
    """Get mass names from database"""
    conn = sqlite3.connect('mass_names.db')
    c = conn.cursor()
    c.execute("SELECT * FROM mass_names")
    tab = c.fetchall()
    table = [i[0] for i in tab]
    c.close()
    conn.close()
    return table

def load_coords(name):
    """Load x coordinates to table"""
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()

    c.execute("SELECT x FROM solar_system WHERE name = (?)", (name,))
    x_cor = c.fetchall()
    x_float = [i[0] for i in x_cor]
    # Load y coordinates to table
    c.execute("SELECT y FROM solar_system WHERE name = (?)", (name,))
    y_cor = c.fetchall()
    y_float = [i[0] for i in y_cor]

    c.close()
    conn.close()
    return [x_float, y_float]

def create_coords_table():
    """Create table with coordinates and get iter value"""
    names = get_mass_names()
    coords_table = np.empty(0)
    for name in names:
        coords_table = np.append(coords_table, load_coords(name))
    return coords_table
# TODO
#1. Create list of list, not list of coords or take iter value simlength/timestamp

def test_num():
    globals.iter_num = globals.iter_num + 1