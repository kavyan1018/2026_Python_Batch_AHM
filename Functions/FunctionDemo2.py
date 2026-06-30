# *args -> accept any number of positional arguments. These arguments are stored in a tuple.


# def numebrs(*data):
#     print(data)
    
# numebrs(1, 2, 3, 4, 5)

#loop 
# def num(*args):
#     for i in args:
#         print(i)
        
# num(1, 2, 3, 4, 5)


# kwargs -> accept any number of keyword arguments. these arguments are stored in a dictionary.
"""

    *  -> tells python to collect all positional arguments into a tuple  
    ** -> tells python to collect all keyword arguments into a dictionary
    
    args -> is just a variable name, you can use any name you want.
"""


# def stu(**data):
#     print(data) 
    
# stu(name="John", age=25, city="New York")


    # marge 
    
def emp(id, *args, **kwargs):
    print("ID :", id)
    
    print("\nSkills :")
    for skill in args:
        print(skill)
    
    print("\nDetails :")
    for key, value in kwargs.items():
        print(key, ":", value)


emp(
    101,
    "Python",
    "JavaScript",
    "Java",   
    name = "John",
    age = 25,
    city = "New York",
    salary = 50000
)