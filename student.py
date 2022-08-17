class Student():
    """Represent a student"""

    def __init__(self, firstName, middleName,
                 lastName, gender, age, email, phone, nationality, degree):
        """Initialized student class"""
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

        """Return string representation of student instance."""
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
