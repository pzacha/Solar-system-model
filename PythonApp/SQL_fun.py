import sqlite3

#SQL database initialization
def create_db():
    conn = sqlite3.connect('sun.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS sun_data (
                iter INT,
                x FLOAT,
                y FLOAT,
                xvel FLOAT,
                yvel FLOAT
        )""")
    c.close()
    conn.close()

    conn = sqlite3.connect('earth.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS earth_data (
                iter INT,
                x FLOAT,
                y FLOAT,
                xvel FLOAT,
                yvel FLOAT
        )""")
    c.close()
    conn.close()

# TODO
# 2. Function that deletes database
