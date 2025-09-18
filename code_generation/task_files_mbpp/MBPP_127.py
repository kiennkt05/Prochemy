# MBPP/127
### Completion
def multiply_int(a, b):
    # Handle negative numbers
    negative_result = (a < 0) ^ (b < 0)  # Result should be negative if one is negative
    a, b = abs(a), abs(b)
    
    result = 0
    for _ in range(b):
        result += a
    
    return -result if negative_result else result

# Test the function
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
