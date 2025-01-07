# You likely learned the Euclidean distance formula in high school -- 
# the formula to find the distance between two points in a plane.  
# You will take the two coordinates 
#     as input and output the distance between them.

import math

x1_str = input("Input x1: \n")  # do not change this line
y1_str = input("Input y1: \n")  # do not change this line
x2_str = input("Input x2: \n")  # do not change this line
y2_str = input("Input y2: \n")  # do not change this line

# convert strings to ints
x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

a = x2_int - x1_int
b = y2_int - y1_int

A = a ** 2
B = b ** 2

d = math.sqrt( A + B)

#  d =
print("d =",d )  # do not change this line