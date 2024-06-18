# palindrome index


def palindromeIndex(s):
    if(len(s)==1):
        return -1
    
    if palindromeCheck(s):
        return -1
    
    for index in range(len(s)):
        if(index==len(s)-1):
            new_str = s[:index]
        else:
            new_str = s[:index]+s[index+1:]
        if(palindromeCheck(new_str)):
            return index
    return -1

def palindromeCheck(s):
    reversed_str = s[::-1]
    if(reversed_str == s):
        return True
    else:
        return False