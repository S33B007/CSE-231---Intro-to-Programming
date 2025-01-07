# Input a six-digit integer.
#   Assign first_three (int) to be the first three digits.
#   Assign last_two (int) to be the last two digits.
#   Assign middle_two (int) to be the middlt two digits.
# Print out the three values.

x_str = input("Input x: \n")
# remember to convert to an int

x_int = int(x_str)

a = x_int//1000
first_three = a

b = x_int % 100
last_two = b

c = x_int % 10000
d = c // 100
middle_two = d

# first_three =
# last_two =
# middle_two =
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)