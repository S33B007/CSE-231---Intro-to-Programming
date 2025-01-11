import math
import time
iterations = 10000
start = time.time()
for i in range(iterations):
    result = math.sqrt(i)
end = time.time()
print("{:d} calls of sqrt took {:6.4f} seconds".format(iterations, end-start))

# making a palindrome
import string
string.ascii_letters
def make_palindrome(mult_int):
    front_str = string.ascii_letters * mult_int
    back_str = front_str[::-1]
    return front_str + back_str

pal_str = make_palindrome(1)
print(pal_str, "\n")




