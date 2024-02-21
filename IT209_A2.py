# Name: Sujan Acharya, Date: 02/13/2024, purpose: A2 Student class definition and methods.


class Student:  # class definition
    totalEnrollment = 0

    def __init__(self, name, major='IST', enrolled='y', credits=0, qpoints=0):  # constructor
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints

        Student.totalEnrollment += 1  # increment totalEnrollment by 1
        self.g_num = 'G' + '0' * \
            (5 - len(str(Student.totalEnrollment))) + \
            str(Student.totalEnrollment)

    def __str__(self):  # string representation of the object
        status = "active" if self.enrolled == 'y' else "inactive"
        return f"{self.name.strip()}, {self.g_num}, {self.classLevel()}, {self.major}, active: {self.enrolled}, credits = {self.credits}, gpa = {self.gpa()}"

    def gpa(self):  # method to calculate gpa
        if self.credits == 0:
            return 0.0
        return self.qpoints / self.credits

    def addGrade(self, grade, credits):  # method to add grade
        grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        if grade.upper() not in grade_values or credits not in range(5):
            return False

        self.qpoints += grade_values[grade.upper()] * credits
        self.credits += credits
        return True

    def isActive(self):  # method to check if student is active
        return self.enrolled == 'y'

    def classLevel(self):  # method to check class level
        if self.credits >= 90:
            return 'Senior'
        elif self.credits >= 60:
            return 'Junior'
        elif self.credits >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def equals(self, other_student):  # method to check if two students are same
        return self.g_num == other_student.g_num and self.name == other_student.name


# A2 testscript global/executable code --------------------------------

# Global/executable code --------------------------------------
input('\nHit "Enter" to create several objects and print their summaries\n')

s1 = Student('Henry Miller', major='Hist',
             enrolled='y', credits=0, qpoints=0)
s2 = Student('Emma Maria Vicente', major='Math',
             enrolled='y', credits=90, qpoints=315)
s3 = Student('A. Einstein', major='Phys',
             enrolled='y', credits=0, qpoints=0)
s4 = Student('W. A. Mozart', major='Mus',
             enrolled='n', credits=29, qpoints=105)
s5 = Student('Emma Maria Vicente', major='CSci',
             enrolled='y', credits=60, qpoints=130)
s5.g_num = s2.g_num
s6 = Student('Vincent Van Gogh', major='Art',
             enrolled='y', credits=120, qpoints=315)
print('\nThe following Student objects were created: \n')
print('s1 = ', s1)
print('s2 = ', s2)
print('s3 = ', s3)
print('s4 = ', s4)
print('s5 = ', s5)
print('s6 = ', s6)
print('\nTotal number of students: ', Student.totalEnrollment)
input('\n\n\n Hit "Enter" to run several tests of the class methods -----------')
print('The gpa of ', s1.name, ' is ', s1.gpa(), '\n')
print('Class standing of ', s4.name, ' is ', s4.classLevel())
print('Class standing of ', s2.name, ' is ', s2.classLevel(), '\n')
if s1.equals(s2):
    print(s1.name, ' and ', s2.name, ' are the same student')
else:
    print(s1.name, ' and ', s2.name, ' are not the same student')
if s2.equals(s5):
    print(s2.name, ' and ', s5.name, ' are the same student')
else:
    print(s2.name, ' and ', s5.name, ' are not the same student\n')
if s1.isActive():
    print(s1.name, ' is currently active')
else:
    print(s1.name, ' is not currently active')
if s4.isActive():
    print(s4.name, ' is currently active')
else:
    print(s4.name, ' is not currently active\n')
print('Adding grade of "A" for ', s4.name, ', result: ', s4.addGrade('A', 3))
print('GPA of ', s4.name, ' is now ', s4.gpa())
print('Class standing of ', s4.name, ' is now ', s4.classLevel())
print('\nTrying to add bogus grade of "X" to ',
      s1.name, ' result: ', s1.addGrade('X', 3))
print('\nEnd of A2 Student class demo')
class Department:
    univ_students = 0
    avgGPA = 0.0

    def __init__(self, d_code, d_name, capacity, minGPA):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.studentRoster = []

    def __str__(self):
        return f"Department code = {self.d_code}, Department name = {self.d_name}, Capacity = {self.capacity}, Minimum GPA = {self.minGPA}"

    def addStudent(self, student):
        if student.gpa() < self.minGPA:
            return False, "GPA too low"
        if student.enrolled == 'n':
            return False, "Student not enrolled"
        if student in self.studentRoster:
            return False, "Duplicate student"
        if len(self.studentRoster) >= self.capacity:
            return False, "Department at capacity"
        
        self.studentRoster.append(student)
        Department.univ_students += 1
        Department.avgGPA = (Department.avgGPA * (Department.univ_students - 1) + student.gpa()) / Department.univ_students
        return True, "Student added successfully"

    def isQualified(self, student):
        if student.enrolled == 'n':
            return False, "Student not enrolled"
        return student.gpa() >= self.minGPA, "Student qualified" if student.gpa() >= self.minGPA else "GPA too low"

    def listRoster(self):
        for student in self.studentRoster:
            print(student)
