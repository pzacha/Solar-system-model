import sqlite3

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

def commit_and_close(cursor, connection):
    """Commit changes and close connection"""
    connection.commit()
    cursor.close()
    connection.close()

def connect(start_new):
    """Connect to database"""
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()
    if start_new == 1:
        #c.execute("INSERT INTO solar_system VALUES (0, Earth , 149600000000, 0, 0, 30000)")
        c.execute("DELETE FROM solar_system")
    #else:
        # Add last row values (iter and coords)
    return [c, conn]

def load_coords(c, conn, object):
    """Load x coordinates to table"""
    c.execute("SELECT x FROM solar_system WHERE name = (?)", (object))
    x_cor = c.fetchall()
    x_float = [i[0] for i in x_cor]
    # Load y coordinates to table
    c.execute("SELECT y FROM solar_system WHERE name = (?)", (object))
    y_cor = c.fetchall()
    y_float = [i[0] for i in y_cor]
    return [x_float, y_float]

def create_mass_name_db(mass_list):
    """SQL mass_name database creation"""
    conn = sqlite3.connect('mass_names.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS mass_names (name TEXT)""")
    # Make sure database is empty
    #c.execute("DELETE FROM mass_names")
    # Save data in SQL database
    for obj in mass_list:
        c.execute("INSERT INTO mass_names VALUES (?)", (obj.name,))
    # Close connection and save database
    conn.commit()
    c.close()
    conn.close()
# TODO
#c.execute("SELECT x FROM earth_data")
