# Given the number n as input, print the first n odd numbers starting from 1.
    # For example if the input is
    # 4
    # The output will be:
    # 1
    # 3
    # 5
    # 7

n_str = input("Input an int: ")
num_int = int(n_str)

n = num_int
for i in range(1,2*n,2):
    print (i)
