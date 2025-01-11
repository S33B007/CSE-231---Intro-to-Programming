# Write a class Student() such that it has an attribute score
# (that is initialized with 10) and three methods:

# add_score(): adds 10 to the score
# decrease_score(): decreases score by 10
# __ str __(): returns the current score (should return a string)

# p = Student()
# print(p)
# 10

# p.add_score()
# print(p)
# 20

# p.decrease_score()
# print(p)
# 10

#class Student goes here
class Student():
    def __init__(self, score=10): # we initialed score to a default value of 10 incase no parameters are passed
        self.score = score # self.score is a member variable and can be used anywher in the class

    def add_score(self):
        self.score += 10 
        return self.score

    def decrease_score(self):
        self.score -= 10
        return self.score
    def __str__(self):
        return '{}'.format(self.score)

p = Student()
print(p)
        

    
