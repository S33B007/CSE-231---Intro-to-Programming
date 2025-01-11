
from volume import Volume

A = Volume( 3, "oz" )
print('A = Volume( 3, "oz" )')

print( "__str__:", str(A) )
assert str(A) == '3.000 oz'
print( "__repr__:", repr(A) )
assert repr(A) == '3.000000 oz'
print( "A.get_magnitude():", A.get_magnitude() )
assert A.get_magnitude() == 3.0
print( "A.get_units():", A.get_units() )
assert A.get_units() == 'oz'
print("Check is_valid() is True.")
assert A.is_valid()
print()

B = Volume( 1.999999, "ml" )

print('B = Volume( 1.999999, "ml"  )')

print( "__str__:", str(B) )
assert str(B) == '2.000 ml'
print( "__repr__:", repr(B) )
assert repr(B) == '1.999999 ml'
print( "B.get_magnitude():", B.get_magnitude() )
assert B.get_magnitude() == 1.999999 
print( "B.get_units():", B.get_units() )
assert B.get_units() == 'ml'
print()

C = Volume( 2.5, "tsp" )
print('C = Volume( 2.5, "tsp" )')

print( "__str__:", str(C) )
assert str(C) == 'Not a Volume'
print( "__repr__:", repr(C) )
assert repr(C) == 'Not a Volume'
print( "C.get_magnitude():", C.get_magnitude() )
assert C.get_magnitude() == None
print( "C.get_units():", C.get_units() )
assert C.get_units() == None
print("Check is_valid() is False.")
assert not C.is_valid()
print()

D = Volume( -4.5678 )
print('D = Volume( -4.5678 )')

print( "__str__:", str(D) )
assert str(D) == 'Not a Volume'
print( "__repr__:", repr(D) )
assert repr(D) == 'Not a Volume'
print( "D.get_magnitude():", D.get_magnitude() )
assert D.get_magnitude() == 0
print( "D.get_units():", D.get_units() )
assert D.get_units() == None
print()


D = Volume( 4.5678 )
print('D = Volume( 4.5678 )')

print( "__str__:", str(D) )
assert str(D) == '4.568 ml'
print( "__repr__:", repr(D) )
assert repr(D) == '4.567800 ml'
print( "D.get_magnitude():", D.get_magnitude() )
assert D.get_magnitude() == 4.5678
print( "D.get_units():", D.get_units() )
assert D.get_units() == 'ml'
print()