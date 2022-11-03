def get_product_of_2_whole_numbers(a,b):      #defining function
'''
author: Charlie
bugs: none
'''
    b = int(b)                      # making the everything an int
    a = int(a)
    if b > 0:                   #if statement
        return a + get_product_of_2_whole_numbers(a,b-1)   # making a 2 whole numbers loop
    if b == 0:
        return 0            #if true return 0
