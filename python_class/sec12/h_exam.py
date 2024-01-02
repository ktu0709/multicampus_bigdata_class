from mysql.connector import MySQLConnection
from dataclasses import dataclass

@dataclass
class Lang:  # 생성자, 소멸자, 연산자 재정의, __repr__
    name : str
    first_appeared: int

class LangDB:
    def __init__(self):
        self.con = MySQLConnection(user='root', password ='xodjs5575', database='my_emp')
        self.cur = self.con.cursor()

    def insert_data(self, data):
        self.cur.executemany("INSERT INTO lang VALUES(%s,%s)",[(lang.name , lang.first_appeared) for lang in  data])
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        result =[Lang(*row)   for  row  in   self.cur.fetchall()]
        return result

    def update_data(self, res:Lang):
        #year = int(year)
        self.cur.execute("UPDATE lang SET name = %s, first_appeared = %s  WHERE name = 'C'", (res.name, res.first_appeared))
        self.con.commit()

    '''
    def __del__(self):  #소멸자 추가
        self.con.close()
    '''
if __name__ == '__main__':
    data = [
        Lang("C", 1972),
        Lang(name= "Fortran", first_appeared=1957),
        Lang(name="Python", first_appeared=1991),
        Lang(name="Go", first_appeared=2009),
    ]

    lang_db = LangDB()
    lang_db.insert_data(data)
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)

    #lang_db.update_data('Java', 2008)
    lang_db.update_data(Lang(name='Java',first_appeared=2008))
    print('-------------')
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)


    del lang_db