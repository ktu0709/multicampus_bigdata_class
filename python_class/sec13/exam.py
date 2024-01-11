import csv
import pandas as pd
from mysql.connector import MySQLConnection

#1
class EmployeeDB:
    def __init__(self, param1,param2,param3):
       self.conn  = MySQLConnection(user=param1, password =param2, database=param3)
       self.cursor   =self. conn.cursor()

    def selectall_emp(self):
           self.cursor.execute('select   * from  emp')
           rows = self.cursor.fetchall()
           return [row for row in rows]

    def selectall_dept(self):
           self.cursor.execute('select   * from  dept')
           rows = self.cursor.fetchall()
           return [row for row in rows]

    def selectall_salgrade(self):
           self.cursor.execute('select   * from  salgrade')
           rows = self.cursor.fetchall()
           return [row for row in rows]



if __name__ == '__main__':
    my_emp_db = EmployeeDB('root','xodjs5575','my_emp')
    emp_res = my_emp_db.selectall_emp()
    dept_res = my_emp_db.selectall_dept()
    salgrade_res = my_emp_db.selectall_salgrade()

    print(emp_res)
    print(dept_res)

    emp_column =['emp_no','ename','job','mgr','hiredate','sal','comm','deptno']
    dept_column = ['deptno','dname','loc']
    salgrade_column = ['grade', 'losal', 'hisal']

    with open('emp_res.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(emp_column)
        writer.writerows(emp_res)  # 행 데이터를 쓴다.

    with open('dept_res.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(dept_column)
        writer.writerows(dept_res)  # 행 데이터를 쓴다.

    with open('salgrade_res.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(salgrade_column)
        writer.writerows(salgrade_res)  # 행 데이터를 쓴다.




    del(my_emp_db)


