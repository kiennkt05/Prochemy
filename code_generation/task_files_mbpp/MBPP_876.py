# MBPP/876
### Completion
def lcm(a, b):
    # Function to calculate the greatest common divisor (GCD)
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # LCM formula: lcm(a, b) = abs(a*b) // gcd(a, b)
    return abs(a * b) // gcd(a, b)

# Test the function with the provided assertion
assert lcm(4, 6) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lcm(4,6) == 12
    assert lcm(15,17) == 255
    assert lcm(2,6) == 6
