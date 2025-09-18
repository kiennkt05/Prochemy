# MBPP/865
### Completion
def ntimes_list(lst, n):
    return list(map(lambda x: x * n, lst))

# Test the function with the provided assertion
assert ntimes_list([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6, 9, 12, 15, 18, 21]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],10)==[10, 20, 30, 40, 50, 60, 70]
