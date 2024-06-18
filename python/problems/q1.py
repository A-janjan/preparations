def caesarCipher(s, k):
    k %= 26
    result = ''
    for i in s:
        if(i.isalpha()):
            if(96<ord(i)<123):
                if(96<ord(i)+k<123):
                    result = result + chr(ord(i) + k)
                elif(ord(i)+k>122):
                    result = result + chr(ord(i) + k - 122 + 96)
            elif(64<ord(i)<91):
                if(64<ord(i)+k<91):
                    result = result + chr(ord(i) + k)
                elif(ord(i)+k>90):
                    result = result + chr(ord(i) + k - 90 + 64)
        else:
            result = result + i
    return result


s = "abcdefghijklmnopqrstuvwxyz"
k = 2
result = caesarCipher(s,k)

desired = "cdefghijklmnopqrstuvwxyzab"


if(result == desired):
    print("SUCCESS")
else:
    print("FAILURE")