#CSD-1233-01
#Assignment 4 Q2
#Akash Mannil
#October 12, 2024

#Defining program main entry point - main() function
def main():
    print("CSD-1233-01")
    print("Assignment 4 Q2")
    print("Akash Mannil")
    print("October 12, 2024\n")

    #Calling function which accepts user input and displays income
    calculate_income_based_on_tickets()

#Function accepts user input and displays income based on ticket types and number
def calculate_income_based_on_tickets():
    #function constants - ticket price based on class
    CLASS_A_TICKETS_PRICE = 20
    CLASS_B_TICKETS_PRICE = 15
    CLASS_C_TICKETS_PRICE = 10

    #getting user inputs
    class_A_tickets_sold = int(input("Enter the no.of Class A tickets sold: "))
    class_B_tickets_sold = int(input("Enter the no.of Class B tickets sold: "))
    class_C_tickets_sold = int(input("Enter the no.of Class C tickets sold: "))

    #calculating income generated and displaying income
    income_generated = CLASS_A_TICKETS_PRICE * class_A_tickets_sold
    income_generated += CLASS_B_TICKETS_PRICE * class_B_tickets_sold
    income_generated += CLASS_C_TICKETS_PRICE * class_C_tickets_sold
    print("Income generated from ticket sales: $" + str(income_generated))

#Program entry point
main()

#End of Assignment 4 Q2