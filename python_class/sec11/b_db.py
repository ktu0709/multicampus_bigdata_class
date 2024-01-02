import sqlite3
import datetime
import my

#connect () 데이터 베이스에 연결
# ":memory:" -> 특수 문자열 ,실제 데이터 베이스가 디스크의 실제 파일이 아닌 RAM에 생성 및 저장된다.

# detect_types -> 데이터 유형을 제어하는 처리 방법

# sqlite3.PARSE_DECLTYPES  : sqlite3 모듈이 [create table문]에서 선언된 유형을 기반으로 열의 데이터를  [자동감지]
#                                   create table test( m   DATE) -> python datetime.date


# sqlite3.PARSE_COLNAMES  : 열의 유형을 자동감지  date  ,  timestamp  -> 쿼리 결과 [select]로 탐지
#                           date라고 선언하게되면 sqlite3의 date 타입으로 처리한다.
#                       select hire_date  As res from emp;  ->  python datetime.date


# date,timestamp 으로 선언을 하게 되면  python의 datetime모듈의  객체로 관리된다.

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(d date, ts timestamp)")  #-> python datetime모듈의 객체로 인지 하겠다.

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

con.close()