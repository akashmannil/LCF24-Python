#CSD-1233-01
#Assignment 6
#Akash Mannil
#November 17, 2024

#Constants for program
PROGRAM_1 = 1
PROGRAM_2 = 2

#Defining program main entry point - main() function
def main():
    print("CSD-1233-01")
    print("Assignment 6")
    print("Akash Mannil")
    print("November 17, 2024\n")

    exit_program_flag = False
    while (exit_program_flag == False):
        print("Please enter Program # to run:")
        user_choice = int(input("(1)Sequential Total (2)Sequential Split :"))
        if user_choice == PROGRAM_1:
            print("SEQUENTIAL TOTAL RESULT: ", seq_total())
        elif user_choice == PROGRAM_2:
            print("SEQUENTIAL SPLIT RESULT:", seq_split())
        else:
            print("Enter valid input")
            continue
        exit_program_flag_input = input("Do you want to rerun the program? (Y/y for Yes)")
        if exit_program_flag_input == "Y" or exit_program_flag_input == "y":
            exit_program_flag = False
        else:
            exit_program_flag = True
     
#Function definition for Program 1
def seq_total():
    user_input = getInput()
    seq_total_result = ""
    for i in user_input:
        try: #conversion identifies float/str value
            temp_value = float(i)
            if seq_total_result == "":
                seq_total_result = 0
            seq_total_result += temp_value
        except ValueError:
            seq_total_result += i
    try:
        if seq_total_result == int(seq_total_result):
            return int(seq_total_result)
    except ValueError:
        return seq_total_result

#Function for getting list or tuple
def getInput():
    user_input = []
    user_input_add_more = "Y"
    user_input_data_type = None
    current_input_data_type = None

    tupleFlag = input("Enter 0 if you want to enter tuple value, otherwise list: ")
    while (user_input_add_more == "Y" or user_input_add_more == "y"):
        input_value = input("Enter tuple/list element: ")
        try: #data integrity maintained after entering the input
            float(input_value)
            if user_input_data_type == None: #1st data entered stored as main data type
                user_input_data_type = float if input_value != int(input_value) else int
            current_input_data_type = float if input_value != int(input_value) else int
        except ValueError:
            if user_input_data_type == None: #1st data entered stored as main data type
                user_input_data_type = str
            current_input_data_type = str

        #If data integrity threatened, new data input requested from user    
        if len(user_input)>0 and user_input_data_type != current_input_data_type:
            print("Please enter same data type as previous element")
            continue
        user_input.append(input_value)
        print("Temporary Tuple/List now:", tuple(user_input) if tupleFlag=="0" else user_input)
        user_input_add_more = input("Do you want to add more values? (Y/y for Yes)")
        if len(user_input) < 2 and user_input_add_more !="Y" and user_input_add_more !="y":
            print("Please enter atleast 2 elements")
            user_input_add_more = "Y"

    if tupleFlag == "0": #to display data as list/tuple
        user_input = tuple(user_input)
    return user_input
    
#Function definition for Program 2
def seq_split():
    user_input = getInput()
    user_input_length = len(user_input)
    if user_input_length % 2 == 0:
        list_1_index = int(user_input_length/2)
        final_list = [user_input[0:list_1_index],user_input[list_1_index:]]
    else:
        list_1_index = int(user_input_length/2+1)
        final_list = [user_input[0:list_1_index],user_input[list_1_index:]]
    return final_list

#Program entry point
main()

#End of Assignment 6