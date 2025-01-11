import math
EPSILON = 0.0000001

def e(): 
    ''' Docstring ''' 
    total_e = 0
    n = 0
    while abs(1/factorial(N)) > EPSILON:
        total_e += 1/factorial(N)
        n += 1
    return round((EPSILON * (total_e)),10)

# if option == 'E' or option == 'e':
       #     print("\ne")
       #    print("\nCalculated:", e())
       #     print("Math:", math.e)
       #     print("Diff: {:.10f}".format((abs(e() - math.e))))
       #     print(MENU)