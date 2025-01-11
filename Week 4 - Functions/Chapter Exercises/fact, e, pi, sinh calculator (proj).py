###########################################################

    #  Computer Project #5
    # function for factorial
    #      Calculate factorial of an integer value
    #      N: the integer value
    #      Returns: N after calculated
    # function for e
    #     Calculates e 
    #     uses factorial
    #     Returns: e
    # function for pi
    #     Calculates pi 
    #     Returns: pi
    # function for sinh
    #     Calculate sine of an integer value
    #     x: an inputted integer value
    #     Returns: the calculated sinh of the integer value
    # function for main line of code
    #     prints menu variable
    #     input a str
    #     while loop for if not x:
    #         loop for str F or f:
    #             input variable
    #             condition to check a not digit:
    #                 print invalid
    #             else:
    #                 change str input to int
    #             condition to check int
    #             else:
    #                 invoke factorial funcition
    #           if str is P or p:
    #               print following str
    #           if str is E or e:
    #               print following str
    #           loop for str S or s:
    #             input variable
    #             invoke sinh
    #           if function return None:
    #             print str
    #           else:
    #             turn function returned to float
    #             print following str
    #     if str is M or m:
    #         print following str
    #     if str is not any provided:
    #         orint following str
    #     prompt for user input
    #     print menu
    # print following str
        
    ###########################################################




import math
EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(N): 
    ''' Calculate factorial of an integer value
    N: the integer value
    Returns: N after calculated
    ''' 
    N = int(N)
    if N == 0:
       return 1
    if N > 0:
        fact = 1
        for i in range(1, N + 1):
           fact = fact * i
        return fact

 
def e(): 
    ''' Calculates e 
    uses factorial
    Returns: e
    ''' 
    total_e = 0
    n = 0
    while abs(1/math.factorial(n)) > EPSILON:
        total_e += 1/math.factorial(n)
        n += 1
    return round((total_e),10)

def pi(): 
    ''' Calculates pi 
    Returns: pi
    ''' 
    total_pi = 0
    n = 0
    while abs((((-1 )** n)/((2*n) + 1))) > EPSILON:
       total_pi += ((-1) ** n)/((2*n) + 1) 
       n += 1
    return round((4 * total_pi),10)

def sinh(x): 
    ''' Calculate sine of an integer value
    try x as a float 
except when it returns ValueError
just return None
    x: an inputted integer value
    Returns: the calculated sinh of the integer value
    ''' 
    try:
        x = float(x) 
    except ValueError:
        return None
        
    n = 0
    total_sin = 0
    equation = x**(2*n+1)/math.factorial(2*n+1)
    while math.fabs(equation) > EPSILON:
       total_sin += equation
       n += 1
       equation = x**(2*n+1)/math.factorial(2*n+1)
    return round((total_sin),10)

def main(): 
    print(MENU) 
    option = input("\nChoose an option: ")
    while option != 'x' and option != 'X':
        if option == 'F' or option == 'f':
            print("\nFactorial")
            N = input("Input non-negative integer N: ")
            if not N.isdigit():
                print("\nInvalid N.")
            else:
                N = int(N) 
                if N <= 0:
                    print("\nInvalid N.")
                elif N >=0:
                    answer = factorial(N)
                    print("\nCalculated:", answer)
                    print("Math:", math.factorial(N))
                    print("Diff:", abs(factorial(N) - math.factorial(N))) 
        elif option == 'P' or option == 'p':
            print("\npi")
            print("Calculated:", pi())
            print("Math: {:.10f}".format(math.pi))
            print("Diff: {:.10f}".format((abs(pi() - math.pi))))
        elif option == 'E' or option == 'e':
            print("\ne")
            print("Calculated:", e())
            print("Math: {:.10f}".format(math.e))
            print("Diff: {:.10f}".format((abs(e() - math.e))))
        elif option == 'S' or option == 's':
            print("\nsinh")
            x = input("X in radians: ")
            answer = sinh(x)
            if answer == None:
                print("\nInvalid X.")
            else:
                math_answer = math.sinh(float(x))
                print("\nCalculated:", answer)
                print("Math: {:.10f}".format(math_answer))
                print("Diff: {:.10f}".format((abs(answer - math_answer))))
        elif option == 'M' or option == 'm':
            print(MENU)
        else:
            print("\nInvalid option:", option.upper())
            print(MENU)
        option = input("\nChoose an option: ")  
        
    print("\nThank you for playing.")  

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()