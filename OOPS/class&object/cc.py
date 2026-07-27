class Student:
    def __init__(self, other):
        self.name = other.name
        self.age = other.age
        
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        
# first object
    # __new__  -> creates object (allocates memory)   new = create

s1 = Student.__new__(Student)  # creating object without calling constructor
s1.name = "John"
s1.age = 20


# copying object
s2 = Student(s1)   # copy constructor is called
s2.display()