###########################################################
# Computer Project #5
# open_file function:
#     This function prompts the user to input a file name to open and keeps prompting until a
#     correct name is entered
# read_names function:
#     This function reads the Names.txt file using file pointer, fp'
# read friends function:
#     This function reads the Friends.csv file using file pointer, fp.
# create friends dict function:
#     This function takes the two lists created in the read_names function and the
#     read_friends function and builds a dictionar
# find common friends function:
#     This function takes two names (strings) and the friends_dict (returned by the
#     create_friends_dict) and returns a set of friends that the two names have in
#     common
# find max friends function:
#     This function takes a list of names and the corresponding list of friends and determines
#     who has the most friends. It returns a list of those with the most friends and how many
#     friends they have.
# find max common friends function:
#     This function takes the friends dictionary and finds which pairs of people have the most
#     friends in common. It returns a list of those pairs with the most common friends and how
#     many friends they have
# find second friends:
#     For each person in
#     the network find the friends of their friends, but don’t include the person’s first order
#     friends or themselves.
# find max second friends function:
#     will find max second-order friends. Return
#     a list of names (strings) and the int that is the maximum number of second-order
#     friendships.
# main
#    Depending on the option selected it would prompt the user for an appropriate option and
#    display the result based on the selection. The function would keep prompting the user for
#    option until the user quits
###########################################################

MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    ''' This function prompts the user to input a file name to open and keeps prompting until a
        correct name is entered'''
    filename = input("\nInput a {} file: ".format(s))
    while True:
        try:
            fp = open(filename,"r",encoding ="windows-1252")
            return fp
        except FileNotFoundError:
            print("\nError in opening file.")
            filename = input("\nInput a {} file: ".format(s))  
    return fp

def read_names(fp):
    '''This function reads the Names.txt file using file pointer, fp'''
    name_list = []
    for line in fp:
        new_line = line[0:-1]
        name_list.append(new_line)
    return name_list

def read_friends(fp,names_lst):
    '''This function reads the Friends.csv file using file pointer, fp.'''
    master_list = []
    line_list = []
    for line in fp:
        list_of_indexes = line.strip().split(",")
        new_list_of_indexes = list_of_indexes[0:-1]
        for index in new_list_of_indexes:
            int_index = int(index)
            name = names_lst[int_index] 
            line_list.append(name)
        master_list.append(line_list)
        line_list = []
    return master_list


def create_friends_dict(names_lst,friends_lst):
    '''This function takes the two lists created in the read_names function and the
        read_friends function and builds a dictionary'''
    friends_dict = dict(zip(names_lst,friends_lst))
    return friends_dict
            
def find_common_friends(name1, name2, friends_dict):
    '''This function takes two names (strings) and the friends_dict (returned by the
        create_friends_dict) and returns a set of friends that the two names have in
        common'''
    set_name1 = set(friends_dict[name1])
    set_name2 = set(friends_dict[name2])
    set_names = set_name1.intersection(set_name2)
    return set_names

def find_max_friends(names_lst, friends_lst):
    '''This function takes a list of names and the corresponding list of friends and determines
        who has the most friends. It returns a list of those with the most friends and how many
        friends they have. '''
    max_dict = {}
    max_name = []
    max_friends = []
    index = 0
    for i in range(len(names_lst)):
        # since the index of names correspdong with friends list, we will go by it's index
        names = names_lst[i] # this is the name 
        # once index reaches 10 this condition won't run
        if index < len(friends_lst):
            # use the index of friends list to get the total of the list and append to toal friends
            friends = friends_lst[index]
            total_friends = len(friends)
            index += 1
            max_friends.append(total_friends)
            # add to dictionary
            max_dict[names] = total_friends
    highest = max(max_friends) # take the highest  number of the list
    max_keys = [key for key, value in max_dict.items() if value == highest]
    # for key, value in max_dict.items():
          # if value == (max_dict.value()):
                # max_key.append(key)
    max_keys.sort()
    return max_keys, highest
   
def find_max_common_friends(friends_dict):
    '''This function takes the friends dictionary and finds which pairs of people have the most
        friends in common. It returns a list of those pairs with the most common friends and how
        many friends they have'''
    master_dict = {}
    # going through each key, value par in a dictionary
    for key1, value1 in friends_dict.items():
        # this is the outer loop 
        for key2, value2 in friends_dict.items():
            # this is inner loop
            if (key2, key1) in master_dict: # rule 1 
                continue
            if key1 in value2 or key2 in value1: # rule 2
                continue
            if key1 == key2: # rule 3
                continue
            common_friends = find_common_friends(key1, key2, friends_dict)
            master_dict[(key1, key2)] = common_friends
    max_list = []
    for value in master_dict.values():
        len_value = len(value)
        max_value = len_value
        max_list.append(max_value)

    highest = max(max_list)
    max_keys = [key for key, value in master_dict.items() if len(value) == highest]

    return max_keys, highest
                

    
def find_second_friends(friends_dict):
    '''For each person in
        the network find the friends of their friends, but don’t include the person’s first order
        friends or themselves. '''
    result_dict = {}
    for original_person in friends_dict:
        # under the first for loop, create that person's second order of friends empty set
        set_of_second_order_friends = set()
        # ^1st order friends are the value in the friends dictionary
        # friend_dict[a] = # first order firends
        first_order_friends = friends_dict[original_person]
        for fof_person in first_order_friends: # for every friend in the ^first order friends, you want to get their friends list
            # 2nd order friends are (friends of the ^first order of freinds) = list
            second_order_friends = list(friends_dict[fof_person])
            for second_order_friend in second_order_friends:
                if second_order_friend == original_person:
                    continue
                if second_order_friend in first_order_friends:
                    continue
                else:
                   set_of_second_order_friends.add(second_order_friend)
        # after the 2 loops
        result_dict[original_person] = set_of_second_order_friends
    return result_dict

def find_max_second_friends(seconds_dict):
    '''will find max second-order friends. Return
        a list of names (strings) and the int that is the maximum number of second-order
        friendships.'''
    max_list = []
    index = 0
    for i in range(len(seconds_dict)):
        for value in seconds_dict.values():
            len_value = len(value)
            if index < len(seconds_dict):
                max_value = len_value
                max_list.append(max_value)
                index += 1
    highest = max(max_list)
    max_keys = [key for key, value in seconds_dict.items() if len(value) == highest]
    return max_keys, highest


def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            prompt = input("\nEnter a name: ")
            while True:
                if prompt not in friends_dict:
                    print("\nThe name {} is not in the list.".format(prompt))
                    prompt = input("\nEnter a name: ")
                else:
                    print("\nFriends of {}:".format(prompt))
                    for key in friends_dict[prompt]:
                        print(key)

                    break

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
