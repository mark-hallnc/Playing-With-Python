#programming exercise 6

def main():
    #declare local variables
    number = 5
    number_list = [1,2,3,4,5,6,7,8,9,10]

    #display the list
    print('List of numbers:\n', number_list, sep='')

    #display numbers from list that are larger than number
    print('List of numbers that are larger than ', number, ':', sep='')

    #call display_larger_than_n_list function passing
    #number and number_list as arguments.
    display_larger_than_n_list(number, number_list)

def display_larger_than_n_list(n, n_list):
    #declare an empty list.
    larger_than_n_list = []

    #loop through the values in the list.
    for value in n_list:
        #determine if value is greater than n.
        if value > n:
            # if so, append the value to the list.
            larger_than_n_list.append(value)
    #display the list
    print(larger_than_n_list)
            

#call main function
main()
