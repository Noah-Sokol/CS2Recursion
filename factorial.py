def get_factorial(n): # defining the function
'''
author: Charlie
bugs: none
function: multiplys n by its factorials
'''
    n = float(n)        # making n a float
    if n==0:            # making an if statement 
        return 1        # return 1 if true
    else:           
        return n * get_factorial(n-1)    # making factorial loop
