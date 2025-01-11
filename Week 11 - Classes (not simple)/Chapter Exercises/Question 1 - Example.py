# Write a class Example that initializes two values v1 and v2 to 0 by default, 
# and prints the values in this form:

# "Value 1: 20, Value 2: 30".

# When two objects of this class are added together using the '+' operator, 
# the result is another Example object where v1 of object 1 gets added to v1 
# of object 2 and v2 of object 1 gets added to v2 of object 2.

# Example:
    
# a = Example(20,30)
# print(a)
# Value 1: 20, Value 2: 30

# b = Example(40,50)
# print(b)
# Value 1: 40, Value 2: 50

# c=a+b
# print(c)
# Value 1: 60, Value 2: 80

#class Example goes here
class Example():
    # initializing the variable and set defualt variables to the paramter
    def __init__(self, v1 = 0, v2 = 0):
        self.value1 = v1
        self.value2 = v2
    # make a string function for the print statement
    def __str__ (self):
        out_str = "Value 1: {}, Value 2: {}".format(self.value1, self.value2)
        return out_str
    # 
    def __add__ (self, b):
        x = b.value1 + self.value1
        y = b.value2 + self.value2
        return Example(x,y)

        
