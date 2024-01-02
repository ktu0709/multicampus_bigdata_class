import sqlite3
import datetime
def adapt_date(date_obj):
    return date_obj.strftime('%Y-%m-%d')

def convert_date(s):
    return datetime.datetime.strptime(s.decode('utf-8'),'%Y-%m-%d').date()

sqlite3.register_adapter(datetime.date, adapt_date) #python -> sql로 변환할 때 사용되는 함수
sqlite3.register_adapter('DATE', convert_date) # sql -> python

'''
detect_types = sqllite3.PARSE_DECLTYPES : 테이블 생성시 정의된 데이터 기반으로 converter 하곘다
                                          m_data DATE;
               sqlite3.PARSE_COLNAMES : 쿼리결과의 열 이름에 명시된 데이터 타입을 기반으로 converter하곘다
                                        select my_clo as "my_clo [DATE] ~~"
'''

#conn = sqlite3.connect('example.db')
conn = sqlite3.connect('example.db',detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (date_column DATE)")

today = datetime.date.today()
cur.execute("INSERT INTO test (date_column) VALUES (?)", (today,))

res = cur.execute('select * from test')
rows = res.fetchall()

for row in rows:
    print(row)
    print(row[0],type(row[0]))
conn.close()
