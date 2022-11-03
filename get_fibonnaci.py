'''
Created on Nov 3, 2022

@author: DDrackett25
'''
def get_fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)



def main():
    
    n = int(input("enter a number:")) #the input
    
    print(get_fibonacci(n))           #calling the function
    



if __name__ == '__main__':
    main()