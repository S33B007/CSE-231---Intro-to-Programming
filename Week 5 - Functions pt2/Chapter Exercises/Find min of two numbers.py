# Write a function named find_min that takes two numbers as arguments and 
# returns the minimum of the two.
    # For example:
    # Given 2 and 4, the function returns 2 as the minimum.
    
def find_min(first,second):
    if first < second:
        return first
    elif second < first:
        return second
    else:
        statement = "The numbers are equal"
        return statement

first = int(input("Enter first number: \n"))
second = int(input("Enter second number: \n"))
minimum = find_min(first,second)
if minimum.isdigit():
    print("Minimum: ", minimum)
else:
    print (minimum)
