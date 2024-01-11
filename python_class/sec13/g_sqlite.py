import sqlite3
import json

con = sqlite3.connect(":memory:")
cur = con.cursor()

def create():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,     data JSON NOT NULL
        )
    """)

def insert():
    data = {
        "STUDENT": [
            {"NAME": "Dominica", "SCORE": {"KOR": 10, "ENG": 20, "MATH": 30}},
            {"NAME": "Dominico", "SCORE": {"KOR": 90, "ENG": 40, "MATH": 100}},
            {"NAME": "RuRe", "SCORE": {"KOR": 90, "ENG": 90, "MATH": 90}}
        ]
    }
    cur.execute("INSERT INTO students (data) VALUES (?)", (json.dumps(data),))
    con.commit()
def select():
    cur.execute("SELECT data FROM students")
    rows = cur.fetchall()
    for row in rows:
        json_data = json.loads(row[0])
        students = json_data.get("STUDENT", [])
        for student in students:
            name = student.get("NAME")
            score = student.get("SCORE")
            print(f"Name: {name}, Scores: {score}")


if __name__ == '__main__':
    create()
    insert()
    print("\n 전체 출력")
    select()
    cur.close()
    con.close()
