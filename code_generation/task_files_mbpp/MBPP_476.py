# MBPP/476
### Completion
def big_sum(arr):
    if not arr:  # Check if the array is empty
        return 0
    largest = max(arr)
    smallest = min(arr)
    return largest + smallest

# Test the function with the provided assertion
assert big_sum([1, 2, 3]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8
