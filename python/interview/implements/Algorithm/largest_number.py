from functools import cmp_to_key

def largest_number(nums):
    nums = list(map(str, nums))
    
    def compare(x, y):
        if x+y > y+x:
            return -1
        if x+y < y+x:
            return 1
        else:
            return 0
    
    nums.sort(key=cmp_to_key(compare))
    
    result = ''.join(nums)
    
    if result[0] == '0':
        return '0'
    
    return result


# Example usage
nums = [3, 30, 34, 5, 9]
print(largest_number(nums))  # Output: "9534330"