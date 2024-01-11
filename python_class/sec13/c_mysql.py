import sqlite3  #sqlite3  CRUD  -> class로 변형  / 입출력 객체를 생성해서  사용한다.
from  dataclasses import dataclass
import mysql.connector
@dataclass
class Employee:
    id : int
    name:str
    age :int
    city : str

class EmployeeDB:
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'xodjs5575',
            'host': '127.0.0.1',
            'database': 'my_emp',
            'raise_on_warnings': False
        }
        self.conn  = mysql.connector.connect(**config)
        self.cursor  = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS employees")
        self.cursor.execute('''
            CREATE TABLE  employees (
                id    INT PRIMARY KEY AUTO_INCREMENT, 
                name  VARCHAR(50) NOT NULL,       
                age   INT NOT NULL, 
                city  VARCHAR(50) NOT NULL
               )    
        ''')
        self.conn.commit();
#4.  insert_t, select, delete_t, update_t
    def  insert_employees(self,employee : Employee):
        self.cursor.execute('insert into employees ( name, age,city) values ( %s,%s,%s)'
                            ,(employee.name,employee.age,employee.city) )
        self.conn.commit()

    def  selectall_employees(self):   # def test(*tupletype, **dicttype):...  test(1,2,3,4)
        self.cursor.execute('select   * from  employees' )
        rows = self.cursor.fetchall()  # [여러개의 행을 튜플로 리턴]
        #Employee(*row)  : row 각 튜플()에서  값을 압축 해제하고 클래스 생성자에게 인수로 전달한다.
        #데이터베이스에 리턴된 튜플의 목록에서 Employee 객체 목록으로 변환해서 리턴한다.
        return    [ Employee(*row)  for row in rows]  #rows[ ('홍길동1', 21, '서울1'),(),(),,]

    def  update_employees(self,employee : Employee):
        self.cursor.execute('UPDATE employees SET name=%s, age=%s, city=%s WHERE id=%s',
                            (employee.name, employee.age, employee.city, employee.id))
        self.conn.commit()
    def  delete_employees(self,id):
        self.cursor.execute('DELETE FROM employees WHERE id=%s', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
        db  = EmployeeDB()
        db.insert_employees(Employee(None,'홍길동1', 21, '서울1'))
        db.insert_employees(Employee(None,'홍길동2', 22, '서울2'))
        db.insert_employees(Employee(None,'홍길동3', 23, '서울3'))
        print("After insert :")
        print(db.selectall_employees())
        #수정 : 번호로  이름 , 나이 , 주소 변경해보자.
        #     1번 친구를   정길동   35  인천 으로 변경해 보자.
        print("After Update :")
        db.update_employees(Employee(3 ,'정길동', 35, '인천'))
        print(db.selectall_employees())

        print("After delete :")
        db.delete_employees(2)
        print(db.selectall_employees())



