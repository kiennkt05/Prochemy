# MBPP/84
### Completion
def sequence(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1 or n == 2:
        return 1
    
    # Initialize the sequence with the first two values
    p = [0] * (n + 1)
    p[1], p[2] = 1, 1
    
    # Fill the sequence using the defined recurrence relation
    for i in range(3, n + 1):
        p[i] = p[p[i - 1]] + p[i - p[i - 1]]
    
    return p[n]

# Test the function
assert sequence(10) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2
