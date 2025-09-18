# MBPP/504
### Completion
def sum_Of_Series(n):
    return sum(i**3 for i in range(1, n + 1))

# Test the function
assert sum_Of_Series(5) == 225
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_Series(5) == 225
    assert sum_Of_Series(2) == 9
    assert sum_Of_Series(3) == 36
