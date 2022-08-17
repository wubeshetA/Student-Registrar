"""module to that interact with the sqlite3 database"""

import sqlite3

# database name
db_name = "student.db"

# SQL queries
CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS student
(id TEXT, first_name TEXT, middle_name TEXT, last_name TEXT,
gender TEXT, age INTEGER, email TEXT, mobile TEXT,
nationality TEXT, degree TEXT) """

INSERT_STUDENT = """ INSERT INTO student (id, first_name, middle_name,
last_name, gender, age, email, mobile, nationality, degree)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

SELECT_STUDENT = """ SELECT * FROM student WHERE id = ? """

UPDATE_STUDENT = """ UPDATE student SET first_name = ?, middle_name = ?,
last_name = ?, gender = ?, age = ?, email = ?, mobile = ?,
nationality = ?, degree = ? WHERE id = ? """

DELETE_STUDENT = """ DELETE FROM student WHERE id = ? """

SELECT_ALL = """ SELECT * FROM student """


# Create a new database if the database doesn't already exist
def create_database(db_name):
    """Create a new database if it doesn't exist"""
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE)
        connection.commit()
    except Exception:
        print("Can't add New Student")
    finally:
        connection.close()

# add student to database


def add_student(db_name, student):
    """Add student information to the database"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(INSERT_STUDENT, (student.id, student.firstName,
                                    student.middleName, student.lastName,
                                    student.gender, student.age, student.email,
                                    student.phone, student.nationality,
                                    student.degree))
    connection.commit()
    connection.close()


# get student by id
def getStudent(db_name, id):
    """Get student information by id from the database"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(SELECT_STUDENT, (id,))
    result = cursor.fetchone()
    connection.close
    return result


# get all students
def get_students():
    """Get all student"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL)
    result = cursor.fetchall()
    return result


def updateStudent(db_name, id, data):
    """Update student information with new information provided"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(UPDATE_STUDENT, (data['firstName'], data['middleName'],
                                    data['lastName'], data['gender'],
                                    data['age'], data['email'],
                                    data['phone'], data['nationality'],
                                    data['degree'], id))
    connection.commit()
    connection.close()


def deleteStudent(db_name, id):
    """Delete student from the database"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(DELETE_STUDENT, (id,))
    connection.commit()
    connection.close()
