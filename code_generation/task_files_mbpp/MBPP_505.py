# MBPP/505
### Completion
def re_order(arr):
    # Initialize a new list to hold non-zero elements
    non_zeroes = [num for num in arr if num != 0]
    # Count the number of zeroes
    zeroes_count = arr.count(0)
    # Extend the non-zero list with the zeroes
    return non_zeroes + [0] * zeroes_count

# Test the function with the provided assertion
assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
    assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
    assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]
