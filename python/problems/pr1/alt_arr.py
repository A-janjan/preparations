def get_sign(n):
    return (n > 0) - (n < 0)

num_of_inputs = int(input())
 
arrs = []

for _ in range(num_of_inputs):
    len_of_array = int(input())
    array = input()
    arr = list(map(int, array.split()))
    assert len(arr)==len_of_array
    arrs.append(arr)
    
arr_alts = []

for arr_num in range(num_of_inputs):
    arr = arrs[arr_num]
    arr_alt = []
    alt_len = 1
    for start in range(len(arr)):
        
        for pointer in range(start, len(arr)):
            if pointer+1 >= len(arr):
                break
            if (get_sign(arr[pointer]) != get_sign(arr[pointer+1])):
                alt_len += 1
                pointer += 1
            else:
                break
            
        arr_alt.append(alt_len)
        alt_len = 1
        
    arr_alts.append(arr_alt)
    
for arr_alt in arr_alts:
    result = ' '.join(map(str, arr_alt))
    print(result)