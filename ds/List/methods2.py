fruits = ["apple", "banana", "orange", "grapes"]
print(fruits)


# clear method
# fruits.clear()
# print(fruits)

# index method
print(fruits.index("grapes")) 
# print(fruits.index("mango"))  not in the list -> error


# number methods  
numbers = [10, 20, 30, 40, 50]
print(numbers)


# count method 
# print(numbers.count(30))

# sort method
# numbers.sort()
# print(numbers)

# reverse method
# numbers.reverse()
# print(numbers)

# copy method
# a = numbers.copy()
# print("this is a copy of numbers:", a)

# extend method
# a = [1, 2]
# b = [3, 4]

# a.extend(b)
# print("A = ",a)
# print("B = ",b)


numbers = [10, 20, 30, 40, 50]
print("Original List :",numbers)


# Slicing -> range of elements from the list

"""
    list[start : end : step]
    
    start -> starting index of the slice
    end -> ending index of the slice
    step -> step size of the slice
"""

# print(numbers[1 : 4])
# print(numbers[:4]) # start index is 0 by default
# print(numbers[2:])  # end index is len(numbers) by default
# print(numbers[:])   # copy of the list
# print(numbers[::2])  # start, end, and step
# print(numbers[1::2])  # start, end, and step
# print(numbers[::-1])  # start, end, and step
print(numbers[-3:])