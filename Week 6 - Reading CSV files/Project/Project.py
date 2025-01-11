###########################################################
# Computer Project #5
# variables with string
# function to open file
#     prompts the user to input a file name to open and keeps prompting until a valid name is entered.
# function to read file
#     This function reads the comma-separated value (csv) file using file pointer fp. The file
#     has one header line. Create a list of tuples.
# function to get characters by criterion
#     Given a list of character tuples, retrieve the characters that match a certain criteria.
#     condtion to check if there is a problem with a value or criteria parameter, don’t add the character to the
#         return list
# function to get characters by criteria
#     his function takes as parameter the list of tuples returned by the read_file function
#     (master_list), an element, a weapon, and a rarity and returns a list of tuples filtered using
#     those 3 criterias
# function to get region
#     Given the master list of character tuples, retrieve all available regions into a list.
# function to sort characters
#     Given a list of character tuples, create a new list where character tuples have been sorted.
#     list is sorted alphabeticaly first then decreasing rarity
# function to display characters
#     Given a list of character tuples, display the characters along with their information, using
#     the formats (HEADER and ROWS) provided as constants
#     condition to check if a region has
#         the value None, display 'N/A'.
# function to get option
#     Display a menu of options and prompt for input (MENU in the starter code).
#     condition to check if the user enters a valid option (the input is an integer between 1 and 4),
#         return the integer
#     otherwise 
#         print an error message (INVALID_INPUT in the starter
#         code).
# function for the main
#     open file
#     read file
#     call get option function
#     condition to continue looping while option is not 4
#         condition if option returns 1
#             print following str
#             call get option again
#         condition if option returns 2
#             while loop if true:
#                 prompt and convert input to int
#                 if condition is not met:
#                     print str
#                     prompt and convert input to int
#                 else 
#                     prompt for value
#                     if condition is met:
#                         try
#                             convert value to int
#                             set variable = call get criterion with parameters being criteria and value
#                             variable = call sort characters and use prior variable as parameter
#                             call display characters and use prior variable
#                             call for get option
#                             break
#                         except invalid input:
#                         print str
#                     else
#                         convert value to int
#                             set variable = call get criterion with parameters being criteria and value
#                             variable = call sort characters and use prior variable as parameter
#                             call display characters and use prior variable
#                             call for get option
#         condition if option returns 3
#             call for input of variables
#             try:
#                 convert input to int
#             except valueerror:
#                 print str
#                 rairity is now an int when input is given
#             set variable = call get criteria with parameters being criteria and value
#             variable = call sort characters and use prior variable as parameter
#             call display characters and use prior variable
#             call for get option
#         condition if is 4
#             break out of program          
# function for main
# call main
###########################################################


import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    ''' prompts the user to input a file name to open and keeps prompting until a valid name is entered.'''
    prompt = input("Enter file name: ")
    while True:
        try:
# fp points to data ... and reads over data
            fp = open(prompt, "r")
            return fp
        except FileNotFoundError:
            print("\nError opening file. Please try again.")
            prompt = input("Enter file name: ") 
    return fp
    

def read_file(fp):
    '''This function reads the comma-separated value (csv) file using file pointer fp. The file
        has one header line. Create a list of tuples.'''
    list1 = []
    fp.readline() # iterate over the line
    for line in fp:
        # give each variable a new index to match the order in the touple
        line = line.strip().split(",")
        name = line[0]
        element = line[2]
        weapon = line[3]
        rarity = int(line[1])
        region = line[4]
        if region == "":
            region = None
        list_tuple = (name, element, weapon, rarity, region)
        list1.append(list_tuple)
    return list1
        


