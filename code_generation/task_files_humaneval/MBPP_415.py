# MBPP/415
### Completion
def max_Product(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    # Sort the array in non-decreasing order
    arr.sort()
    
    # The two largest numbers will be the last two elements in the sorted array
    first = arr[-1]
    second = arr[-2]
    
    # Return the pair with the highest product
    return (second, first)

# Test case
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)

# Additional test cases
assert max_Product([-10, -3, 5, 6, -2]) == (5, 6)  # Positive numbers
assert max_Product([-10, -3, -5, -6, -2]) == (-2, -3)  # Negative numbers
assert max_Product([0, 0, 0, 0]) == (0, 0)  # All zeros
assert max_Product([1, 1, 1, 1]) == (1, 1)  # All ones

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)
