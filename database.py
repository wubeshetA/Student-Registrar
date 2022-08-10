import sqlite3

# database name
db_name = "student.db"

# SQL queries
CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS student 
(id TEXT, first_name TEXT, middle_name TEXT, last_name TEXT,
gender TEXT, age INTEGER, email TEXT, mobile TEXT,  nationality TEXT, degree TEXT) """

INSERT_STUDENT = """ INSERT INTO student (id, first_name, middle_name, last_name, gender, age, email, mobile, nationality, degree) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

SELECT_STUDENT = """ SELECT * FROM student WHERE id = ? """
UPDATE_STUDENT = """ UPDATE student SET first_name = ?, middle_name = ?, last_name = ?, gender = ?, age = ? email = ?, mobile = ?, Nationality = WHERE id = ? """
DELETE_STUDENT = """ DELETE FROM student WHERE id = ? """
SELECT_ALL = """ SELECT * FROM student """ 


# Create a new database if the database doesn't already exist
def create_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute(CREATE_TABLE)
        conn.commit()
    except:
        print("Can't add New Student")
    finally:
        conn.close()

# add student to database
def add_student(db_name, student):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(INSERT_STUDENT, (student.id, student.firstName,
    student.middleName, student.lastName, student.gender, student.age,
    student.email, student.phone, student.nationality, student.degree))
    conn.commit()
    conn.close()


# get student by id
def getStudent(db_name, id):
    pass

# get all students
def get_students():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(SELECT_ALL)
    rows = c.fetchall()
    # conn.close()
    # return rows
    for row in rows:
        print(row)

def updateStudent(db_name, id):
    pass

# delete student from database by id
def deleteStudent(db_name, id):
    pass

