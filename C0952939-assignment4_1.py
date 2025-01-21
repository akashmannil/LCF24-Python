#CSD-1233-01
#Assignment 4 Q1
#Akash Mannil
#October 12, 2024

#Defining program main entry point - main() function
def main():
    print("CSD-1233-01")
    print("Assignment 4 Q1")
    print("Akash Mannil")
    print("October 12, 2024\n")

    #user input for distance
    distance_in_kms = float(input("Enter the distance in kms: "))

    #calling distance calculator function and displaying the value
    convert_kms_to_miles(distance_in_kms);

#Function to convert kms to miles 
def convert_kms_to_miles(distance_in_kms):
    #local constant - conversion rate from kms to miles 
    KM_TO_MILE_CONVERSION_RATE = 0.6214

    #distance conversion and displaying data
    distance_in_miles = distance_in_kms * KM_TO_MILE_CONVERSION_RATE
    print("Converted distance is", distance_in_miles, "miles")

#Program entry point
main()

#End of Assignment 4 Q1