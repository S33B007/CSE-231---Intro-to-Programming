# Given an integer as input, print all the integers starting from 1 up to
# but not including that number. Print one number per line. 

    # For example if the input is
    # 4
    # the output should be:
    # 1
    # 2
    # 3

num_str = input("Input an int: \n")
num = int(num_str)

n = num
for i in range(1,n):
    print(i)