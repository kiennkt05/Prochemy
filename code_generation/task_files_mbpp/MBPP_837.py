# MBPP/837
### Completion
def cube_Sum(n):
    return sum((2 * i + 1) ** 3 for i in range(n))

# Test the function with the provided assertion
assert cube_Sum(2) == 28
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cube_Sum(2) == 28
    assert cube_Sum(3) == 153
    assert cube_Sum(4) == 496
