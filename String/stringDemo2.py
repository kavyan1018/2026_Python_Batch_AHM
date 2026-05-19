"""
string  : immutable  sequence  of  characters   ==> no changes   in string  . 
"""

"""s= "my name is ram."
print(s)
print(type(s))
"""

# built in  function   : len min max  sorted sum  reverse 

"""
s="my name is zana."
print(len(s))   # length   ===> 1 
print(min(s))   # minimum   ===> ascci value  : 
print(max(s))   # maximum 
print(sorted(s))  # sorted
"""

# slicing  in string  : 

"""
s="my name is yana."
#  0123456
# index : 0   =====> 
# pos  index : left to right 
# neg  index : right to left
print(s[0])
print(s[2])
print(s[3:5])  # start  end step   ===> starting index 3  ending  index : 5 
print(s[2 :11])
print(s[1 : 9  :2])  # start : 1 index ending  : 9  step  :2
print(s[3 : 12  :3])  # start : 3 index ending  : 12  step  :3

print(s[-1]) 
print(s[-3])
print(s[2 : -2])
print(s[ : -2])
print(s[ : ])
print(s[-2 : -9 : -1])
print(s[ : : -1])
"""

# task :1 
"""
input : "dishant dipakkumar shah"
output : d.d.shah  
"""
# s="dishant dipakkumar shah"
# result = s[0] +"." +s[8] +"."+s[19 :] 
# print(result)

# methods  : 

s="my name is yana."

print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.casefold())

print(s.count("a"))
print(s.count("a",5,20))  # word count  , start index , end index
print(s.count("na"))