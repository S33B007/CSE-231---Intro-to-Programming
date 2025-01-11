
# mutate_list() takes 3 parameters -- 
# a list, index number, and a value -- and inserts the value in the position 
# specified by the index number in the list.
def mutate_list(user_list, index_num, v):
    user_list.insert(index_num, v)
    return user_list
# remove_index() takes 2 parameters --
#  a list and an index number -- and remove the element at the position number
#  indicated by index. It also prints the total number of elements in the list 
#  before and after removing the character in this fashion:
def remove_index(user_list, index_num):
    print("Total elements in list =",len(user_list))
    user_list.pop(index_num)
    print("Total elements in list =",len(user_list))
    return user_list
# 3.   reverse_list() takes 1 parameter -- a list -- 
# and returns the list reversed.
def reverse_list(user_list):
    user_list.reverse()
    return user_list


# The main() module in the starter code below takes integer inputs separated by 
# commas from the user and stores them in a list. Then, it allows the user to 
# manipulate the list using 3 functions:
def main():
    user_list = input("Enter values in list separated by commas: \n")
    user_list = user_list.split(",") # turns the string into a list
    user_list = [int(i) for i in user_list] # turns each string in list to int
    print(user_list)
    print("Menu: ")
    print("mutate list(m), remove (r), reverse_list (R)")
    user_choice = input("Enter choice (m,r,R): \n")
    if user_choice == 'm':
        index_num, v = input("\n").split(",")
        index_num = int(index_num)
        v = int(v)
        mutate_list(user_list, index_num, v)
        print(user_list)
    elif user_choice == 'r':
        index_num = int(input("\n"))
        remove_index(user_list, index_num)
        print(user_list)
    elif user_choice == 'R':
        new_list = reverse_list(user_list)
        print(new_list)
main()