# Write a function called 'return_list' that takes a string as a parameter and 
# returns a list of words in the string. "Words" are entities that are 
# separated by either commas (',') or spaces (' '). 

# In case the string contains neither commas nor spaces, 
# the string will be returned without any manipulation.


def return_list(new_list):
    list1 = new_list.split(' ')
    return list1
    
def main():
    the_string = input("Enter the string: \n")
    result = return_list(the_string)
    print(result)
    
main()