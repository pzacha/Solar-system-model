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

# TODO
#c.execute("SELECT x FROM earth_data")
# 2. Function that deletes database
