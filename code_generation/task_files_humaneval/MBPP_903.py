# MBPP/903
### Completion
def count_Unset_Bits(n):
    total_unset_bits = 0
    
    # Iterate through each number from 1 to n
    for i in range(1, n + 1):
        # Get the binary representation of the number
        binary_representation = bin(i)[2:]  # Skip the '0b' prefix
        # Count the number of unset bits (0s)
        unset_bits = binary_representation.count('0')
        # Add to the total count of unset bits
        total_unset_bits += unset_bits
    
    return total_unset_bits

# Test case
assert count_Unset_Bits(2) == 1  # The binary representations are 1 (0 unset bits) and 10 (1 unset bit)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Unset_Bits(2) == 1
    assert count_Unset_Bits(5) == 4
    assert count_Unset_Bits(14) == 17
