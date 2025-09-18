# MBPP/903
### Completion
def count_Unset_Bits(n):
    total_unset_bits = 0
    
    for i in range(1, n + 1):
        # Convert the number to binary and count the number of '0's
        binary_representation = bin(i)[2:]  # Get binary representation without '0b' prefix
        unset_bits_count = binary_representation.count('0')
        total_unset_bits += unset_bits_count
    
    return total_unset_bits

# Test the function with the provided assertion
assert count_Unset_Bits(2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Unset_Bits(2) == 1
    assert count_Unset_Bits(5) == 4
    assert count_Unset_Bits(14) == 17
