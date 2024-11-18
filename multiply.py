#Mark Hall
#10/25/21
#Pg 616 #2


def main():
    #Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    #Display their product.
    print('Their product is', multiply(num1, num2))
    
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

#Call the main function.
main()

    
