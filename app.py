

# Id number generator 
from pip import main


def id_generator(firstName):
    """Generates a unique id number for a student from a combination
     of the first name and a random number in the following format"""

    pass


class Student():
    """Student class"""

    def __init__(self, id, firstName, middleName,
    lastName, gender, age, email, phone, nationality, degree):
        self.id = id_generator(self.firstName)
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.gender = gender
        self.age = age
        self.email = email
        self.phone = phone
        self.Nationality = nationality
        self.degree = degree

    def __str__(self):
        student = """
        Student Name: {self.firstName} {self.middleName} {self.lastName}
        Gender: {self.gender}
        Age: {self.age}
        Contact: {self.phone} / {self.email} 
        Nationality: {self.Nationality}
        degree: {self.degree}
        """
        return student

def mainMenu():
    """menu items for user interation"""
    pass

if __name__ == '__main__':
    mainMenu()