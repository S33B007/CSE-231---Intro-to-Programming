# Write a function called game_of_eights() that accepts a list of numbers as an 
# argument and then returns True if two consecutive eights are found in the list.
# For example: [2,3,8,8,9] -> True.

# the function returns True if consecutive eights (8) are found in the list; 
# returns False otherwise.

# the function can handle the edge case where the last element of the list is an
# 8 without crashing.

# the function prints out an error message saying 
# 'Error. Please enter only integers.' if the list is found 
# to contain any non-numeric characters.

# Enter elements of list separated by commas: 2,3,8,8,5
# True

# Enter elements of list separated by commas: 3,4,5,8
# False

# Enter elements of list separated by commas: 2,3,5,8,8,u
# Error. Please enter only integers.

def game_of_eights(a_list):
    for i in range(len(a_list)):
        if a_list[i] == 8 and a_list[i-1] == 8:
            return True
    return False

# The main() function will accept a list of numbers separated by commas from the
# user and send it to the game_of_eights() function. Within the game_of_eights()
# function, you will provide logic such that:

def main():
    a_list = input("Enter elements of list separated by commas: \n").split(',')
    new_list = []
    for value in a_list:
        try:
            new_value = int(value)
            new_list.append(new_value)
            if len(a_list) == len(new_list):
               result = game_of_eights(new_list)
               print(result) 
        except ValueError:
            print("Error. Please enter only integers.")
            break

    

main()