
from cards import Card
from proj10 import waste_to_tableau
from copy import deepcopy

c1 = Card(4,3)
c4 = Card(10,2)
waste = [c4,c1]
c3 = Card(2,1)
c2 = Card(5,2)
tableau = [[],[],[],[],[],[],[]]
tableau[0].append(c3)
tableau[0].append(c2)
c5 = Card(5,3)
c6 = Card(3,1)
tableau[1].append(c5)
tableau[1].append(c6)
c7 = Card(5,1)
tableau[2].append(c7)
instructor_tableau = deepcopy(tableau)
instructor_waste = waste[:]
print("Test failure due to color: red on red.")
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 0
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
assert waste == instructor_waste
print("---------------")

print("Test failure due to incorrect rank test.")
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 1
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
assert waste == instructor_waste

print("---------------")


print("Test failure because destination is empty and source is not king.")
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 5
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
assert waste == instructor_waste

print("---------------")

print("Test correct: red on black.")
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 2
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
instructor_tableau[t_num].append(instructor_waste.pop())
assert success == True
assert tableau == instructor_tableau
assert waste == instructor_waste

print("---------------")

print("Test success because destination is empty and source is king.")

c8 = Card(13,2)
waste.append(c8)
instructor_waste = deepcopy(waste)
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 5
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
instructor_tableau[t_num].append(instructor_waste.pop())
assert success == True
assert tableau == instructor_tableau
assert waste == instructor_waste

print("---------------")

print("Test success: black on red.")

c9 = Card(4,1)
waste.append(c9)
instructor_waste = deepcopy(waste)
print("waste before function call:",waste)
print("tableau before function call:",tableau)
t_num = 0
print("t_num:",t_num)

success = waste_to_tableau( waste, tableau, t_num )
print("function return:",success)

print("waste after function call:",waste)
print("tableau after function call:",tableau)
instructor_tableau[t_num].append(instructor_waste.pop())
assert success == True
assert tableau == instructor_tableau
assert waste == instructor_waste