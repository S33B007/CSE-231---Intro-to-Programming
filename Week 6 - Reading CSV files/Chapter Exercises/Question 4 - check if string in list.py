# Write a function that takes a list as a parameter, converts every element in 
# the list to integer and then prints a tuple comprising of these integer 
# elements. If the function encounters a character such as 'p' that cannot 
# be converted to an integer, it throws this error message on the screen: 
"Error. Please enter only integers."

def list_to_tuple(a_list):
    i = 0
    new_list = []
    while i < len(a_list):
        if a_list[i].isdigit():
            i += 1
            new_list.append(a_list[i])
        else:
            i += 1
            return "Error. Please enter only integers"
            break


    int_tuple = tuple(new_list)
    return int_tuple


def main():
    a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
    print(list_to_tuple(a_list))
    

main()
                