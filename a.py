#Definition for main program entry point
def main():

    userInput = int(input('Please enter a non negative integer'))

#Checking for Non negative integer input

    if (userInput>0):

        factorial(userInput)

    else:

        print('Enter valid positive number')

#Factorial function definition We check no negative integer is being passed to #the function beforehand

def factorial(n):

    factorialValue = 1 #We update the value on each iteration

    while(n >0):

        factorialValue = factorialValue * n

        n-=1 #each iteration reduces the number

    print('The factorial value of the provided number is:', factorialValue)

#Program start&nbsp;
main()