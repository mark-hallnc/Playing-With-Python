#Mark Hall
#10/5/21

#import random module for penny flip.
import random

#Define the penny class
class Penny:

    # The __init__ method initializes the
    # __sideup data attribute with 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
    def toss(self):

        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    def get_sideup(self):
        return self.__sideup

# main function
def main():

    # Create a Penny object.
    my_coin = Penny()

    # This will display 'Heads'.
    print('This side is up: ', my_coin.get_sideup())
    print('I am tossing the coin...')
    print('I am going to toss the coin twelve times:')

    #Loop to toss the penny 12 times
    count = 0
    for count in range(12):
        my_coin.toss()
        print(count + 1, my_coin.get_sideup())

#Call to main function to start program.
main()
