# Write a class Example() such that it has a method that gives the difference
# between the size of strings when the '-' (subtraction) symbol is used between
# the two objects of the class. Additionally, implement a method that returns 
# True if object 1 length is greater than object 2 length and False otherwise 
# when the (>) (greater than) symbol is used.

# Example:

# obj1 = Example('this is a string')
# obj2 = Example('this is another one')
# print(obj1 > obj2)
# False
# print(obj1-obj2)
# 3

#class Example goes here
class Example(object):

    def __init__(self, string=''):
        self.__string = string

    def __sub__(self, other):
       return len(self.__string) - len(other.__string)

    def __gt__(self, other):
        return len(self.__string) > len(other.__string)

    def __str__(self):
        pass