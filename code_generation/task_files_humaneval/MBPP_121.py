# MBPP/121
### Completion
def check_triplet(arr, a, b, c):
    # Calculate the target sum
    target_sum = a + b + c
    
    # Get the length of the array
    n = len(arr)
    
    # Check all combinations of triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of the triplet equals the target sum
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return True
    return False

# Test case
assert check_triplet([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_triplet([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True
    assert check_triplet([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0) == False
    assert check_triplet([10, 4, 2, 3, 5], 5, 15, 0) == True
