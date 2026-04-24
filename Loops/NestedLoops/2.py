# for i in range(1, 5):
#     for a in range(1, 5):
#         print(i, end = " ")
#     print()
    
    
for i in range(1, 5):       # 1 to 4 -> 4 iterations -> as a row
    for a in range(i):    # 0 to i - 1 -> as a column
        print( "*", end = " ")
    print()