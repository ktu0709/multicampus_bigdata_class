import sqlite3
con = sqlite3.connect("abc.db")
print(type(con))
cur=con.cursor()
#cur.execute("create table movie(title,year,score)")
insert_sql = "insert into movie values(1,1,1)"
cur.execute(insert_sql)
con.commit()

select_sql = "select * from movie"
res = cur.execute(select_sql)
print(res.fetchone())
con.close()