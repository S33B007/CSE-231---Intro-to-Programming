def leap_year(year):
    if int(year) % 4 == 0 or (int(year) % 100 == 0 and int(year) % 400 != 0) :
        return True
    else:
        return False
    
def rotate(s,n):
    return s[len(s)-n:] + s[0:len(s) - n]

print(rotate('watermelon', 4))

def digit_count(n):
    even_count = 0
    odd_count = 0
    zero_count = 0

    for i in str(n):
        if i != ".":
            if int(i) % 2 == 0 and int(i) != 0:
                even_count += 1
            elif int(i) % 2 != 0:
                odd_count += 1
            elif int(i) == 0:
                zero_count += 1
        else:
            break
    return even_count, odd_count, zero_count

def float_check(m):
    result = False
    for i in m:
        if i.isdigit() or '.' in m and m.count('.') <= 1:
            result = True
        else:
            result = False
            break
    return result
    
    
        
