# Write a function named count_case that takes a string as an argument 
# and returns the count of upper case and lower case characters in 
# the string (in that order). Any characters that are not letters 
# should be ignored

def count_case(user_input):
    count_upper = 0
    count_lower = 0
    for i in (user_input):
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lower += 1
    return (count_upper, count_lower)
        
        
        

    
print("-"*30)
print("Count Upper Case and Lower Case")
print("-"*30)

user_input = input("Enter a string: \n")
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)
