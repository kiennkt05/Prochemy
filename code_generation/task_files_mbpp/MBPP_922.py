# MBPP/922
### Completion
def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    # Initialize variables to keep track of the two largest numbers
    max1 = max2 = float('-inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return (max2, max1)

# Test the function with the provided assertion
assert max_product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product([1, 2, 3, 4, 7, 0, 8, 4])==(7, 8)
    assert max_product([0, -1, -2, -4, 5, 0, -6])==(-4, -6)
    assert max_product([1, 3, 5, 6, 8, 9])==(8,9)
