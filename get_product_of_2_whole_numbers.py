def get_product_of_2_whole_numbers(a,b):
    b = int(b)
    a = int(a)
    if b > 0:
        return a + get_product_of_2_whole_numbers(a,b-1)
    if b == 0:
        return 0

def main():

    b = input("b = ")
    a = input("a = ")
    end = get_product_of_2_whole_numbers(a,b)
    print (end) 

main()