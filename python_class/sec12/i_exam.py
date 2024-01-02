import mysql.connector
from dataclasses import dataclass
@dataclass
class Lang:
    name: str
    year: int

class LangDB:
    def __init__(self, user, password, database):
        self.con = mysql.connector.connect(user=user, password=password, database=database)
        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS lang")
        self.cur.execute("CREATE TABLE  lang(name VARCHAR(50), year INTEGER)")

    def insert_data(self, data):
        for lang in data:
            self.cur.execute("INSERT INTO lang(name, year) VALUES (%s, %s)", (lang.name, lang.year))
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        result = self.cur.fetchall()
        return [Lang(name=row[0], year=row[1]) for row in result]

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    db = LangDB('root', 'xodjs5575', 'my_emp')
    data = [
        Lang(name="C", year=1972),
        Lang(name="Fortran", year=1957),
        Lang(name="Python", year=1991),
        Lang(name="Go", year=2009),
    ]
    db.insert_data(data)
    all_rows = db.select_all()
    for row in all_rows:
        print(row)
    del db