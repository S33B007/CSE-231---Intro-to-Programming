#  Given input that represents a floating point number, that is, 
# made up of digits and at least one decimal point, c
# onvert the input to a float and print it with 
# the following specifications:
#  field width of 12
# 2 decimal digits of precision
# right justified
    # For example, if the input is
    # 1234.56789
    # The output will be
    #       1234.57
    # 123456789012
    
s = input("Input a float: \n")
s_float = float(s)
print("{:>12.2f}".format(s_float))