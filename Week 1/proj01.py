############################################################################
# Computer project #1
#
# Purpose = perform arithmetic on information then display results
#   prompt for an integer
#   input an integer
#   convert integer to float
#   perform arithmetic on float
#   display results
#
# 
####################################################################


initial_value = input( "Input rods: \n" )

rods = float(initial_value)

print ( "You input", rods, "rods.\n")

  # Number of Meter to equal 1 rod
m = rods * 5.0292

  # number of rod to equal 1 forlong
r = rods/40 

 # number of meters to equal 1 mile
ms = rods * (5.0292/1609.34)

   # number of meters to equal 1 foot
f = rods * (5.0292/0.3048)

    # number of rod to equal 1 hour
h = ((ms * 60)/(3.1))


print ( "Conversions" )
print ( "Meters:",round(m,3) ) #round the results to 3 decimals
print ( "Feet:",round(f,3) )
print ( "Miles:",round(ms,3) )
print ( "Furlongs:",round(r,3) )
print ( "Minutes to walk", rods, "rods:",round(h,3))


