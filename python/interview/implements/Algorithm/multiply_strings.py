def multiply_strings(num1, num2):
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    
    for i in range(len1-1, -1, -1):
        for j in range(len2-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            total = mul + result[i+j+1]
            result[i+j+1] = total % 10
            result[i+j] += total//10
            
    rersult_str = ''.join(map(str, result))
    rersult_str = rersult_str.lstrip('0')
    
    return rersult_str if rersult_str else "0"