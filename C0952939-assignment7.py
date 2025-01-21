#CSD-1233-01
#Assignment 7
#Akash Mannil
#December 2, 2024

#Galilean Moon Data for program
G_MOON_MEAN_RADIUS = {
    'Io': 1821.6,
    'Europa': 1560.8,
    'Ganymede': 2634.1,
    'Callisto': 2410.3
}
G_MOON_SURFACE_GRAVITY = {
    'Io': 1.796,
    'Europa': 1.314,
    'Ganymede': 1.428,
    'Callisto': 1.235
}
G_MOON_ORBITAL_PERIOD = {
    'Io': 1.769,
    'Europa': 3.551,
    'Ganymede': 7.154,
    'Callisto': 16.689
}

#Defining program main entry point - main() function
def main():
    print("CSD-1233-01")
    print("Assignment 7")
    print("Akash Mannil")
    print("December 2, 2024\n")

    more_input_flag = True
    #User input based repeated search
    while more_input_flag == True:
        displayMoonData()
        more_input_flag = input("Do you want to search more? ")
        more_input_flag = True if (more_input_flag=="Y" or more_input_flag=="y") else False

#Function to get user input and display data based on defined values
def displayMoonData():
    input_moon_name = input("Please enter name of Galilean moon of Jupiter: ")
    input_moon_name = input_moon_name.lower().capitalize() #conversion based on defined format
    if input_moon_name in G_MOON_MEAN_RADIUS:
        print("Name:", input_moon_name)
        print("Mean Radius:", str(G_MOON_MEAN_RADIUS[input_moon_name]) + "kms")
        print("Surface Gravity:", str(G_MOON_SURFACE_GRAVITY[input_moon_name]) + "m/s")
        print("Orbital Period:", str(G_MOON_ORBITAL_PERIOD[input_moon_name]) +"days")
    else:
        print("Invalid moon name. No results for the provided input.")
    

#Program entry point
main()

#End of Assignment 7