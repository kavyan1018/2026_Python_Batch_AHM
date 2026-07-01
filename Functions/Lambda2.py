# map() -> given function to every element of iterable and returns a map object
# list, tuple, set, dict   -> returns a new iterable of the same type

# num = [1, 2, 3, 4, 5]
# squares = list(map(lambda x : x ** 2, num))
# print(squares)

# convert the string to uppercase

# name = ["john", "jane", "doe"]
# res = map(str.upper, name)
# print(list(res))


# multiple iterables

# a = [1, 2, 4]
# b = [10, 20, 30]
# res = map(lambda x, y: x + y, a, b)
# print(list(res))



# --------------------------------------------------------
#The filter() function is used to select elements from an iterable based on a condition.

# filter(function, iterable) 
# num = [10, 15, 20, 25, 30]  

# res = filter(lambda x : x <= 20, num)
# print(list(res))


names = ["Amit", "Ankit", "Ravi", "Ramesh", "Suresh", "Amitabh"]

res = filter(lambda names: names.startswith("A"), names)
print(list(res))