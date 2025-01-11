
from cards import Card
from proj10 import waste_to_foundation

c1 = Card(3,3)
c4 = Card(10,3)
waste = [c4,c1]
c3 = Card(2,3)
c2 = Card(1,3)
foundation = [[],[],[],[]]
foundation[0].append(c2)
foundation[0].append(c3)
c5 = Card(5,3)
c6 = Card(3,1)

print("Test success due to correct color and rank.")
print("waste before function call:",waste)
print("foundation before function call:",foundation)
f_num = 0
print("f_num:",f_num)

success = waste_to_foundation( waste, foundation, f_num )
print("function return:",success)

print("waste after function call:",waste)
print("foundation after function call:",foundation)
assert success == True


print("---------------")
print("Test failure due to incorrect rank test.")
print("waste before function call:",waste)
print("foundation before function call:",foundation)
f_num = 1
print("f_num:",f_num)

success = waste_to_foundation( waste, foundation, f_num )
print("function return:",success)

print("waste after function call:",waste)
print("foundation after function call:",foundation)
assert success == False


print("---------------")
print("Test failure because of incorrect color")
c8 = Card(4,1)
waste.append(c8)
print("waste before function call:",waste)
print("foundation before function call:",foundation)
f_num = 0

print("f_num:",f_num)

success = waste_to_foundation( waste, foundation, f_num )
print("function return:",success)

print("waste after function call:",waste)
print("foundation after function call:",foundation)
assert success == False


print("---------------")
print("Test failure because destination is empty and source is not Ace.")
print("waste before function call:",waste)
print("foundation before function call:",foundation)
f_num = 3
print("f_num:",f_num)

success = waste_to_foundation( waste, foundation, f_num )
print("function return:",success)

print("waste after function call:",waste)
print("foundation after function call:",foundation)
assert success == False

print("---------------")
print("Test success because destination is empty and source is Ace.")

c8 = Card(1,2)
waste.append(c8)
print("waste before function call:",waste)
print("foundation before function call:",foundation)
f_num = 3
print("f_num:",f_num)

success = waste_to_foundation( waste, foundation, f_num )
print("function return:",success)

print("waste after function call:",waste)
print("foundation after function call:",foundation)
assert success == True