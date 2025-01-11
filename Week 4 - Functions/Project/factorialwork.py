def factorial(N): 
    ''' Calculate factorial of a number ''' 
    if N == 0:
       print(1)
    return
    for i in range(1, N):
       fact = N * i
       N = fact
    return print(N)
   

N = int(input("input a number cuh: "))
answer = factorial(N)
