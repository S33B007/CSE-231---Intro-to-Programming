# Write a function named find_min that takes two numbers as arguments
# and returns the minimum of the two.
    # For example:
    # Given 2 and 4, the function returns 2 as the minimum.

def find_min(first,second):
    if first < second:
        return first
    else:
        return second

first = int(input("Enter first number: \n"))
second = int(input("Enter second number: \n"))
minimum = find_min(first,second)
print("Minimum: ", minimum)