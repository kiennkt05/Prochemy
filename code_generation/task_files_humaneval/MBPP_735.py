# MBPP/735
### Completion
def toggle_middle_bits(n):
    # Convert the number to binary and get its length
    binary_str = bin(n)[2:]  # Get binary representation without '0b' prefix
    length = len(binary_str)
    
    # If the number has less than 3 bits, return it as is
    if length < 3:
        return n
    
    # Create a mask to toggle the middle bits
    # The mask will have 1s in all positions except the first and last
    mask = (1 << (length - 2)) - 1  # This creates a mask of '00...011...11'
    
    # Toggle the middle bits using XOR
    # We need to shift the mask to the correct position
    middle_mask = mask << 1  # Shift left to skip the first bit
    toggled_number = n ^ middle_mask  # Toggle the middle bits
    
    return toggled_number

# Test the function with the provided test case
assert toggle_middle_bits(9) == 15  # 9 in binary is 1001, toggling middle gives 1111 which is 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
