import sqlite3  #sqlite3  CRUD

#1.연결   db 생성
conn  = sqlite3.connect("employee.db")
#2. 커서 생성
cursor   = conn.cursor()
#3. 테이블 생성    employees    id (pk, auto)  정수  , name  문자열  nn, age 정수 nn, city 문자열  nn
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        age   INTEGER NOT NULL, 
        city  TEXT NOT NULL
       )    
''')

#4.  insert_t, select, delete_t, update_t
def  insert_employees(name, age, city):
    cursor.execute('insert into employees ( name, age,city) values ( ?,?,?)',(name,age,city) )
    conn.commit()
def  selectall_employees():
    cursor.execute('select   * from  employees' )
    return cursor.fetchall()

def update_employees(id, name, age, city):
    #id로 찾아서 name,age,city로 변경하겠다
    cursor.execute('UPDATE employees SET name=?, age=?, city=? WHERE id=?', (name, age, city, id))
    conn.commit()
def  delete_employees(id):
    cursor.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()
#5. 실행 결과
#########insert

#insert_employees('홍길동1', 21, '서울1')
#insert_employees('홍길동2', 22, '서울2')
#insert_employees('홍길동3', 23, '서울3')

#print(selectall_employees())
#수정 : 번호로  이름 , 나이 , 주소 변경해보자.
#     1번 친구를   정길동   35  인천 으로 변경해 보자.
#update_employees(1 ,'정길동', 35, '인천')
#print(selectall_employees())
#delete_employees(1)
print(selectall_employees())



#6. conn. close()
conn.close()

