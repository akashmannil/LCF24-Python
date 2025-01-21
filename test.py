#Function definition for the required problem
def get_passes(name_to_grade, min_pass):
    #Initialisation of the results
    pass_list = dict()
    
   #Looping through to find passed students
    for key in name_to_grade:
        if name_to_grade[key]>=min_pass:
            pass_list[key]=name_to_grade[key]
    
    return pass_list

#Not definining and calling any other functions as question only mentions function def.

d = {'Jane Goodall': 82, 'Anya Tafliovich': 46, 'Marie Curie': 97}

print(get_passes(d, 46))
print(get_passes(d, 85))