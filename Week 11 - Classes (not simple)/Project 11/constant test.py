
from volume import Volume
DELTA = .001
V = Volume( 50.0, "ml" )

print('V = Volume( 50.0, "ml") ')
print("-"*30)

print("Testing: Z = V + 2.5")
print("Instructor: 52.500 ml")
Z = V.add(2.5)
print("Student:",Z)
assert abs(Z.get_magnitude() - 52.500) < DELTA and Z.get_units() == 'ml'
print("-"*30)

print("Testing: Z = V - 3.5")
print("Instructor: 46.500 mt")
Z = V.sub(3.5)
print("Student:",Z)
assert abs(Z.get_magnitude() - 46.500) < DELTA and Z.get_units() == 'ml'
print("Check the type of the result.")
assert type(Z) == Volume
print("-"*30)

print("Testing: Z = V + 20")
print("Instructor: 70.000 ml")
Z = V.add(20)
print("Student:",Z)
assert abs(Z.get_magnitude() - 70) < DELTA and Z.get_units() == 'ml'
print("-"*30)

print("Testing: Z = V - 30")
print("Instructor: 20.000 ml")
Z = V.sub(30)
print("Student:",Z)
assert abs(Z.get_magnitude() - 20) < DELTA and Z.get_units() == 'ml'
print("-"*30)

print("Check that V is unchanged.")
assert V == Volume( 50.0, "ml" ) 