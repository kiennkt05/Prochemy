# MBPP/383
### Completion
def even_bit_toggle_number(n):
    # Create a mask for odd bits (0b01010101 for 8 bits)
    # This mask will toggle bits at positions 1, 3, 5, 7, ...
    mask = 0b01010101  # This is 85 in decimal for an 8-bit number
    
    # Toggle the odd bits using XOR
    result = n ^ mask
    
    return result

# Test the function with the provided test case
assert even_bit_toggle_number(10) == 15  # 10 in binary is 1010, toggling odd bits gives 1111 (15 in decimal)

# Additional test cases
print(even_bit_toggle_number(0))    # Should return 85 (0b01010101)
print(even_bit_toggle_number(85))   # Should return 0 (0b00000000)
print(even_bit_toggle_number(255))  # Should return 170 (0b10101010)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_toggle_number(10) == 15
    assert even_bit_toggle_number(20) == 1
    assert even_bit_toggle_number(30) == 11
