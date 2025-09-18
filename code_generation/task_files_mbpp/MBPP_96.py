# MBPP/96
### Completion
def divisor(n):
    if n <= 0:
        return 0  # Return 0 for non-positive integers
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Test the function with the provided assertion
assert divisor(15) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert divisor(15) == 4 
    assert divisor(12) == 6
    assert divisor(9) == 3
