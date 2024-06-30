def validate_ip_address(IP: str) -> str:
    
    def is_ipv4(s):
        parts = s.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if not 0 <= int(part) <= 255:
                return False
            if part[0] == '0' and len(part) != 1:
                return False
        return True
    
    def is_ipv6(s):
        parts = s.split(":")
        if len(parts) != 8:
            return False
        hexdigits = "0123456789abcdefABCDEF"
        for part in parts:
            if len(part) == 0 or len(part) > 4:
                return False
            for char in part:
                if char not in hexdigits:
                    return False
        return True
    
    if IP.count('.') == 3 and is_ipv4(IP):
        return "IPv4"
    elif IP.count(':') == 7 and is_ipv6(IP):
        return "IPv6"
    else:
        return "Neither"
    
    
    
# Example usage
print(validate_ip_address("192.168.0.1"))        # Output: "IPv4"
print(validate_ip_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: "IPv6"
print(validate_ip_address("256.256.256.256"))    # Output: "Neither"
print(validate_ip_address("1234:5678:9abc:def::")) # Output: "Neither"