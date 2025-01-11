# Given a string of any length named s.
# Extract and then print the first and last characters of the string
# (with one space between them).
    # For example, given
    #   s = 'abcdef'
    # The output will be
    #   a f
    # Use the input statement provided in the skeleton:
    #   s = input("Input a string: \n")


n_str = input("Input a string: \n")
index_int = 0
limit = n_str[-1]
print(n_str[index_int], limit )