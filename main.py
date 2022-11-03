'''
Author - Noah Sokol
Last Edited:11/2/22
'''
def get_powers(a,n):
    '''
    author: Charlie Jenkins
    bugs: none
    '''
    n = float(n)
    a = float(a)
    if n==0:
        return 1
    else:
        return a * get_powers(a,n-1)

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
    if t == 0: return p
        
    else: return (1 + r) * get_compound_interest_balance(p,r,t-1)
        

def get_gcd(x,y):
    ''' 
    last updated 11/2/22
    Author: Noah Sokol
        Args:
          x - float - the larger of the two numbers
          y - float - the smaller of the two numbers
        Returns: the largest integer that divides both number1 and number2 without a remainder.
    '''
    if y <= x and x % y == 0:
        return y
    else: 
        return get_gcd(y,x % y)


def main():
    
    function_to_run = input('which function would you like to run ')
    if function_to_run.split('-')[0] == 'pwr':
        output = get_powers(float(function_to_run.split(',')[0][4:]),float(function_to_run.split(',')[1]))
    elif function_to_run.split('-')[0] == 'gcd':
        output = get_gcd(float(function_to_run.split(',')[0][4:]),float(function_to_run.split(',')[1]))
    elif function_to_run.split('-')[0] == "cib":
        output = get_compound_interest_balance(float(function_to_run.split(',')[0][4:]),float(function_to_run.split(',')[1]),float(function_to_run.split(',')[2]))
        '''
        could use something like variables = function_to_run.split('')[2:]
        '''
    print(output)
    
main()
