# MBPP/735
### Completion
def toggle_middle_bits(n):
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(n)[2:]
    
    # If the number has less than 3 bits, return it as is
    if len(binary) <= 2:
        return n
    
    # Toggle the middle bits
    middle_bits = list(binary[1:-1])  # Get the middle bits
    for i in range(len(middle_bits)):
        middle_bits[i] = '1' if middle_bits[i] == '0' else '0'  # Toggle the bit
    
    # Reconstruct the binary number
    new_binary = binary[0] + ''.join(middle_bits) + binary[-1]
    
    # Convert back to decimal
    return int(new_binary, 2)

# Test the function with the provided assertion
assert toggle_middle_bits(9) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
