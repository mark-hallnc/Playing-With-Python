#Mark Hall
#9/7/21
#Unique Words


def main():

    #get the name of the file to open.
    input_name = input("Enter the name of the input file ")

    #open the input file and read the text.
    input_file = open(input_name, 'r')
    text = input_file.read()
    words = text.split()

    #create a set of unique words.
    unique_words = set(words)

    #print the results.
    print("These are the unique words in the text: ")
    for word in unique_words:
        print(word)

    #close the file.
        input_file.close()
    

#call the main function.
main()    
