"""A menu driven CLI application that used to register students information
to a database and read information from the database."""

import database
from database import create_database, db_name
import random


def generateId(student):
    """Generates a unique id number for a student from a combination
    of the first name initial and a random number."""
    id = student.firstName[0] + str(random.randint(1000, 9999))
    return id


class Student():
    """Student class"""

    def __init__(self, firstName, middleName,
                 lastName, gender, age, email, phone, nationality, degree):

        self.id = None
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.gender = gender
        self.age = age
        self.email = email
        self.phone = phone
        self.nationality = nationality
        self.degree = degree

    def __str__(self):
        student = """
        ============================ {} {} ===============================\n
                            Full Name: {} {} {}
                            Gender: {}
                            Age: {}
                            Contact: {} / {}
                            Nationality: {}
                            Degree: {}
        """.format(str(self.firstName).upper(), str(self.lastName).upper(),
                   self.firstName, self.middleName, self.lastName,
                   self.gender,
                   self.age,
                   self.email, self.phone,
                   self.nationality, self.degree)

        return student


def addStudent():

    firstName = input("Enter first name: ")
    middleName = input("Enter middle name: ")
    lastName = input("Enter last name: ")
    gender = input("Enter gender: ")
    age = int(input("Enter age:"))
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    nationality = input("Enter nationality: ")
    degree = input("Enter degree: ")
    new_student = Student(firstName, middleName, lastName,
                          gender, age, email, phone, nationality, degree)
    new_student.id = generateId(new_student)

    # excute database operation

    database.add_student(db_name, new_student)
    print("New student has been added successfully!")
    response = input("Do you want do Another operation? yes/no")
    if response.lower() == "yes":
        mainMenu()
    else:
        exit()


def updateStudent():
    id = input("Enter student id: ")
    new_data = {
        "firstName": input("Enter new first name: "),
        "middleName": input("Enter new middle name: "),
        "lastName": input("Enter new last name: "),
        "gender": input("Enter new gender: "),
        "age": int(input("Enter new age: ")),
        "email": input("Enter new email: "),
        "phone": input("Enter new phone number: "),
        "nationality": input("Enter new nationality: "),
        "degree": input("Enter new degree: "),
    }
    database.updateStudent(db_name, id, new_data)


def getStudent():
    """get student by id"""
    id = input("Enter student id: ")
    # get all the info for a student info from the database by it's id
    student_info = database.getStudent(db_name, id)
    # create a new student object with the data above
    student = Student(student_info[1], student_info[2], student_info[3],
                      student_info[4], student_info[5], student_info[6],
                      student_info[7], student_info[8], student_info[9])
    print(student)
    # print the student.
    response = input("Do you want do Another operation? yes/no")
    if response.lower() == "yes":
        mainMenu()
    else:
        exit()


def deleteStudent():
    """delete student by it's id"""
    pass

    id = input("Enter student id: ")
    # get student name by it's id and store it in studentName variable
    student = database.getStudent(db_name, id)
    if student is None:
        print("There is no student with such id")
        response = input("Do you want do Another operation? yes/no")
        if response.lower() == "yes" or response.lower == "y":
            mainMenu()
    else:
        studentName = student[1] + " " + student[2]
        response = input(f"Are you sure you want remove '{studentName}' "
                         "permanently? (yes/no) ")
        # if respose is yes proceed to deletion
        if response.lower() == "yes":
            database.deleteStudent(db_name, id)
            print(f"Student {studentName} has been deleted successfully")

        else:
            print("Deletion canceled!")
            exit()


def getAllStudents():
    """get all students"""
    # get all students from the database
    # iterate through the students and display all the students info as follow
    print("Here are the details of the students: ")
    all_students = database.get_students()
    print("\n===================== ALL STUDENTS ============================")
    header = "ID\tFull Name\t\tE-mail\t\t\t\tMajor"
    print(header)
    print("--\t---------\t\t------\t\t\t\t-----")
    for student in all_students:
        student_info = f"{student[0]}\t{student[1]} {student[2]}\t\t"\
            f"{student[6]}\t\t{student[9]}"
        print(student_info)
    response = input("Do you want do Another operation? yes/no: ")
    if response.lower() == "yes":
        mainMenu()
    else:
        exit()


def choices():
    print("1. Add a new student")
    print("2. Update a student")
    print("3. Delete a student")
    print("4. Get a student by id")
    print("5. Get all students")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice


def mainMenu():
    create_database(db_name)
    """menu items for user interaction"""
    # print(s)
    print("============ STUDENT REGISTRATION =============")
    print("Let's know what you want to do")

    choice = choices()

    if choice == 1:
        addStudent()
    elif choice == 2:
        updateStudent()
    elif choice == 3:
        deleteStudent()
    elif choice == 4:
        getStudent()
    elif choice == 5:
        getAllStudents()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        response = input("Do you still want to continue? yes/no")
        if response.lower() == "yes":
            mainMenu()
        else:
            exit()


if __name__ == '__main__':
    mainMenu()
