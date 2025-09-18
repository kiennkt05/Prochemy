# MBPP/545
### Completion
def toggle_F_and_L_bits(num):
    # Convert the number to binary to find the first and last bits
    if num == 0:
        return 0  # If the number is 0, both bits are 0, toggling gives 0
    
    # Find the number of bits in the binary representation
    num_bits = num.bit_length()
    
    # Create masks for the first and last bits
    first_bit_mask = 1 << (num_bits - 1)  # Mask for the first bit
    last_bit_mask = 1                     # Mask for the last bit
    
    # Toggle the first and last bits using XOR
    toggled_num = num ^ (first_bit_mask | last_bit_mask)
    
    return toggled_num

# Test case
assert toggle_F_and_L_bits(10) == 3  # 10 in binary is 1010, toggling gives 0011 which is 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert toggle_F_and_L_bits(10) == 3
    assert toggle_F_and_L_bits(15) == 6
    assert toggle_F_and_L_bits(20) == 5
