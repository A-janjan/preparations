# License Key Formatting: Format a license key string according to specific rules

def format_license_key(s, k):
    s = s.replace("-", "").upper()
    first_group_size = len(s) % k
    result = s[:first_group_size]
    
    for i in range(first_group_size, len(s), k):
        if i > 0:
            result += "-"
        result += s[i:i+k]
        
    return result


# Example usage
license_key = "2-4A0r7-4k"
k = 4
print(format_license_key(license_key, k))  # Output: "24A0-R74K"