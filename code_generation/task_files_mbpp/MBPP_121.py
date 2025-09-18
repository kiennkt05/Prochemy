# MBPP/121
### Completion
def check_triplet(arr, a, b, c):
    # Create a set to store the elements of the array
    elements = set(arr)
    
    # Check for each pair (a, b) if (c - a - b) exists in the set
    for x in arr:
        for y in arr:
            if x != y:  # Ensure we are not using the same element
                z = a + b + c - x - y
                if z in elements:
                    return True
    return False

# Test the function with the provided assertion
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
