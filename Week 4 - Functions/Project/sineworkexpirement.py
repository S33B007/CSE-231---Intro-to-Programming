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
    while X > 0:
        n = 0
        total_sin = 0
        equation = X**(2*n+1)/factorial(2*n+1)
        while abs(equation) > EPSILON:
            total_sin += equation
            n += 1
            equation = X**(2*n+1)/factorial(2*n+1)
        return round((total_sin),10)
   

X = float(input("input a number cuh: "))
answer = sinhx(X)
print(answer)


