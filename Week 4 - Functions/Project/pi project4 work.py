import math
EPSILON = 0.0000001

def pi(): 
    ''' Docstring ''' 
    total_pi = 0
    n = 0
    while abs((((-1 )** n)/((2*n) + 1))) > EPSILON:
       total_pi += ((-1) ** n)/((2*n) + 1) 
       n += 1
    return round((4 * total_pi),10)
    
    
    
if option == 'P' or 'p':
    print("\npi")
    print("\nCalculated:", pi())
    print("Math:", math.pi())
    print("Diff:", (abs(pi() - math.pi()))
    print(MENU)