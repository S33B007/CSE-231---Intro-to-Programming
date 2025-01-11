# Given a string named s, move the first 3 letters to the back of the string.
# Print it.
    # For example, given s = "magic tortoise"
    #   will output
    #   ic tortoisemag
    # Use the input statement in the skeleton:
    # s = input("Input a string: \n")

s = input("Input a string: \n")
s_str = s[3::]
s_str2 = s[0:3]
print(s_str + s_str2)