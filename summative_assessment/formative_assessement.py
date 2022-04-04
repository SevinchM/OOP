from datetime import datetime, date

class Person:
    def __init__(self, name, dob) -> None:
        self.name = name
        self.dob = dob

    def __repr__(self) -> str:
        return f"Name: {self.name}, DOB: {self.dob}, Age: {self.age()}"


    #method to claculate the person's age
    def age(self) -> int:
        #calcualte the age
        #get date
        today = date.today()
        #convert DOB from str to datetime obj
        birthdate = datetime.strptime(self.dob, '%Y/%m/%d')
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        year_difference = today.year-birthdate.year
        age = year_difference - one_or_zero
        return age



class Student(Person):
    #class attributes 
    school = "ASU"

    def __init__(self, name, dob, grade, subjects) -> None:
        #access parent's properties
        super().__init__(name, dob)
        self.grade = grade
        self.subjects = subjects

    def __repr__(self) -> str:
        return super().__repr__() + f", Grade: {self.grade}, Subjects: {self.subjects}"

#list of students

students = []


print("Welcome to ASU digital student services!")
print("Please enter your new-student information.")

while True:
    name = input("Please enter your name: ")
    dob = input("Enter your data of birth (yyyy/mm/dd): ")
    grade = input("Enter your grade level: ")
    subjects = input("Subjects: ")
    
    students.append(Student(name, dob, grade, subjects))

    answer = ''
    while answer not in ('yes', 'no'):
        answer = input("Would you like to add another student? (yes/no)")

    if answer =='no':
        for student in students:
            print(student)
            print("...................................................")

    break
    
    


