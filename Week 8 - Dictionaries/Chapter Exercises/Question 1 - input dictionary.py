# Write a program that asks for name from the user and then asks for a number
# and stores the two in a dictionary (called the_dict) as key-value pair. 
# The program then asks if the user wants to enter more data 
# (“More data (y/n)?” ) and depending on user choice, either asks for another 
# name-number pair or exits and stores the dictionary key, values in a list of 
# tuples and prints the list.

# Name: pranshu
# Number: 517-244-2426

# More data (y/n)? y

# Name: rich
# Number: 517-842-5425

# More data (y/n)? y

# Name: imen
# Number: 517-432-5224

# More data (y/n)? n

# [('imen', '517-432-5224'), ('pranshu', '517-244-2426'), ('rich', '517-842-5425')]

dictlist = []
the_dict = {}
while True:
    name = input("Name: \n")
    number = input("Number: \n")
    the_dict.update({name: number})
    more_data = input('More data (y/n)? \n')
    if more_data == 'y':
        continue
    elif more_data == 'n':
        break

for key, value in the_dict.items():  #we store the dictionary in a list, then sort and print
    temp = (key,value)
    dictlist.append(temp)       
print(sorted(dictlist))
