#!/usr/bin/python
# python类学习

# 父类
class SchoolMember:
    '''class Represent any school member......'''
    def __init__(self, name, age): # 构造
        self.name = name
        self.age = age
        print("Initializing a school member.")
    def __del__(self): # 析构
        print ("dec a school member.")
    def tell(self):
        '''Tell my details'''
        print("Name: %s, Age: %s, " % (self.name, self.age))

# 继承
class Teacher(SchoolMember):
    '''class Teacher Represent a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initializing a teacher")
    def __del__(self):
        print ("dec a teacher")
    def tell(self):
        SchoolMember.tell(self)
        print("Salary: %d" % self.salary)

class Student(SchoolMember):
    '''class Student Represent a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ("Initializing a student")
    def __del__(self):
        print ("dec a student")
    def tell(self):
        SchoolMember.tell(self)
        print( "Marks: %d" % self.marks)

# 打印类注释？声明？
print(dir(SchoolMember)) # 打印这个类的内置属性
print(SchoolMember.__doc__)
print(Teacher.__doc__)
print(Student.__doc__)

t = Teacher("Late Lee", 30, 9000)
s = Student("Peter", 25, 90)

members = [t, s]

for m in members:
    m.tell()

