# MBPP/60
### Completion
def max_len_sub(arr, n):
    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) <= n:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length

# Test the function with the provided assertion
assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
    assert max_len_sub([-2, -1, 5, -1, 4, 0, 3], 7) == 4
    assert max_len_sub([9, 11, 13, 15, 18], 5) == 1
