# MBPP/545
### Completion
def toggle_F_and_L_bits(n):
    # Calculate the number of bits in the number
    num_bits = n.bit_length()
    
    # Create masks for the first and last bits
    first_bit_mask = 1 << (num_bits - 1)  # Mask for the first bit
    last_bit_mask = 1                    # Mask for the last bit
    
    # Toggle the first and last bits using XOR
    toggled_n = n ^ (first_bit_mask | last_bit_mask)
    
    return toggled_n

# Test the function with the provided assertion
assert toggle_F_and_L_bits(10) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert toggle_F_and_L_bits(10) == 3
    assert toggle_F_and_L_bits(15) == 6
    assert toggle_F_and_L_bits(20) == 5
