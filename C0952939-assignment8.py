#CSD-1233-01
#Assignment 8
#Akash Mannil
#December 7, 2024

#Import random function to select random key to pop
import random

#Define main function
def main():
    print("CSD-1233-01")
    print("Assignment 8")
    print("Akash Mannil")
    print("December 7, 2024\n")


    print("Dictionary Key/Values:")
    count = 0
    while count < 1:
        try: #catching non integer input from user
            count = int(input("How many key value pairs are in the Dictionary: "))
        except ValueError:
            print("Please enter a valid input")

    #Declaring the input dictionary variable
    inputDictionary = {}

    #Entering data
    for i in range(count):
        print("Element", i+1, "data:")
        key = input("Enter the Key: ")
        value = input("Enter the Value: ")
        inputDictionary[key] = value
    
    #Display the input dictionary
    print("Input dictionary: ", inputDictionary)

    userChoice = 'y'
    while (userChoice == 'y' or userChoice == 'Y'):
        #call dict_pop_item() function to pop random element
        outputList = dict_pop_item(inputDictionary)

        if outputList[1] == None:
            print("No more elements to delete. Exiting program")
            break #can be made userChoice = "N" to exit as well
        else:
            #Display the updated dictionary after popping
            print("New Dictionary: ", outputList[0])
            #Display the popped key value pair
            print("Key value pair removed: ", outputList[1])
            userChoice = input("Do you want to delete more? (Y/N) ")

#Declare dict_pop_item function
def dict_pop_item(inputDictionary):
    # Empty Dictionary scenario
    if not inputDictionary:
        return [inputDictionary, None]

    #Use random function to generate random key and pop the key value pair
    popKey = random.choice(list(inputDictionary.keys()))
    popValue = inputDictionary.pop(popKey)

    popItem = (popKey, popValue) #tuple with removed data

    #Return the list with [new dictionary,poppeed item] format
    return [inputDictionary, popItem]

#Program entry point
main()

#End of Assignment 8