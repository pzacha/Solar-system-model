import sqlite3

#SQL database initialization
def create_db():
    conn = sqlite3.connect('sun.db')
    c = conn.cursor()
    c.execute("""create table sun_data (
                iter int,
                x float,
                y float,
                xvel float,
                yvel float
        )""")
    conn.close()

    conn = sqlite3.connect('earth.db')
    c = conn.cursor()
    c.execute("""create table earth_data (
                iter int,
                x float,
                y float,
                xvel float,
                yvel float
        )""")
    conn.close()

# TODO
# 1. Function that checks if database exists
# 2. Function that deletes database


#c.execute("SELECT x FROM earth_data")
#test = c.fetchall()
#print(test)