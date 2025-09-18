# MBPP/127
### Completion
def multiply_int(a, b):
    # Determine the sign of the result
    negative_result = (a < 0) ^ (b < 0)  # Result is negative if one is negative and the other is positive
    
    # Work with absolute values
    a, b = abs(a), abs(b)
    
    result = 0
    while b > 0:
        # If the least significant bit of b is set, add a to the result
        if b & 1:
            result += a
        
        # Double a and halve b
        a <<= 1  # Equivalent to a = a * 2
        b >>= 1  # Equivalent to b = b // 2
    
    # Apply the sign to the result
    return -result if negative_result else result

# Test case
assert multiply_int(10, 20) == 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_int(10,20)==200
    assert multiply_int(5,10)==50
    assert multiply_int(4,8)==32
