# [] , ()

# data = {10, 20, 30, 40}
# print(data)

# data = {10, 20, 30, 40, 20}
# print(data)

# data = {10, 20, 30, 40, 20}
# data.add(50)

# print(data)


# data = {10, 20, 30, 40, 20}
# data[3] = 100
# print(data)


data = {10, 20, 30, 40}

old = int(input("Enter the old value: "))
new = int(input("Enter the new value: "))

if old in data:
    data.remove(old)
    data.add(new)
    
    print("Updated set:", data)
else :
    print("Value not found in the set.")