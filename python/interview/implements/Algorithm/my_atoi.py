def my_atoi(s: str) -> int:
    INT_MAX = 2**31-1
    INT_MIN = -2**31
    
    i = 0
    n = len(s)
    
    
    while i < n and s[i].isspace():
        i += 1
        
    sign = 1
    if i < n and s[i] == '+':
        i += 1
    elif i < n and s[i] == '-':
        sign = -1
        i += 1
        
    result = 0
    
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = digit + result * 10
        if result * 10 + digit > INT_MAX:
            return INT_MAX if sign>0 else INT_MIN
        
        result = result * 10 + digit
        i += 1
        
    return sign * result