# def find_max(num):
#     return max(num)


# lst = [10, 20, 30, 40, 50]
# print(find_max(lst))


# create f --> which will accept args and returen all key as list and print it

def get_keys(**kwargs):
    return list(kwargs.keys())

# fun call
keys = get_keys(name="John", age=25, city="New York", salary=50000)
print("Keys:", keys)