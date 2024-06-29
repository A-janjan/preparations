def find_equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    equilibrium_indices = []
    
    for i, num in enumerate(arr):
        total_sum -= num
        
        if total_sum == left_sum:
            equilibrium_indices.append(i)
            
        left_sum += num
    
    return equilibrium_indices