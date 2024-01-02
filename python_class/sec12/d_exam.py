import sqlite3
from mysql.connector import MySQLConnection

con =MySQLConnection(user='root', password ='xodjs5575', database='my_emp')
cur= con.cursor()
cur.execute("drop table if exists lang ")
cur.execute("create table lang(name varchar(20),first_appeared int)")
def insert_data(data):
    formatted_data = [(d['name'],d['year']) for d in data]
    cur.executemany("INSERT INTO lang VALUES(%s, %s)", formatted_data)
    con.commit();

def select_all():
    cur.execute("SELECT * FROM lang")
    result = cur.fetchall()
    return result

def update_data(name, year):
    cur.execute("ALTER TABLE lang ADD COLUMN year INTEGER")
    #year = int(year)
    cur.execute("UPDATE lang SET name = %s, year = %s  WHERE name = 'C'" , (name,year))
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

    update_data('java',2008)

    all= select_all()
    for  row in all :
        print( f'{row[0]:<10} \t {row[1]:<15}')