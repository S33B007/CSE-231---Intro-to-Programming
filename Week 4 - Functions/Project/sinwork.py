EPSILON = 0.0000001

def factorial(N): 
    ''' Calculate factorial of a number ''' 
    if N == 0:
       return 1
    for i in range(1, N):
       fact = N * i
       N = fact
    return N
   




def sinhx(X): 
    ''' Calculate sine of a number ''' 
    
    total_e = 0
    n = 0
    formula = X**(2*n+1)/factorial(2*n+1)
    while formula > EPSILON:
        total_e += formula
        n += 1
        formula = X**(2*n+1)/factorial(2*n+1)
    return round((total_e),10)
    # N = 0
    # a = (2*N) + 1
    # numerator = float(X**a)
    # denominator = factorial(a)
    # total_sin = X
    # equation = float(numerator/denominator)
    # while abs(equation - total_sin) >= 0:
    #     total_sin += equation
    #     N += 1
    # return float(total_sin * EPSILON)
   

X = float(input("input a number cuh: "))
answer = sinhx(X)
print(answer)

