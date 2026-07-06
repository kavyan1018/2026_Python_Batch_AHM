# Built in function math

# import math    -> mathematical functions


# print(math.sqrt(25))
# print(math.factorial(5))    
# print(math.pow(2,5))    
# print(math.pi)    
# print(math.ceil(4.7))   Round up 
# print(math.ceil(4.02))    
# print(math.floor(4.02))    Round down
# print(math.floor(4.999))    


# import random  -> random number generation


# randint -> random integer 
# print(random.randint(start, end))
# print(random.randint(1, 10))
# print(random.random())
# print(random.choice(["Red", "Green", "Blue"]))
# print(random.choice([1, 2, 3, 4, 5]))
# print(random.randrange(1, 10, 3))  # start, end, step



# datetime module   -> Date and Time

# import datetime
# print(datetime.datetime.now())
# now  = datetime.datetime.now()
# print(now)
# print(now.date())
# print(now.time())



# os Module    -> Operating System

# import os
# print(os.getcwd())      # current working directory
# os.mkdir("Demo")
# os.mkdir("Demo3")
# print(os.listdir())    # list of files and directories in the current working directory
# os.rename("Demo2", "Demo1")    # rename directory
# print(os.remove("Demo1"))   # remove file
# print(os.rmdir("Demo"))  # remove directory



# sys module   -> System Infrormation


# import sys
# print(sys.version)    # -> version of python
# print(sys.platform)   # -> platform of the system
# print(sys.path)       # -> list of directories where python looks for modules
# print(sys.argv)         # -> list of command line arguments passed to the script
# print(sys.getsizeof(1))   # -> size of an object in bytes
# print(sys.exit())   # -> exit the program


# time module   -> Time related functions

# import time

# print("Start")
# time.sleep(5)  # -> sleep for 5 seconds
# print("End")
# time.time()  # -> current time in seconds since epoch
# print(time.ctime())  # -> current time in human readable format


# Statistics module   -> Statistical functions

# import statistics
# marks = [5, 20, 120, 40, 2, 2, 2]
# # print(statistics.mean(marks))   # -> mean of the list   -> Average of the list
# # print(statistics.median(marks))   # -> median of the list  -> middle value of the list  # -> 10, 20, 40, 50, 120
# print(statistics.mode(marks))   # -> mode of the list  -> most frequent value of the list
# # print(statistics.stdev(marks))   # -> standard deviation of the list  -> measure of how spread out the values are


# calendar module   -> Calendar related functions

# import calendar

# print(calendar.month(2026, 7))   # -> print the calendar of July 2026
# print(calendar.monthcalendar(2026, 7))   # -> print the calendar of July 2026 in list format
# print(calendar.isleap(2025))   # -> check if the year is a leap year or not
# print(calendar.leapdays(2020, 2022))   # -> count the number of leap years between 2020 and 2030
# print(calendar.calendar(2026))  # -> print the calendar of the year 2023