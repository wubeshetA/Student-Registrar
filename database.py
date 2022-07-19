import sqlite3

# SQL queries
CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS student 
(id INTEGER PRIMARY KEY, first_name TEXT, middle_name TEXT, last_name TEXT,
gender TEXT, age INTEGER, email TEXT, mobile TEXT,  Nationality TEXT) """

INSERT_STUDENT = """ INSERT INTO student (first_name, middle_name, last_name, gender, age, email, mobile, Nationality) VALUES (?, ?, ?, ?, ?, ?, ?, ?) """
SELECT_STUDENT = """ SELECT * FROM student WHERE id = ? """
UPDATE_STUDENT = """ UPDATE student SET first_name = ?, middle_name = ?, last_name = ?, gender = ?, age = ? email = ?, mobile = ?, Nationality = WHERE id = ? """
DELETE_STUDENT = """ DELETE FROM student WHERE id = ? """
SELECT_ALL = """ SELECT * FROM student """ 

# Create a new database if the database doesn't already exist
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(CREATE_TABLE)
    conn.commit()
    conn.close()


# get student by name

# get all list of students

# add student to database

# update student in database

# remove student from database

