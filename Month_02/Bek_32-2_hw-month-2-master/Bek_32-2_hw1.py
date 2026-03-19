class Person:
    def __init__(self, fullname, age, is_married):
        self.FullName = fullname
        self.Age = age
        self.IsMarried = is_married

    def introduce_myself(self):
        print(f'Name: {self.FullName}, Age: {self.Age}, Is married: {self.IsMarried}')

AkmatbekovBek = Person('Akmatbekov Bek', 15, 'No')
AkmatbekovBek.introduce_myself()


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def mid(self):
        print(self.marks.values(), sum(self.marks.values()) / len(self.marks.values()))

class Teacher(Person):

    Salary = 10000

    def __init__(self, fullname, age, is_married, experience=0):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def SalaryTeacher(self):
        if self.experience > 3:
            return self.Salary + (self.Salary / 100 * 5) * (self.experience - 3)


Egor_Gromov = Teacher('Egor Gromov', 36, 'Yes', 10)
Egor_Gromov.introduce_myself()
print(f'Expirience: {Egor_Gromov.experience}, Salary: {Egor_Gromov.SalaryTeacher()}')



def CreateStudent():
    student1 = Student('Ivan Ivanov', 16, 'No', {
        'Geometry': 4,
        'History': 5,
        "Physics": 4,
        "Biology": 2
    })
    student2 = Student('Artem Petrov', 17, 'No',{
        'Geometry': 3,
        'History': 4,
        "Physics": 4,
        "Biology": 5
    })
    student3 = Student('Roman Stepanov', 15, 'No',{
        'Geometry': 5,
        'History': 3,
        "Physics": 2,
        "Biology": 4
        })
    StudentList = [student1, student2, student3]
    return StudentList

inf = CreateStudent()
for i in inf:
    i.introduce_myself(), i.mid()











































