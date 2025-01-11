# A prime number is a natural number greater than 1 that has 
# no positive divisors other than 1 and itself.
# Write a function named is_prime that takes an integer 
# argument and returns True if the number is prime and 
# False otherwise.

def is_prime(num):
    while num > 0:
        if num >= 3 and num % 2 == 0:
            return False
        if num == 3:
            return True
            
        if num % 1 == 0 and num % num == 0 and num % 3 != 0:
            return True
        elif num % 1 == 0 and num % num == 0 and num % 3 == 0:
            return False

num = int(input("Input an integer greater than 1: \n"))

if is_prime(num):
    print("{:d} is a prime".format(num))
else:
    print("{:d} is not a prime".format(num))

