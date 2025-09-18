# MBPP/468
### Completion
def max_product(arr, n):
    if n == 0:
        return 0
    
    # Initialize the max_product array
    max_prod = [0] * n
    
    # Each element is a subsequence of length 1
    for i in range(n):
        max_prod[i] = arr[i]
    
    # Compute the maximum product for increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if it's an increasing subsequence
                max_prod[i] = max(max_prod[i], max_prod[j] * arr[i])
    
    # The result is the maximum value in max_prod
    return max(max_prod)

# Test the function with the provided assertion
assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000 
    assert max_product([4, 42, 55, 68, 80], 5) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000 
