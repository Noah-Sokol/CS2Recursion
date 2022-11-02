'''
author: Charlie
bugs: none
function: multiplys n by its factorials
'''
def get_factorial(n):

    n = float(n)
    if n==0:
        return 1
    else:
        return n * get_factorial(n-1)