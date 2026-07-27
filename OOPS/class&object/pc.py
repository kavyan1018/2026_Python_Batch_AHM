class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        
Stu1 = Student("Kavyan", 22)
Stu2 = Student("Yana", 20)
Stu3 = Student("Pratham", 20)
Stu4 = Student("Yagna", 19)

Stu1.display()
print("---------------------")
Stu2.display()
print("---------------------")
Stu3.display()
print("---------------------")
Stu4.display()
