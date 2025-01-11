    ###########################################################
    #  Computer Project #3
    #  
    #  Algorithm
    #  prompt if user wants to continue
    #  counter for valid triangles
    #  while loop if input is y  
    #      prompt user input for all sides
    #      condition if true
    #      print values
    #      calculations for radians
    #      calculations for degree
    #      print calculations degree
    #      print calculations for radians
    #      calculations for perimeter and area
    #      print perimeter and area
    #      conditions for tpe of triangles
    #      if condition is satisfied
    #         print corresponding identifications
    #      increas count by one
    #      prompt user for input
    #   condition
    #     print if condition is true
    #     pronpt user for input
    #   condition 
    #     print if condition is true
    #     prompt user for input
    #  condition  
    #     print if satisfied
    #  condition
    #     print if satisfied
    #
    ###########################################################

import math


BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER,"\n")

PROMPT = input("Do you wish to process a triangle (Y or N)?  ")

number_of_valid_triangles_count = 0
while PROMPT.lower() == "y":
     A = float(input('\nEnter length of side AB: '))
     B = float(input('\nEnter length of side BC: '))
     C = float(input('\nEnter length of side CA: '))
     if (A + B) > C and (A + C) > B and (B + C) > A:
         print("\n\n  Valid Triangle")
         print("\n  Triangle sides:")
         print("    Length of side AB:", A)
         print("    Length of side BC:", B)
         print("    Length of side CA:", C)
        
         print("\n  Degree measure of interior angles:")
         angle_B = float(math.acos((A ** 2 + C ** 2 - B ** 2)/(2 * A * C)))
         B_degree = float((angle_B * 180)/(math.pi))
         print("    Angle A:", round(B_degree,1))        
        
         angle_C = float(math.acos((A ** 2 + B ** 2 - C ** 2)/(2 * B * A)))
         C_degree = float((angle_C * 180)/(math.pi))
         print("    Angle B:", round(C_degree,1))
        
         angle_A = float(math.acos((C ** 2 + B ** 2 - A ** 2)/(2 * B * C)))
         A_degree = float((angle_A * 180)/(math.pi))
         print("    Angle C:", round(A_degree,1))
        
         print("\n  Radian measure of interior angles:")
         print("    Angle A:", round(angle_B,1))
         print("    Angle B:", round(angle_C,1))
         print("    Angle C:", round(angle_A,1))
        
         print("\n  Perimeter and Area of triangle:")
         perimeter = float(A + B + C)
         print("    Perimeter of triangle:", round(perimeter,1))    
        
         s = float((( A + B + C)/2))
         area = float(math.sqrt(s * (s-A) * (s-B) * (s-C)))
         print("    Area of triangle:", round(area,1))
        
        
         print("\n  Types of triangle:")
         if ( A != B != C != A):
             print("    Scalene Triangle")
         if (A == C or A == B or C == A):
             print("    Isosceles Triangle")
         if ( A == B == C):
             print("    Equilateral Triangle")
         if (A_degree != 90.0 and B_degree != 90.0 and C_degree != 90.0):
             print("    Oblique Triangle")
         if (A_degree == 90.0 or B_degree == 90.0 or C_degree == 90.0):
             print("    Right Triangle")
         if ( A_degree > 90.0 or B_degree > 90.0 or C_degree > 90.0):
             print("    Obtuse Triangle")
        
         number_of_valid_triangles_count += 1
         PROMPT = input("\nDo you wish to process another triangle? (Y or N) ")
     elif (A <= B <= C) and (A + B) == C:
        print("\n\n  Degenerate Triangle")
        PROMPT = input("\nDo you wish to process another triangle? (Y or N) ")
     elif (A + B) < C or (A + C) < B or (B + C) < A:
        print("\n\n  Not a Triangle")
        PROMPT = input("\nDo you wish to process another triangle? (Y or N) ")
if number_of_valid_triangles_count > 0:
     print("\nNumber of valid triangles:", number_of_valid_triangles_count)
elif number_of_valid_triangles_count == 0:
     print("\nNumber of valid triangles:", number_of_valid_triangles_count)
