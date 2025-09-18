# MBPP/799
### Completion
def left_Rotate(n, d):
    # Assuming n is a 32-bit integer
    d = d % 32  # To handle cases where d >= 32
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF  # Mask to keep it 32 bits

# Test the function with the provided assertion
assert left_Rotate(16, 2) == 64
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert left_Rotate(16,2) == 64
    assert left_Rotate(10,2) == 40
    assert left_Rotate(99,3) == 792
