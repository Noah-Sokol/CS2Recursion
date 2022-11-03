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
    if t == 0:
        return p
    else:
        return (1 + r) * get_compound_interest_balance(p,r,t-1)
