import sqlite3

#SQL database initialization
conn = sqlite3.connect('sun.db')
c = conn.cursor()
c.execute("""CREATE TABLE sun_data (
            x float,
            y float,
            xvel float,
            yvel float
    )""")
conn.close()

conn = sqlite3.connect('earth.db')
c = conn.cursor()
c.execute("""CREATE TABLE earth_data (
            x float,
            y float,
            xvel float,
            yvel float
    )""")

