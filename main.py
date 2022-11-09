'''
Author - Noah Sokol
Last Edited:11/8/22
Discription - runs functions using recursion
'''

def get_factorial(n): # defining the function
    '''
author: Charlie
bugs: none
function: multiplys n by its factorials
'''
    if n<0: return False
    if n==0:            # making an if statement 
        return 1        # return 1 if true
    else:           
        return n * get_factorial(n-1)    # making factorial loop

def get_summation(n):
    '''
Created on Nov 2, 2022

@author: DDrackett25
'''
    if n<0: return False
    if n == 0:                        #saying that if the number inputed is equal to 0
        return 0                      # it is returning that it equals 0
    else:                             #if the input is anything else, it is returning the sum of the factorial 
        return n + get_summation(n-1)

def get_powers(a,n):                                     #defining the get powers function
    '''
author: Charlie
bugs: none
'''
    if n<0 or a<0: return False
    if n==0:                                            #if statement
        return 1                                         #returning 1 if equel to zero
    else:                                               #else statement
        return a * get_powers(a,n-1)                    # doing the power loop

def get_sum_of_numers_digits(n):  #defining the function
    '''
author: Charlie
bugs: none
'''
    if n < 0: return False
    if n<10:                        #if statement true if n is less than 10
        return n                    #returning the n if ture
    else:
        return get_sum_of_numers_digits(n/10) + n %10       #sum of numbers loop here (the % is the mod)

def get_compound_interest_balance(p,r,t):
    '''
    last updated: 11/2/22
    gets the compound interest balance using principal, rate, and time
        Arg:
            p - float - principal
            r - float - rate
            t - float - time in years - can't be under 0
        Returns:
            output - float - the compound interest balance
    '''
    if t < 0: return False
    if t == 0: return p
        
    else: return (1 + r) * get_compound_interest_balance(p,r,t-1)

def get_fibonacci(n):
    '''
    Created on Nov 3, 2022
author: Deja
'''
    if n<0: return False
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

def get_gcd(x,y):
    ''' 
    last updated 11/2/22
    Author: Noah Sokol
        Args:
        x - float - the larger of the two numbers
        y - float - the smaller of the two numbers
        Returns: the largest integer that divides both number1 and number2 without a remainder.
    '''
    x = abs(x)
    y = abs(y)
    if y <= x and x % y == 0:
        return y
    else: 
        return get_gcd(y,x % y)

def get_product_of_2_whole_numbers(a,b):      #defining function
    '''
author: Charlie
bugs: none
'''
    if a<0 or b<0: return False
    if b > 0:                   #if statement
        return a + get_product_of_2_whole_numbers(a,b-1)   # making a 2 whole numbers loop
    if b == 0:
        return 0            #if true return 0

def get_square_root(n,p,e):                 #defining the function 
    '''
author: Charlie
bugs: none
'''
    if n <0 or p<0 or e<0: return False
    if1 = (e*2)-2                           #doing the job so I dont have to in the if statement to make it more orginized
    if abs(if1) < p:                        # if statement with absolute value inside
        return e                            # returning only e if it is tru
    else:
        return get_square_root(n,p,(((e+n)/e)/2))     #doing the square root loop

def main():
    output = 'None'
    try:
        while True:
            function_to_run = input('fct for factorial, pwr for powers, sum for summation, fib for fibonacci, snd for sum of number digits, gcd for gcd, pro for product of 2 numbers, cib for compund balance interest, sqr for square root then - for the parameters ')
            if function_to_run.split('-')[0] == 'fct':
                output = get_factorial(int(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]))
            elif function_to_run.split('-')[0] == 'pwr':
                output = get_powers(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),float(function_to_run.split(',')[1]))
            elif function_to_run.split('-')[0] == 'sum':
                output = get_summation(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]))
            elif function_to_run.split('-')[0] == 'fib':
                output = get_fibonacci(int(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]))
            elif function_to_run.split('-')[0] == 'snd':
                output = get_sum_of_numers_digits(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]))
            elif function_to_run.split('-')[0] == 'gcd':
                output = get_gcd(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),float(function_to_run.split(',')[1]))
            elif function_to_run.split('-')[0] == "pro":
                output = get_product_of_2_whole_numbers(int(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),int(function_to_run.split(',')[1]))
            elif function_to_run.split('-')[0] == "cib":
                output = get_compound_interest_balance(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),float(function_to_run.split(',')[1]),float(function_to_run.split(',')[2]))
            elif function_to_run.split('-')[0] == "sqr":
                output = get_square_root(float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),float(function_to_run.split(',')[1]),float(function_to_run.split(',')[0][len(function_to_run.split('-')[0])+1:]),float(function_to_run.split(',')[2]))

            if output == False:  print('bad input please try again')

            else: break

        print(output)
    except IndexError: print('wrong number of paramaters entered')
    except ValueError: print('Please enter numbers')
    

while True:    
    main()
