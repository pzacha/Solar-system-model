import sqlite3

conn = sqlite3.connect('solar_system.db')
c = conn.cursor()

c.execute("SELECT x FROM solar_system")
x_cor = c.fetchall()
#c.fetchall("SELECT x FROM solar_system WHERE name = (?)", (object))
y = [i[0] for i in x_cor]
print(y)