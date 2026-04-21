"""
    *
    **
    ***
    ****
    *****

i + 1
                        0 + 1 -> 1
    1            range(i + 1) -> 1     -> 1
    2            range(i + 1) -> 2     -> 2
    3            range(i + 1) -> 3     -> 3
    4            range(i + 1) -> 4     -> 4
    5            range(i + 1) -> 5     -> 5

    
"""



for i in range(5):   # 1, 2, 3, 4, 5    # outer loop -> 5 iterations -> as a row
    for j in range(i + 1):      # -> as a colums 
        print("*", end = "")
    print()