#CSD-1233-01
#Assignment 3
#Akash Mannil
#September 21, 2024

print("CSD-1233-01");
print("Assignment 3");
print("Akash Mannil");
print("September 21, 2024\n");

#Program 1
print("Program 1")
area_in_square_meter = int(input("Enter the total Square meters in a tract of land: "))
area_in_hectares = area_in_square_meter / 10000
print("Area of entered tract of land in Hectares: ", area_in_hectares, "Hectares")

#Program 2
print("\nProgram 2")
foodCharge = float(input("Enter the charge of food: "))
tipAmount = 0.18 * foodCharge
hstAmount = 0.13 * foodCharge
totalFoodCharges = foodCharge + tipAmount + hstAmount
print("Tip amount: ", tipAmount)
print("HST Charges: ", hstAmount)
print("Total amount: ", totalFoodCharges)


#Program 3
print("\nProgram 3")
principal_amount = float(input("Enter the amount of principal originally deposited into the account: "))
annual_interest_rate = float(input("Enter the annual interest rate paid by the account(in percentage): "))
number_of_times_interest_compounded = int(input("Enter the number of times per year the interest is compounded(if monthly enter 12, if quarterly enter 4): "))
number_of_years_account_left = float(input("Enter the no.of years the account will be left to earn interest: "))

#Changing interest rate to percentage value and calculating final amount
annual_interest_rate = annual_interest_rate/100 
finalAmount = principal_amount * \
    (1 + (annual_interest_rate/number_of_times_interest_compounded))**(number_of_times_interest_compounded * number_of_years_account_left)

print("Final Amount in account will be", finalAmount)

#End of Assignment 3