def get_powers(a,n):                                     #defining the get powers function
'''
author: Charlie
bugs: none
'''
    n = int(n)                                           #making them ints
    a = int(a)                                           #making them ints
    if n==0:                                            #if statement
        return 1                                         #returning 1 if equel to zero
    else:                                               #else statement
        return a * get_powers(a,n-1)                    # doing the power loop
