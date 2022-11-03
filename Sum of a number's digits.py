def get_sum_of_numers_digits(n):  #defining the function
'''
author: Charlie
bugs: none
'''
    n = float(n)                    #making the variable n into float
    if n<10:                        #if statement true if n is less than 10
        return n                    #returning the n if ture
    else:
        return get_sum_of_numers_digits(n/10) + n %10       #sum of numbers loop here (the % is the mod)
