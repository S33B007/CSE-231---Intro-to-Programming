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
        

    
p = Student()

print(p)

# 10

p.add_score()

print(p)

# 20

p.decrease_score()

print(p)

# 10
