for i in range(1, 4):     # outer loop   1, 2, 3    -> 3 iterations -> as a row 
    for x in range(1, 6):   # inner loop   1, 2, 3, 4, 5  -> 5 iterations -> as a column
        print(i * x, end = " ")
    
    print()
    
    
"""
        1 * 1 = 1
        1 * 2 = 2
        1 * 3 = 3
        1 * 4 = 4
        1 * 5 = 5
        
    2 
    
        2 * 1 = 2
        2 * 2 = 4
        2 * 3 = 6
        2 * 4 = 8
        2 * 5 = 10    

    3
        3 * 1 = 3
        3 * 2 = 6
        3 * 3 = 9
        3 * 4 = 12
        3 * 5 = 15
"""
