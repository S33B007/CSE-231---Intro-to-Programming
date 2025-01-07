# A Python program which inputs a
# series of integers and processes them. The program will:
    # a) Continue to process values until the user enters the value 0
    # b) Ignore all negative integers
    # c) Count the number of odd integers entered
    # d) Count the number of even integers entered
    # e) Calculate the sum of the odd integers in the series
    # f) Calculate the sum of the even integers in the series
    # g) Display the sum of odds
    # h) Display the sum of evens
    # i) Display the count of odds
    # j) Display the count of evens
    # k) Display the total number of positive integers entered
    # l) Optional: print a message whenever a negative integer is entered



num_str = input("Input an integer (0 terminates): \n")
num = int(num_str)
# Good stuff goes here

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0
counter = 0


while num != 0:
    if num >= 0:  
        if num % 2 == 0:
            even_count +=1
            even_sum += num
        else:
            odd_count += 1
            odd_sum += num
        positive_int_count += 1
    num_str = input("Input an integer (0 terminates): \n")
    num = int(num_str)
    

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
