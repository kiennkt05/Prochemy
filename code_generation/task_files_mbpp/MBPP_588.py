# MBPP/588
### Completion
def big_diff(arr):
    if not arr:  # Check if the array is empty
        return 0
    return max(arr) - min(arr)

# Test the function with the provided assertion
assert big_diff([1, 2, 3, 4]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7
