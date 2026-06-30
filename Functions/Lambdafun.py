""" 
    Lambda function : small anonymous function
    
    fun normal
        def : 
            // code 
            
    lambda : one line function args : exp
    
    lambda argguments : expression 
    
    lambda : -> keyword to create a function
    args   : -> arguments to the function 
    expression : -> single expression to be evaluated and returned
        -> operation to perform (automatically returns)

"""

# def sum(a, b):
#     return a + b

# print(sum(10, 20))


# oprators 
# sum = lambda a, b : a + b
# print(sum(10, 20))

# if - else 

#  lambda arguments : expression if condition else expression
even = lambda num : "Even" if num % 2 == 0 else "Odd"   
# print(even(10))
print(even(7))