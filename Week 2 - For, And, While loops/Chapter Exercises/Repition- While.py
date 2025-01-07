# Given a series of numbers as input, add them up until the input is 10 
# and print the total.

    # For example, if the following numbers are input
    # 8
    # 3
    # 11
    # 10
    # The output should be:
    # 22
    
num_str = input("Input an int: ")
num_int = int(num_str)

counter = 0
while num_int != 10:
    counter += num_int
    num_str = input("Input an int: ")
    num_int = int(num_str)
print(counter, "")