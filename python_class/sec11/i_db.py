import sqlite3
from dataclasses import dataclass

@dataclass
class Lang:
    name: str
    year: int

def adapt_lang(lang):
    return (lang.name, lang.year)
def convert_lang(value):
    return Lang(*value)



con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
sqlite3.register_adapter(Lang, adapt_lang)
sqlite3.register_converter("lang", convert_lang)
cur = con.cursor()
cur.execute("CREATE TABLE lang(name TEXT, year INTEGER)")
def insert_data(cur, data):
    for lang in data:
        cur.execute("INSERT INTO lang(name, year) VALUES (?, ?)", (lang.name, lang.year))
    con.commit()
def select_all(cur):
    cur.execute("SELECT * FROM lang")
    result = cur.fetchall()
    return [Lang(name=row[0], year=row[1]) for row in result]

if __name__ == '__main__':
    data = [
        Lang(name="C", year=1972),
        Lang(name="Fortran", year=1957),
        Lang(name="Python", year=1991),
        Lang(name="Go", year=2009),
    ]
    insert_data(cur, data)
    all_rows = select_all(cur)
    for row in all_rows:
        print(row)
