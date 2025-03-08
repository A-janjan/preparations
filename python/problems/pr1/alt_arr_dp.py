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


results = []

for arr in arrs:
    len_of_array = len(arr)
    ans = [1] * len_of_array
    ans[len_of_array-1] = 1
    
    for i in range(len_of_array-2, 1, -1):
        if get_sign(arr[i]) != get_sign(arr[i+1]):
            ans[i] = ans[i+1] + 1
        else:
            ans[i] = 1

    results.append(' '.join(map(str, ans)))
    
for result in results:
    print(result)