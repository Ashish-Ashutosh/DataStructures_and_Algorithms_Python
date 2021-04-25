def calculate_mode(*args):
    #stores the received arguments in a list
    storeInput = []
    #list to store elements
    storeElement = []
    #corresponding list to store their frequency
    storeFrequency = []

    #adding input elements to the list
    for item in args:
        storeInput.append(item)

    #calculating the frequency of each element in the list
    for selecting_item in storeInput:
        element = selecting_item
        counter = 0
        for counting_item in storeInput:
            if(element == counting_item):
                counter = counter + 1
        storeElement.append(element)
        storeFrequency.append(counter)

    #list to store the mode value of the input elements
    modeOfInputElements = []
    #logic to calculate the maximum frequency from the storeFrequency List
    maximum_frequency = 0
    for item in storeFrequency:
        if(item > maximum_frequency):
            maximum_frequency = item

    #logic to get the index of the highest frequency in storeFrequency and then adding the corresponding value from the
    #storeElement list to modeOfInputElements list
    counter = 0
    for item in storeFrequency:
        if (item == maximum_frequency):
            modeOfInputElements.append(storeElement[counter])
        counter = counter + 1

    #removing the duplicates from the modeOfInputElements using SET and adding it to another final list
    finalModeList = list(set(modeOfInputElements))
    print(finalModeList)


#calling the method to calculate mode
calculate_mode(0,1,0,1,1,1,1,20,20,20,20,20,0,0,0)

