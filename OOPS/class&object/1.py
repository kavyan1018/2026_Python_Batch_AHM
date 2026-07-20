# # class 

# class Student:
#     def display(self):
#         print("Hello, I am a student")
        
        
# # object
# s1 = Student()


# # calling method
# s1.display()



class Student:
    
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)

# object
s = Student()

# Assigning values to object properties

s.name = "John"
s.age = 20

# calling method
s.display()