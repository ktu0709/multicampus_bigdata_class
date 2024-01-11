import mysql.connector
from dataclasses import dataclass
@dataclass
class Lang:
    name: str
    year: int
class DBManager:
    def __init__(self, config):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS lang(
            name VARCHAR(255),  year INT
        )  """)


    def insert_data(self, data):
        for lang in data:
            self.cursor.execute("""
            INSERT INTO lang(name, year) VALUES (%s, %s)
            """, (lang.name, lang.year))
        self.conn.commit()

    def select_all(self):
        self.cursor.execute("SELECT * FROM lang")
        result = self.cursor.fetchall()
        return [Lang(name=row[0], year=row[1]) for row in result]

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'my_emp',
    }
    db_manager = DBManager(config)
    data = [
        Lang(name="C", year=1972),
        Lang(name="Fortran", year=1957),
        Lang(name="Python", year=1991),
        Lang(name="Go", year=2009),
    ]
    db_manager.insert_data(data)
    all_rows = db_manager.select_all()
    for row in all_rows:
        print(row)
