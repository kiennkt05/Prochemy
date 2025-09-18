# MBPP/633
### Completion
def pair_OR_Sum(arr, n):
    total_xor_sum = 0
    
    # Iterate through all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            total_xor_sum += arr[i] ^ arr[j]
    
    return total_xor_sum

# Test the function with the provided assertion
assert pair_OR_Sum([5, 9, 7, 6], 4) == 47
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pair_OR_Sum([5,9,7,6],4) == 47
    assert pair_OR_Sum([7,3,5],3) == 12
    assert pair_OR_Sum([7,3],2) == 4
