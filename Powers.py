'''
author: Charlie
bugs: none
'''
def get_powers(a,n):

    n = int(n)
    a = int(a)
    if n==0:
        return 1
    else:
        return a * get_powers(a,n-1)