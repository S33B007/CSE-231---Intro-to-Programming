# Given two integers as input, find the greatest common divisor (gcd) of them.
# GCD is the largest integer that divides each of the two integers. 
    # For example, given the numbers 12 and 15
    # The output will be
    # 3

M = input("Input the first integer: \n")
N = input("Input the second integer: \n")

m = int(M)
n = int(N)

if m< n:
     range_end = m
elif m> n:
    range_end = n
g_c_d = 0
for i in range(1,range_end+1):
    if m % i == 0 and n % i == 0:
        if i>g_c_d:
            g_c_d =i
print (g_c_d)
