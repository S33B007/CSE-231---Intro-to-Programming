
from cards import Card,Deck
from proj10 import display,tableau_to_tableau, tableau_to_foundation
from copy import deepcopy

c1 = Card(1,3)
c1.flip_card()
c4 = Card(5,4)
c4.flip_card()
c3 = Card(13,1)
c2 = Card(5,2)
c2.flip_card()
tableau = [[],[],[],[],[],[],[]]
tableau[0].append(c2)
tableau[0].append(c1)
tableau[0].append(c3)
c5 = Card(5,3)
c5.flip_card()
c6 = Card(3,1)
tableau[1].append(c5)
tableau[1].append(c6)
c7 = Card(3,2)
c8 = Card(4,3)
c9 = Card(5,1)
tableau[2].append(c7)
tableau[3].append(c8)
tableau[4].append(c9)
instructor_tableau = deepcopy(tableau)
save_tableau = deepcopy(tableau)

foundation = [[],[],[],[]]
instructor_foundation = deepcopy(foundation)
#tableau[1].append(c5)
#tableau[1].append(c6)
#c7 = Card(5,1)
#tableau[2].append(c7)
c8 = Card(1,1)
waste = [c8]
stock = Deck()
display(tableau, stock, foundation, waste)

# print("Face Up status")
# for L in tableau:
#     for c in L:
#         print(c.is_face_up(),end=",")
#     print()
face_up_L = [[False,False,True],
[False,True],
[True],
[True],
[True]]

print("Test failure (tableau_to_tableau) -- no change.")
print("tableau before function call:", tableau)
t_num1 = 0
print("t_num1:", t_num1)
t_num2 = 2
print("t_num2:", t_num2)

success = tableau_to_tableau(tableau, t_num1, t_num2)
print("function return:", success)

print("tableau after function call:", tableau)
assert success == False
assert tableau == instructor_tableau
# check face up status
for i in range(7):
    for j in range(len(tableau[i])):
        c = tableau[i][j]
        assert(c.is_face_up()==face_up_L[i][j])

print("---------------")

print("Test failure (tableau_to_foundation) -- no change.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
t_num = 3
print("t_num:",t_num)
f_num = 2
print("f_num:",f_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == False
assert tableau == instructor_tableau
assert foundation == instructor_foundation
# check face up status
for i in range(7):
    for j in range(len(tableau[i])):
        c = tableau[i][j]
        assert(c.is_face_up()==face_up_L[i][j])

print("---------------")

print("Test success (tableau_to_tableau) -- cards flipped.")
print("tableau before function call:", tableau)
t_num1 = 1
print("t_num1:", t_num1)
t_num2 = 3
print("t_num2:", t_num2)

success = tableau_to_tableau(tableau, t_num1, t_num2)
print("function return:", success)

print("tableau after function call:", tableau)
assert success == True
instructor_tableau[t_num2].append(instructor_tableau[t_num1].pop())
face_up_L = [[False,False,True],
[True],
[True],
[True,True],
[True]]
# check face up status
for i in range(7):
    for j in range(len(tableau[i])):
        c = tableau[i][j]
        assert(c.is_face_up()==face_up_L[i][j])

print("---------------")

print("Test success (tableau_to_tableau) -- cards flipped.")
print("tableau before function call:", tableau)
t_num1 = 0
print("t_num1:", t_num1)
t_num2 = 5
print("t_num2:", t_num2)

success = tableau_to_tableau(tableau, t_num1, t_num2)
print("function return:", success)

print("tableau after function call:", tableau)
assert success == True
instructor_tableau[t_num2].append(instructor_tableau[t_num1].pop())
face_up_L = [[False,True],
[True],
[True],
[True,True],
[True],
[True]]
# check face up status
for i in range(7):
    for j in range(len(tableau[i])):
        c = tableau[i][j]
        assert(c.is_face_up()==face_up_L[i][j])
print("---------------")

print("Test success (tableau_to_foundation) -- no cards flipped.")
print("tableau before function call:",tableau)
print("foundation before function call:",foundation)
t_num = 0
print("t_num:",t_num)
f_num = 2
print("f_num:",f_num)

success = tableau_to_foundation( tableau, foundation, t_num, f_num )
print("function return:",success)

print("tableau after function call:",tableau)
print("foundation after function call:",foundation)
assert success == True
instructor_foundation[f_num].append(instructor_tableau[t_num].pop())
assert tableau == instructor_tableau
assert foundation == instructor_foundation
face_up_L = [[True],
[True],
[True],
[True,True],
[True],
[True]]
# check face up status
for i in range(7):
    for j in range(len(tableau[i])):
        c = tableau[i][j]
        assert(c.is_face_up()==face_up_L[i][j])
print("---------------")