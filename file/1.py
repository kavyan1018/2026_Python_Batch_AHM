# Write mode

# file = open("FileDemo1.txt", "w") 
# file.write("Hello World\n") 
# file.write("This is My First Session of File \n") 
# file.close()


# Read mode 

# file = open("FileDemo1.txt", "r")
# content = file.read()
# print(content)
# file.close()


# Append mode

# file = open("FileDemo1.txt", "a")
# file.write("I am 23 Years Old\n")
# file.write("I am from India\n")
# file.close()



#  w+ mode 
# file = open("FileDemo2.txt", "w+") 
# file.write("Hello World\n") 
# file.write("This is My First Session of File \n")

# file.seek(0) # -> Move the cursor to the beginning of the file

# read = file.read()
# print(read) 
# file.close()


# r+ mode

# file = open("FileDemo2.txt", "r+") 
# print(file.read())

# file.write("I am 23 Years Old\n")

# file.close()


# a+ mode

file = open("FileDemo2.txt", "a+")
file.write("I am from India\n")

file.seek(0) # -> Move the cursor to the beginning of the file
print(file.read())
file.close()