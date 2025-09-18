# MBPP/799
### Completion
def left_Rotate(n, d):
    """
    Left rotate the bits of a given number n by d positions.
    
    Parameters:
    n (int): The number to be rotated.
    d (int): The number of positions to rotate.
    
    Returns:
    int: The result of left rotating n by d positions.
    """
    # Get the number of bits in the binary representation of n
    num_bits = n.bit_length()
    
    # Normalize d to be within the range of the number of bits
    d = d % num_bits
    
    # Perform the left rotation
    rotated = (n << d) | (n >> (num_bits - d))
    
    # Mask to ensure we only keep the bits that fit in the original number
    return rotated & ((1 << num_bits) - 1)

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
