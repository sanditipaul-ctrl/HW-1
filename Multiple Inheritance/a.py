class Teacher:
    def __init__(self):
        self.teacher_id = input("Enter teacher id: ")
        self.teacher_name = input("Enter teacher name: ")
        self.qualification = input("Enter teacher qualificatiom: ")
        self.experience_years = input("Enter teacher experience years: ")

    def display_info(self):
        print(f"Teacher id: {self.teacher_id}\nTeacher name: {self.teacher_name}\nQualification: {self.qualification}\nExperience years: {self.experience_years}")
class Department:
    def __init__(self):
        self.department_name = input("Enter department name: ")
        self.office_room = input("Enter office room: ")

    def display_info(self):
        print(f"Department name: {self.department_name}\nOffice room: {self.office_room}")
class FacultyMember(Teacher,Department):
    def __init__(self):
        Teacher.__init__(self)
        Department.__init__(self)
        self.destination = input("Enter destination: ")

    def display_info(self):
        Teacher.display_info(self)
        Department.display_info(self)
        print(f"Destination: {self.destination}\nSalary: {self.salary}")

f1 = FacultyMember()
f1.display_info()
print("Thanks!")