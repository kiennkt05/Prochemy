# MBPP/160
### Completion
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solution(a, b, n):
    gcd, x, y = extended_gcd(a, b)
    
    # Check if n is a multiple of gcd
    if n % gcd != 0:
        return None  # No solution exists
    
    # Scale the solution
    x *= n // gcd
    y *= n // gcd
    
    return ('x = ', x, ', y = ', y)

# Example usage
assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    assert solution(4, 2, 7) == 'No solution'
    assert solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
