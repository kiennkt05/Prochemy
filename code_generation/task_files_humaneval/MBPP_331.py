# MBPP/331
### Completion
def count_unset_bits(n):
    """
    Count the number of unset bits (0s) in the binary representation of a given number.

    Parameters:
    n (int): The number to count unset bits for.

    Returns:
    int: The count of unset bits in the binary representation of n.
    """
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Count the total number of bits
    total_bits = len(binary_representation)
    
    # Count the number of set bits (1s)
    set_bits = binary_representation.count('1')
    
    # Calculate unset bits (0s)
    unset_bits = total_bits - set_bits
    
    return unset_bits

# Test case
assert count_unset_bits(2) == 1  # Binary of 2 is '10', which has 1 unset bit
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_unset_bits(2) == 1
    assert count_unset_bits(4) == 2
    assert count_unset_bits(6) == 1
