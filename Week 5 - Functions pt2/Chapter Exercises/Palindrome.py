# palindrome function definition goes here
def palindrome(my_str):
    my_str = my_str.lower()
    if my_str != my_str.isalpha():
        my_str = my_str.replace(" ", "")
        my_str = my_str.replace(",", "")
        my_str = my_str.replace("'", "")
        my_str = my_str.replace("!", "")
        my_str = my_str.replace("?", "")
        
    while my_str:
        if my_str[0] != my_str[-1]:
            return False
        my_str = my_str[1:-1]
    else:
        return True


my_str = input("Enter a string: \n")
print('"{:s}" is '.format(my_str),end='')
if not palindrome(my_str):
    print("not ", end = '')
print("a palindrome.")
