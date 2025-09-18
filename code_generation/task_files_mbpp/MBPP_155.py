# MBPP/155
### Completion
def even_bit_toggle_number(n):
    # Create a mask for even bits (0b0101010101010101... for 16 bits)
    mask = 0xAAAAAAAA  # This is the hexadecimal representation for even bits in 32 bits
    # Toggle the even bits using XOR
    return n ^ mask

# Test the function with the provided assertion
assert even_bit_toggle_number(10) == 0

# Additional test cases
print(even_bit_toggle_number(0))  # Should return 0
print(even_bit_toggle_number(1))  # Should return 2 (0b0001 -> 0b0010)
print(even_bit_toggle_number(2))  # Should return 3 (0b0010 -> 0b0011)
print(even_bit_toggle_number(15)) # Should return 1 (0b1111 -> 0b0001)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_toggle_number(10) == 0
    assert even_bit_toggle_number(20) == 30
    assert even_bit_toggle_number(30) == 20
