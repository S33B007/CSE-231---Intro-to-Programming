
from cards import Card,Deck
from proj10 import display,tableau_to_tableau
from copy import deepcopy

c1 = Card(4,3)
c4 = Card(5,4)
c3 = Card(13,1)
c2 = Card(5,2)
tableau = [[],[],[],[],[],[],[]]
tableau[0].append(c2)
tableau[0].append(c3)
c5 = Card(5,3)
c6 = Card(3,2)
tableau[1].append(c5)
tableau[1].append(c6)
c7 = Card(3,1)
tableau[2].append(c7)
tableau[3].append(c1)
tableau[4].append(c4)
instructor_tableau = deepcopy(tableau)
save_tableau = deepcopy(tableau)

c3 = Card(2,3)
c2 = Card(1,3)
foundation = [[],[],[],[]]
c5 = Card(5,3)
c6 = Card(3,1)
#tableau[1].append(c5)
#tableau[1].append(c6)
#c7 = Card(5,1)
#tableau[2].append(c7)
c8 = Card(1,1)
waste = [c8]
stock = Deck()
display(tableau, stock, foundation, waste)
print("Test failure due to mismatched rank.")
print("tableau before function call:",tableau)
t_num1 = 0
print("t_num1:",t_num1)
t_num2 = 2
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
print("---------------")

print("Test failure due to mismatched rank.")
print("tableau before function call:",tableau)
t_num1 = 3
print("t_num1:",t_num1)
t_num2 = 2
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
print("---------------")

print("Test failure due to same suit color.")
print("tableau before function call:",tableau)
t_num1 = 1
print("t_num1:",t_num1)
t_num2 = 3
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
print("---------------")


print("Test failure due to placing non-king on empty column.")
print("tableau before function call:",tableau)
t_num1 = 1
print("t_num1:",t_num1)
t_num2 = 5
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == False
assert tableau == instructor_tableau
print("---------------")


print("Test success due to placing king on empty column.")
print("tableau before function call:",tableau)
t_num1 = 0
print("t_num1:",t_num1)
t_num2 = 5
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == True
instructor_tableau[t_num2].append(instructor_tableau[t_num1].pop())
assert tableau == instructor_tableau
print("---------------")

print("Test success, correct rank and color.")
print("tableau before function call:",tableau)
t_num1 = 3
print("t_num1:",t_num1)
t_num2 = 4
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == True
instructor_tableau[t_num2].append(instructor_tableau[t_num1].pop())
assert tableau == instructor_tableau
print("---------------")
print("Test success, correct rank and color.")
print("tableau before function call:",tableau)
t_num1 = 2
print("t_num1:",t_num1)
t_num2 = 4
print("t_num2:",t_num2)

success = tableau_to_tableau( tableau, t_num1, t_num2 )
print("function return:",success)

print("tableau after function call:",tableau)
assert success == True
instructor_tableau[t_num2].append(instructor_tableau[t_num1].pop())
assert tableau == instructor_tableau
print("---------------")