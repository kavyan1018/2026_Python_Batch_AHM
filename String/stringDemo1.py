# A string is a sequence of characters.  

#  ""   '' -> immutable (cannot be changed)


# name = "John"
name = 'John'     # j -> 0      o  -> 1     h -> 2     n -> 3
print(name)

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

print(len(name))     # length of the string -> 4

# loop

# for i in range(len(name)):   # len -> length of the string
#     print(name[i])
    
    
# for each  ->  for each character in the string
for i in name:
    print(i)
    

x = "Hello"
m = x

print(m)