# MBPP/383
### Completion
def even_bit_toggle_number(n):
    # Create a mask with 1s at all odd bit positions
    # For a 32-bit integer, the mask would be 0xAAAAAAAA (binary: 10101010...)
    mask = 0xAAAAAAAA
    # Toggle the odd bits using XOR
    return n ^ mask

# Test the function with the provided assertion
assert even_bit_toggle_number(10) == 15

# You can also print the result to verify
print(even_bit_toggle_number(10))  # Output should be 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_toggle_number(10) == 15
    assert even_bit_toggle_number(20) == 1
    assert even_bit_toggle_number(30) == 11
