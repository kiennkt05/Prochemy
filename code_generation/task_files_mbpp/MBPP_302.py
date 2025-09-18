# MBPP/302
### Completion
def set_Bit_Number(n):
    if n <= 0:
        return 0
    
    # Find the most significant bit
    msb = 1
    while msb <= n:
        msb <<= 1  # Shift left to find the next power of 2
    
    # The most significant bit is the last power of 2 that was less than or equal to n
    return msb >> 1  # Shift right to get the correct value

# Test the function
assert set_Bit_Number(6) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_Bit_Number(6) == 4
    assert set_Bit_Number(10) == 8
    assert set_Bit_Number(18) == 16
