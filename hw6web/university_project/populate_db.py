import random
from faker import Faker
import psycopg2
from psycopg2.extras import execute_values

fake = Faker()

conn = psycopg2.connect("dbname=university_db user=postgres password=mypassword host=localhost")
cursor = conn.cursor()

def populate_database():
    groups = ["Group A", "Group B", "Group C"]
    execute_values(cursor, "INSERT INTO groups (name) VALUES %s", [(g,) for g in groups])

    teachers = [fake.name() for _ in range(4)]
    execute_values(cursor, "INSERT INTO teachers (name) VALUES %s", [(t,) for t in teachers])

    subjects = [("Math", 1), ("Physics", 2), ("Chemistry", 3), ("Biology", 4)]
    execute_values(cursor, "INSERT INTO subjects (name, teacher_id) VALUES %s", subjects)

    students = [(fake.name(), random.randint(1, len(groups))) for _ in range(30)]
    execute_values(cursor, "INSERT INTO students (name, group_id) VALUES %s", students)

    grades = [
        (random.randint(1, 30), random.randint(1, len(subjects)), random.randint(50, 100), fake.date_time_this_year())
        for _ in range(600)
    ]
    execute_values(cursor, "INSERT INTO grades (student_id, subject_id, grade, date) VALUES %s", grades)

    conn.commit()

populate_database()
cursor.close()
conn.close()
