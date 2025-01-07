# Given an int as the input, print all the factors of that number, 
# one in each line. 
    # For example, if the input is
    # 15
    # The output will be
    # 1
    # 3
    # 5
    # 15
    
n_str = input("Input an int: \n")
num_int = int(n_str)


for i in range (1,num_int+1):
    if num_int % i == 0:
        print(i)
