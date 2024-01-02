import sqlite3
class LangDB:
    def __init__(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.execute("CREATE TABLE lang(name, first_appeared)")

    def insert_data(self, data):
        self.cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        result = self.cur.fetchall()
        return result

    def update_data(self, name, year):
        year = int(year)
        self.cur.execute("UPDATE lang SET name = ?, first_appeared = ?  WHERE name = 'C'", (name, year))
        self.con.commit()

    def __del__(self):  #소멸자 추가
        self.con.close()

if __name__ == '__main__':
    data = [
        {"name": "C", "year": 1972},
        {"name": "Fortran", "year": 1957},
        {"name": "Python", "year": 1991},
        {"name": "Go", "year": 2009},
    ]

    lang_db = LangDB()
    lang_db.insert_data(data)
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)

    lang_db.update_data('Java', 2008)
    print('-------------')
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)


