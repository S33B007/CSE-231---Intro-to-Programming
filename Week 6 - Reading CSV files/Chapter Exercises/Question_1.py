

# write a function called new_list_function that takes this initial_list 
# as input and returns another list with 3 copies of every value in the 
# initial_list. Finally, inside main(), print out all of the values in 
# the new list.


def new_list_function(input_str):
    new_list = input_str.split(' ')
    new_list = new_list * 3
    return new_list
  
# Write a program that keeps asking the user for new values to be added to a 
# list until the user enters 'exit' ('exit' should NOT be added to the list).
# These values entered by the user are added to a list we call 'initial_list'.

def main():
    initial_list = " "
    input_str = input('Enter value to be added to list: \n')
    while input_str != 'exit':
        input_str = input('Enter value to be added to list: \n')
        initial_list += input_str
        
    new_list = new_list_function(initial_list)
    for values in new_list:
       print(values)
main()
    
# # new_list_function definition goes here


# def main():
#   #loop to ask users for values goes here
#     input_str = input('Enter value to be added to list: \n')
#   new_list = new_list_function(initial_list)
#   #print values in new list
# main()
    
