from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector
from mysql.connector import MySQLConnection

#cnx = mysql.connector.connect(user='root', password ='xodjs5575', database='employees')
cnx =MySQLConnection(user='root', password ='xodjs5575', database='employees')
print(cnx , type(cnx))


print(cnx.get_server_info())
print(cnx.get_server_version())


cur =cnx.cursor(buffered=True)
cur.execute("select * from my_emp.emp")
res = cur.fetchall()

for r in res:
    print(r)
cur.close()
cnx.close()