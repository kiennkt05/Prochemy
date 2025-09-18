# MBPP/420
### Completion
def cube_Sum(n):
    # Calculate the sum of cubes of the first n even natural numbers
    return sum((2 * i) ** 3 for i in range(1, n + 1))

# Test the function with the provided assertion
assert cube_Sum(2) == 72
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800
