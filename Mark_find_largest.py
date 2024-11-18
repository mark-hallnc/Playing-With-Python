#Mark Hall
#11/3/21
#Pg. 616 #4

def find_largest(number_list):
    #base case. if only one num in the list, it is
    #obviously the largest.
    if len(number_list) == 1:
        return number_list[0]
    #Test if the first number is greater than the second.
    #If it is, remove the second from the list.
    elif number_list[0] > number_list[1]:
        number_list.pop(1)
        #call the function.
        return find_largest(number_list)
    else:
        #If the first number is not greater than the second,
        #remove the first(smaller) number from the list.
        number_list.pop(0)
        #Call the function. 
        return find_largest(number_list)

