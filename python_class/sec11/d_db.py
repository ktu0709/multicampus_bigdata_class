import sqlite3
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")
def insert_data(data):
    cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)
    con.commit();

def select_all():
    cur.execute("SELECT * FROM lang")
    result = cur.fetchall()
    return result

def update_data(name, year):
    cur.execute("ALTER TABLE lang ADD COLUMN year INTEGER")
    #year = int(year)
    cur.execute("UPDATE lang SET name = ?, year = ?  WHERE name = 'C'" , (name,year))
    con.commit()

if __name__ == '__main__':
    data = [{"name": "C", "year": 1972},
            {"name": "Fortran", "year": 1957},
            {"name": "Python", "year": 1991},
            {"name": "Go", "year": 2009},
            ]
    insert_data(data)
    all= select_all()
    for  row in all :
        print( f'{row[0]:<10} \t {row[1]:<15}')


    update_data('Java',2008);  #name c를 찾아서  각각 변경을 해본다.
    print('-------------')
    all = select_all()
    for row in all:
        print(row)
