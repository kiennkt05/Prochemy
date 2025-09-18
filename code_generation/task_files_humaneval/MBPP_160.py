# MBPP/160
### Completion
def extended_gcd(a, b):
    """Return gcd of a and b, and coefficients x, y such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solution(a, b, n):
    """Find integers x and y such that ax + by = n"""
    gcd, x0, y0 = extended_gcd(a, b)
    
    # Check if a solution exists
    if n % gcd != 0:
        return None  # No solution exists
    
    # Scale the solution
    scale = n // gcd
    x = x0 * scale
    y = y0 * scale
    
    return ('x = ', x, ', y = ', y)

# Test the function with the provided test case
assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)

# Additional test cases
print(solution(2, 3, 7))  # Expected output: ('x = ', 2, ', y = ', 1)
print(solution(2, 3, 1))  # Expected output: None (no solution)
print(solution(5, 7, 1))  # Expected output: ('x = ', 3, ', y = ', -2)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    assert solution(4, 2, 7) == 'No solution'
    assert solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
