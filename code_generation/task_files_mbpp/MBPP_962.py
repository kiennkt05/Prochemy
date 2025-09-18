# MBPP/962
### Completion
def sum_Even(l, r):
    # Ensure l is even; if not, increment it by 1
    if l % 2 != 0:
        l += 1
    # Ensure r is even; if not, decrement it by 1
    if r % 2 != 0:
        r -= 1
    # Calculate the sum of even numbers in the range
    return sum(range(l, r + 1, 2))

# Test the function with the provided assertion
assert sum_Even(2, 5) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Even(2,5) == 6
    assert sum_Even(3,8) == 18
    assert sum_Even(4,6) == 10
