#Mark Hall
#9/7/21
#File Encryption and Decryption

#encrypt and decrypt the inverse of one another.
CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}


#constants for the menu choices.
ENCRYPT = 1
DECRYPT = 2
QUIT_CHOICE = 9

def main():
    choice = 0

    while choice != QUIT_CHOICE:
        #display the menu.
        display_menu()
        #get the user's choice.
        choice = int(input("Enter your choice "))

        #perform the selected action.
        if choice == ENCRYPT:
            encrypt()
        elif choice == DECRYPT:
            decrypt()
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")

#part 1
def encrypt():

    #obtain a string of the converted text.
    result = convert()

    #open output file and write to it.
    output_name = input("Enter the name of the output file: ")
    output_file = open(output_name, 'w')
    output_file.write(result)
    output_file.close()

#part 2
def decrypt():

    #I originally wrote this to just call the convert function,
    #followed by calling the encrypt function. It worked, but
    #it would print the input file line twice, so the input file
    #had to be entered twice. I settled with copying the code
    #from the encrypt function, but I understand that repeating
    #code is counterintuitive to the main function of functions
    #in the first place. 
    result = convert()
    output_name = input("Enter the name of the output file: ")
    output_file = open(output_name, 'w')
    output_file.write(result)
    output_file.close()
    
    #encrypt()
    

    
def convert():
    input_name = input("Enter the name of the input file: ")

    input_file = open(input_name, 'r')

    result = ''
    text = input_file.read()

    #If the character is a space, it is not converted;
    #otherwise convert.
    for ch in text:

        if ch.isspace():
            result = result + ch
        else:
            result = result + CODE[ch]

    return result

def display_menu():
    print('          ')
    print('     Encryption/Decryption Program Version 1.1')
    print('          ')
    print(' 1) Encrypt a file')
    print(' 2) Decrypt a file')
    print(' 9) Exit')
        

#call the main function.
main()
