
from cards import Card,Deck
from proj10 import display,tableau_to_foundation
from copy import deepcopy

c1 = Card(3,3)
c4 = Card(10,2)
c3 = Card(1,1)
c2 = Card(5,2)
tableau = [[],[],[],[],[],[],[]]
tableau[0].append(c3)
#tableau[0].append(c2)
c5 = Card(5,3)
c6 = Card(3,3)
tableau[1].append(c5)
tableau[1].append(c6)
c7 = Card(3,1)
tableau[2].append(c7)
instructor_tableau = deepcopy(tableau)
save_tableau = deepcopy(tableau)

c3 = Card(2,3)
c2 = Card(1,3)
foundation = [[],[],[],[]]
foundation[0].append(c2)
foundation[0].append(c3)
instructor_foundation = deepcopy(foundation)
save_foundation = deepcopy(foundation)
c5 = Card(5,3)
c6 = Card(3,1)
#tableau[1].append(c5)
#tableau[1].append(c6)
#c7 = Card(5,1)
#tableau[2].append(c7)
waste = [c6]
stock = Deck()
display(tableau, stock, foundation, waste)
print("Test failure due to mismatched suit.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
f_num = 0
print("f_num:",f_num)
t_num = 2
print("t_num:",t_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == False
assert tableau == instructor_tableau
assert foundation == instructor_foundation
print("---------------")

print("Test failure due to incorrect rank.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
f_num = 0
print("f_num:",f_num)
t_num = 0
print("t_num:",t_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == False
assert tableau == instructor_tableau
assert foundation == instructor_foundation
print("---------------")

print("Test failure because destination is empty and source is not Ace.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
f_num = 1
print("f_num:",f_num)
t_num = 1
print("t_num:",t_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == False
assert tableau == instructor_tableau
assert foundation == instructor_foundation
print("---------------")

print("Test correct.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
f_num = 0
print("f_num:",f_num)
t_num = 1
print("t_num:",t_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)

assert success == True
instructor_foundation[f_num].append(instructor_tableau[t_num].pop())
print(instructor_tableau)
print("tableau after function call:",tableau)
assert tableau == instructor_tableau
assert foundation == instructor_foundation
print("---------------")

print("Test correct: Ace to empty foundation.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
f_num = 1
print("f_num:",f_num)
t_num = 0
print("t_num:",t_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == True
instructor_foundation[f_num].append(instructor_tableau[t_num].pop())
assert tableau == instructor_tableau
assert foundation == instructor_foundation
print("---------------")

