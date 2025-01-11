
from volume import Volume
DELTA = .001
V1 = Volume( 50.0, "ml" )
V2 = Volume( 60.0, "oz" )

print('V1 = Volume( 50.0, "ml") ')
print('V2 = Volume( 60.0, "oz") ')
print("-"*30)

print("Testing: Z = V1 + V2")
print("Instructor: 1824.412 ml")
Z = V1.add(V2)
print("Student:",Z)
assert abs(Z.get_magnitude() - 1824.412) < DELTA and Z.get_units() == 'ml'
print("Check the type of the result.")
assert type(Z) == Volume
print("-"*30)

print("Testing: Z = V2 + V1")
print("Instructor: 61.691 oz")
Z = V2.add(V1)
print("Student:",Z)
assert abs(Z.get_magnitude() - 61.691) < DELTA and Z.get_units() == 'oz'
print("-"*30)

print("Testing: Z = V1 - V2")
print("Instructor: Not a Volume")
Z = V1.sub(V2)
print("Student:",Z)
assert Z.get_magnitude() == 0 and Z.get_units() == None

print("-"*30)

print("Testing: Z = V2 - V1")
print("Instructor: 58.309 oz")
Z = V2.sub(V1)
print(Z.get_magnitude(),Z.get_units())
print("Student:",Z)
assert abs(Z.get_magnitude() - 58.309) < DELTA and Z.get_units() == "oz"
print("-"*30)

print("Check that V1 and V2 are unchanged.")
assert V1 == Volume( 50.0, "ml" ) and V2 == Volume( 60.0, "oz" )
print("-"*30)

V1 = Volume( 70.0, "ml" )
V2 = Volume( 1.0, "oz" )
print('V1 = Volume( 70.0, "ml") ')
print('V2 = Volume( 40.0, "oz") ')
print("Testing: Z = V1 - V2")
print("Instructor: 40.426 ml")
Z = V1.sub(V2)
print("Student:",Z)
assert abs(Z.get_magnitude() - 40.426) < DELTA and Z.get_units() == "ml"
