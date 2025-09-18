# MBPP/137
### Completion
def zero_count(arr):
    if not arr:  # Check if the array is empty
        return 0.0
    zeroes = arr.count(0)  # Count the number of zeroes in the array
    return zeroes / len(arr)  # Calculate the ratio of zeroes

# Test the function with the provided assertion
assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.15
    assert zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.00
    assert zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.00
