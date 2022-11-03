def get_square_root(n,p,e):                 #defining the function 
    n = float(n)                            #making them all floats
    p = float(p)
    e = float(e)
    if1 = (e*2)-2                           #doing the job so I dont have to in the if statement to make it more orginized
    if abs(if1) < p:                        # if statement with absolute value inside
        return e                            # returning only e if it is tru
    else:
        return get_square_root(n,p,(((e+n)/e)/2))     #doing the square root loop
