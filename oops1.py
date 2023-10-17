# Procedural programming

# from dataclasses import dataclass

# @dataclass
# class Student:
#     name:str
#     age:int
#     gender:str

# def print_student(student:Student):
#     print(student.name)
#     print(student.age)
#     print(student.gender)

# if __name__=='__main__':
#     print("Hello World")

#     s1 = Student("Vishal",10,"Male")

#     print_student(s1)

# Object Oriented Programming


class Student:
    name:str
    age:int
    gender:str


    def __init__(self,name:str,age:int,gender:str):

        self.name=name
        self.age=age
        self.gender=gender
    
    def print_student(self):
        print(self.name)
        print(self.age)
        print(self.gender)


if __name__=="__main__":
        print("Main")

        student1 = Student(name="Vishal", age=10, gender="Male")

        print(student1.name)
        print(student1.age)
        print(student1.gender)