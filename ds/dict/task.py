"""

Create a Python program that:

Take the following details from the user:
Roll Number
Name
Course
Marks
Store them in a Dictionary.
Display all student details.
Update the marks.
Add a new key called "City".
Search for a key entered by the user and display its value.
Delete the "Course" key.
Display:
Total number of keys
All keys
All values

"""



# take input from user

roll_no = input("Enter roll number: ")
name = input("Enter name: ")
course = input("Enter course: ")
marks = input("Enter marks: ")


# store the data in a dictionary

student = {
    "Roll Number" : roll_no,
    "Name" : name,
    "Course" : course,
    "Marks" : marks
}


# display the data
print("------Student Details-------")
for key in student:
    print(key, ":" , student[key])
    
    
# Update marks
new_marks = input("Enter new marks: ")
student["Marks"] = new_marks

# Add a new key-value called city
city = input("Enter city: ")
student["City"] = city



# serch for a key entered by the user and display its value
search_key = input("Enter key to search: ")

if search_key in student:
    print("Search Value = ", student[search_key])
else :
    print("Key not found in the dictionary.")
    
    

# delete the course key

del student["Course"]


# display total number of keys, all keys and all values
# total number of keys

print("Total number of keys: ", len(student))


# all keys
print("All keys: ", student.keys())

# all values
print("All values: ", student.values())