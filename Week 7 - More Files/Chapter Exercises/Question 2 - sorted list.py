# Write a function sort_list() that accepts a list of integers and sorts it. 
# The function should not explicitly 'return' this list and yet the list will be 
# sorted when printed within main() after being passed to sort_list() as a 
# parameter. Complete the main() module such that it accepts numbers from the 
# user, until an empty string is entered, and stores them in a list called 
# a_list.

# Input:
# 2
# 32
# 43
# 12
# 24
# 32

# Output:
# [2, 32, 43, 12, 24, 32]
# [2, 12, 24, 32, 32, 43]

def sort_list(a_list):
    sorted_a_list = a_list.sort()
    return sorted_a_list

def main():
    #loop to accept integers until an empty string is entered goes here
    a_list = []
    input_for_list = (input())
    while  True:
        if not input_for_list:
            break
        int_input = int(input_for_list)
        a_list.append(int_input)
        input_for_list = input()

    ######Do not modify this part######
    print(a_list)
    sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here
if __name__ == "__main__":
    main()