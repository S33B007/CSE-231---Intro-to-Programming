# Menu:
# add(a), remove(r), find(f): a

# Key: rich
# Value: 1
# More (y/n)? y

# Menu:

# add(a), remove(r), find(f): a
# Key: alireza
# Value: 2

# More (y/n)? n
# [('alireza', '2'), ('rich', '1')]



# add_to_dict(): takes a dictionary, a key, a value and adds the key,value pair
# to the dictionary. If key is already in dictionary then it displays the error
# message: "Error. Key already exists.". Returns dictionary.
def add_to_dict(dictionary, key,value):
    try:
        if key not in dictionary:
            dictionary[key] = value
            return dictionary
        else:
            print("Error. Key already exists.")
            return dictionary
    except:
        print("Error. Key already exists.")
        return dictionary

# remove_from_dict(): takes a dictionary and key and removes the key from the 
# dictionary. Returns dictionary. If no such key is found in the dictionary then
# it prints: "No such key exists in the dictionary.".
def remove_from_dict(dictionary, key):
    try:
        if True:
            poped = dictionary.pop(key)
            return poped
        else:
            print("No such key exists in the dictionary.")
            return dictionary
    except:
        print("No such key exists in the dictionary.")
        return dictionary

# find_key(dictt, key): takes dictionary and key and prints value corresponding 
# to the key from the dictionary: print("Value: ", value). If key is not found, 
# then prints: "Key not found." Hint: Use try-except
def find_key(dictionary, key):
    try:
        if key in dictionary:
            print("Value: ",dictionary[key])
            return dictionary
        else:
            print ("Key not found.")
            return dictionary
    except:
        print ("Key not found.")
        return dictionary



def main():
    more = True
    dictt = {}
    dictlst = []
    while more:      
        print("Menu: ")
        choice = input("add(a), remove(r), find(f): \n")
        if choice.lower() == "a":
            key = input("Key: \n")
            value = input("Value: \n")
            dictt = add_to_dict(dictt, key,value)
        elif choice.lower() == "r":
            key = input("key to remove: \n")
            dictt = remove_from_dict(dictt,key)
        elif choice.lower() == "f":
            key = input("Key to locate: \n")
            find_key(dictt,key)
        else:
            print("Invalid choice.")
            
        do_more = input("More (y/n)? \n")
        if do_more.lower() != 'y':
            more = False
    if dictt:
      for key, value in dictt.items():
          temp = (key,value)
          dictlst.append(temp)
      print(sorted(dictlst))
main()