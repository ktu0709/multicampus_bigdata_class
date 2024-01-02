import sqlite3
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

data = (   {"name": "C", "year": 1972},
           {"name": "Fortran", "year": 1957},
           {"name": "Python", "year": 1991},
           {"name": "Go", "year": 2009},
        )
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

params = (1972,'Python')
#cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
#cur.execute("SELECT * FROM lang")
cur.execute("SELECT * FROM lang WHERE first_appeared = ? or name = ?", params)
print(cur.fetchall())

con.close()
