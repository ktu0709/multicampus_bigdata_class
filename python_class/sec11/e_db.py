import sqlite3  #sqlite3  CRUD  -> class로 변형

class EmployeeDB: #db인 스키마는 사용자로 전달받아 생성 / 테이블은 employees로 클래스의 create_table(self)에서 만들겠다
    def __init__(self, db_name):
       self. conn  = sqlite3.connect(db_name)
       self. cursor   =self. conn.cursor()
       self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id    INTEGER PRIMARY KEY AUTOINCREMENT, 
                name  TEXT NOT NULL,       
                age   INTEGER NOT NULL, 
                city  TEXT NOT NULL
               )    
        ''')
        self.conn.commit();
#4.  insert_t, select, delete_t, update_t
    def  insert_employees(self,name, age, city):
        self.cursor.execute('insert into employees ( name, age,city) values ( ?,?,?)',(name,age,city) )
        self.conn.commit()
    def  selectall_employees(self):
        self.cursor.execute('select   * from  employees' )
        return self.cursor.fetchall()
    def  update_employees(self,id, name, age, city):
        self.cursor.execute('UPDATE employees SET name=?, age=?, city=? WHERE id=?', (name, age, city, id))
        self.conn.commit()
    def  delete_employees(self,id):
        self.cursor.execute('DELETE FROM employees WHERE id=?', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
        db  = EmployeeDB("emp.db")
        db.insert_employees('홍길동1', 21, '서울1')
        db.insert_employees('홍길동2', 22, '서울2')
        db.insert_employees('홍길동3', 23, '서울3')
        print("After insert :")
        print(db.selectall_employees())
        #수정 : 번호로  이름 , 나이 , 주소 변경해보자.
        #     1번 친구를   정길동   35  인천 으로 변경해 보자.
        print("After Update :")
        db.update_employees(3 ,'정길동', 35, '인천')
        print(db.selectall_employees())

        print("After delete :")
        db.delete_employees(2)
        print(db.selectall_employees())



