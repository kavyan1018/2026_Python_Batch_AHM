fruits = ["apple", "banana", "orange", "grape"]
'''
print(fruits[-1])   # why -> -1 is used to access the last element of the list. 


# append method 
fruits.append("Mango")
print(fruits)

# insert method
fruits.insert(1, "Kiwi")
print(fruits)

# remove method
fruits.remove("banana")
print(fruits)

# pop method -> remove the last element of the list and return it.
fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

#list length
print(len(fruits))

'''

for i in fruits:
    print(i)
    
    
if "apple" in fruits:
    print("Yes, apple is in the list")