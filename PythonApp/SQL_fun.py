import sqlite3

#SQL database initialization
def create_db():
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

#Commit changes and close connection
def commit_and_close(cursor, connection):
    connection.commit()
    cursor.close()
    connection.close()

def connect(start_new):
    conn = sqlite3.connect('solar_system.db')
    c = conn.cursor()
    if start_new == 1:
        #c.execute("INSERT INTO solar_system VALUES (0, Earth , 149600000000, 0, 0, 30000)")
        c.execute("DELETE FROM solar_system")
    #else:
        # Add last row values (iter and coords)
    return [c, conn]

def load_coords(c, conn, object):
    x_cor = c.fetchall("SELECT x FROM solar_system WHERE name = (?)", (object))
    y_cor = c.fetchall("SELECT y FROM solar_system WHERE name = (?)", (object))
    return [x_cor, y_cor]

# TODO
#c.execute("SELECT x FROM earth_data")
