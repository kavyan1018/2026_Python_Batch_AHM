# class Student:
#     def display(self):
#         print("Constructor is called")
        
# # object 

# a = Student()     # default constructor is called

# a.display()   


class Student:
    def __init__(self):
        self.name = "John"
        self.age = 20
        
    def  display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        
s = Student()    # constructor is called
s.display()