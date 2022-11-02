'''
author: Charlie
bugs: none
'''
def get_sum_of_numers_digits(n):

    n = float(n)
    if n<10:
        return n
    else:
        return get_sum_of_numers_digits(n/10) + n %10