# MBPP/331
### Completion
def count_unset_bits(n):
    # Get the total number of bits required to represent the number
    total_bits = n.bit_length()
    # Count the number of set bits (1s) in the binary representation
    set_bits = bin(n).count('1')
    # The number of unset bits is the total bits minus the set bits
    unset_bits = total_bits - set_bits
    return unset_bits

# Test the function with the provided assertion
assert count_unset_bits(2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_unset_bits(2) == 1
    assert count_unset_bits(4) == 2
    assert count_unset_bits(6) == 1
