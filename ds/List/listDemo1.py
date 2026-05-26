# fruits = ["apple", "banana", "orange", "grape"]

# print(fruits)  
# print(fruits[0])  # apple


# # mixed data types

# mixed = [10, "This is my First List", 3.14, True]
# print(mixed)


# # mutable  ->  we can change the value of the list

# fruits[2] = "Mango"
# print(fruits)


# split -> It is a method that is used to split a string into a list of substrings based on a specified delimiter. By default, 

# fruits = input("Enter the fruits :").split()
# print(fruits)


fruits = input("Enter the fruits :").split()
print("Original List :",fruits)

# taking input from the user 
index = int(input("Enter the index of the fruit you want to change :"))

# value input 
value = input("Enter the new fruit Name :")

# value change 
fruits[index] = value

print("Updated List :",fruits)