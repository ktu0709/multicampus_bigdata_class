import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

#cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
cur.execute("SELECT * FROM polls_choice;")
tables = cur.fetchall()

for i in tables:
    print(i)