def get_characters_by_criterion (list_tuple, criteria, value):
    '''Given a list of character tuples, retrieve the characters that match a certain criteria.'''
    list2 = []
    # we want to go through each tuple if character mathes criteria add to list
    for tuples in list_tuple:
        if criteria == RARITY:
            if tuples[criteria] and type(value) == int and tuples[criteria] == value:
                list2.append(tuples)
        else:
            if tuples[criteria] and type(value) == str and tuples[criteria].lower() == value.lower():
                list2.append(tuples)
    return list2

        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''This function takes as parameter the list of tuples returned by the read_file function
        (master_list), an element, a weapon, and a rarity and returns a list of tuples filtered using
        those 3 criterias'''
    # here we are filtering each list with the criteria to math with the parameters
    result_list = get_characters_by_criterion(master_list, ELEMENT, element)
    result_list = get_characters_by_criterion(result_list, WEAPON, weapon)
    result_list = get_characters_by_criterion(result_list, RARITY, rarity)
    return result_list



def get_region_list  (master_list):
    '''Given the master list of character tuples, retrieve all available regions into a list.'''
    region_list = []
    # go through each line and check conditions for adding to the list
    for line in master_list:
        if line[4] == None or line[4] in region_list:
            continue
        else:
            region_list.append(line[4])
    region_list.sort()
    return region_list
        
        
        
def sort_characters (list_of_tuples):
    '''Given a list of character tuples, create a new list where character tuples have been sorted.'''
    sorted_list = sorted(list_of_tuples)
    new_list = sorted(sorted_list, key=itemgetter(3), reverse = True)
    return new_list
    

def display_characters (list_of_tuples):
    '''Given a list of character tuples, display the characters along with their information, using
        the formats (HEADER and ROWS) provided as constants in prog06.py.  '''
    if list_of_tuples == []:
        print('\nNothing to print.')
    else:
        print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format("Character","Element", "Weapon", "Rarity", "Region"))
        for tuples in list_of_tuples:
            if tuples[4] == None:
                # since we can't modify a tuple we are putting a string in that index to replace the value in the list
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(tuples[0],tuples[1],tuples[2],tuples[3],"N/A"))
            else:
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(tuples[0],tuples[1],tuples[2],tuples[3],tuples[4]))


def get_option():
    '''Display a menu of options and prompt for input (MENU in the starter code).'''
    option = int(input(MENU))
    if 1 <= option <= 4:
        return option
    else:
        print(INVALID_INPUT)
        option = input(MENU)

  
def main():
    files = open_file()
    op = read_file(files)
    option = get_option()
    while option != 4:
        if option == 1:
            print("\nRegions:")
            print(", ".join(get_region_list(op)))
            option = get_option()
        if option == 2:
            while True:
                # I am converting it to int so I can check the condition and compare it with ints and works with 
                #   the functions we later call
                criteria_inp = int(input(CRITERIA_INPUT))
                if not(0 <= int(criteria_inp) <= 4):
                    print(INVALID_INPUT)
                    criteria_inp = int(input(CRITERIA_INPUT))
                else:
                    value_inp = input(VALUE_INPUT)
                    if criteria_inp == RARITY:
                        try:
                            value = int(value_inp)
                            # by assigning each function to a variable we dont have to put parameter in a function in a parameter in a function 
                            criterion = get_characters_by_criterion(op, criteria_inp, value)
                            sort = sort_characters(criterion)
                            display_characters(sort)
                            option = get_option()
                            break
                        except ValueError:
                            print(INVALID_INPUT)
                            criteria_inp = input(CRITERIA_INPUT)
                    else:
                        value = value_inp
                        criterion = get_characters_by_criterion(op, criteria_inp, value)
                        sort = sort_characters(criterion)
                        display_characters(sort)
                        option = get_option()
                        break            
        if option == 3:
            element = input(ELEMENT_INPUT)
            weapon = input(WEAPON_INPUT)
            rarity = input(RARITY_INPUT)
            try:
                rarity = int(rarity)
            except ValueError:
                print(INVALID_INPUT)
                rarity = int(input(RARITY_INPUT))
            characters = get_characters_by_criteria(op, element, weapon, rarity)
            characters = sort_characters(characters)
            display_characters(characters)
            option = get_option() 
        if option == 4:
            break
       
    





# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
