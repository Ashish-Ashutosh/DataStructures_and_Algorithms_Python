def reverseString(input):
    #first we do some validation to check if the input is a STRING
    if(input.isnumeric() or len(input) < 2 ):
        print("Invalid input type. Please enter a string")
    else:
        reverseString = []
        i=len(input)

        while(i>0):
            #storing the last element of input string into a LIST (Note that we reduce index by 1 because "string" count starts from index = 1
            reverseString.append(input[i-1])
            i=i-1

        #converting a LIST to String using 'join'
        print(''.join(reverseString))


def reverseString2(input):
    #pythons shortcut method to reverse a string
    outputString = input[::-1]
    print(outputString)



#method call to reverse a string
reverseString("ashish")
reverseString2("ashish")
