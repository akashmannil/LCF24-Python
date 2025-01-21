#CSD-1233-01
#Assignment 5
#Akash Mannil
#November 5, 2025

#MENU based constants
ADD_BOOK_OPTION = 1
VIEW_BOOK_OPTION = 2
SEARCH_BOOK_OPTION = 3
EXIT_LIBRARY_OPTION = 4


#Defining program main entry point - main() function
def main():
    print("CSD-1233-01")
    print("Assignment 5")
    print("Akash Mannil")
    print("November 5, 2024\n")

    exit_flag = False #Flag for exiting program
    book_list = [] #Stores Library Books Data

    #Data entry Loop
    while exit_flag != True:
        userInput = get_user_input()
        
        #Menu options begins
        if userInput == ADD_BOOK_OPTION:
            book_list = add_book(book_list)
        elif userInput == VIEW_BOOK_OPTION:
            view_book(book_list)
        elif userInput == SEARCH_BOOK_OPTION:
            search_book(book_list)
        elif userInput == EXIT_LIBRARY_OPTION:
            print("Exiting Library Management program")
            exit_flag = True
        else:
            print("Please choose valid option") #Handling invalid input
        
        input("Press enter to continue") #Adding "enter to continue" action to provide smoother end user experience
    
    print("End of Assignment 5")

#Function to get user input
def get_user_input():
    #not using int(input()) so that exception wont be raised - resulting in abrupt program exit
    option = input("Manage Your Library:\n1.\tAdd Book\n2.\tView Books\n3.\tSearch Book\n4.\tExit\nChoose the option: ")
    if option.isdigit() == False:
        print("Invalid Option.")
        input("Press enter to retry")
        return get_user_input()
    return int(option)

#Function to add book into book_list variable
def add_book(book_list):
    #Get user inputs with proper validations done - returns original list, if invalid user inputs
    title = input("Enter book's title: ")
    #We check for numeric too, since volumes appear, and "1984" is a valid book title  by George Orwell
    if title.isalnum() == False:
        print("Please enter valid title. Data addition failed.")
        return book_list
    author = str(input("Enter book's author: "))
    if author.isalpha() == False:
        print("Please enter valid author. Data addition failed.")
        return book_list
    publication_year = input("Enter book's publication year: ")
    if publication_year.isdigit() == False:
        print("Please enter valid publication year. Data addition failed.")
        return book_list
    
    book_list.append([title, author, int(publication_year)])
    #successful data addition message
    print("Book", title, "authored by", author, "with publication year", publication_year, "added successfully")
    return book_list    
    
#Function to view all books
def view_book(book_list):
    #Empty Library condition
    if len(book_list) == 0: 
        print("Library is empty.")
        return
    #Loop in through book_list and display all data
    else:
        print("Books available in the Library:")
        for i in range(len(book_list)):
            print("Book", i+1)
            print("Name:", book_list[i][0])
            print("Author:", book_list[i][1])
            print("Publication Year:", book_list[i][2], "\n")

#Function to view all matching books based on user search term
def search_book(book_list):
    #Empty library condition - early exit
    if len(book_list) == 0:
        print("Library is empty.")
        return book_list
    
    book_title = input("Enter search book's title:")
    book_found_flag = False #Flag to trigger no data match output message

    #Looping in through book_list vartiable to match it with search input term book_title
    for i in range(len(book_list)):
        if book_list[i][0].upper() == book_title.upper():
            book_found_flag = True 
            print("Found a matching book, Book", i+1)
            print("Name:", book_list[i][0])
            print("Author:", book_list[i][1])
            print("Publication Year:", book_list[i][2], "\n")
    if book_found_flag == False:
        print("No matching book found")

#Program entry point
main()

#End of Assignment 5