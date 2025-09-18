# MBPP/235
### Completion
def even_bit_set_number(n):
    # Create a mask with all even bits set to 1
    # For a 32-bit integer, the mask would be 0xAAAAAAAA (in hexadecimal)
    mask = 0xAAAAAAAA
    
    # Set all even bits of the number n
    result = n | mask
    
    return result

# Test case
assert even_bit_set_number(10) == 10  # 10 in binary is 1010, even bits remain unchanged
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30
