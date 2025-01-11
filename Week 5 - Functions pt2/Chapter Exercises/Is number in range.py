# Write a function named range_test that takes an integer as an 
# argument and returns True if the number is within the range 1 to 555 
# (not inclusive, i.e. neither 1 nor 555 are in range). 
# Otherwise return False.

def range_test(num):
    count = 0
    for i in range(2,555,1):
        while count < i:
            if i == num:
                return True
            else:
                count += 1


num = int(input("Enter a number: \n"))
if range_test(num):
    print( "{:d} is in range.".format(num))
else:
    print("The number you entered is outside the range!")
