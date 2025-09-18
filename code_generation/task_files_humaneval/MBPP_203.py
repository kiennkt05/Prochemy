# MBPP/203
### Completion
def hamming_distance(x: int, y: int) -> int:
    """
    Calculate the Hamming distance between two integers.

    Parameters:
    x (int): The first integer.
    y (int): The second integer.

    Returns:
    int: The Hamming distance between the two integers.
    """
    # Perform XOR operation
    xor_result = x ^ y
    
    # Count the number of 1s in the binary representation of the result
    distance = bin(xor_result).count('1')
    
    return distance

# Test case
assert hamming_distance(4, 8) == 2  # 4 is 100 in binary, 8 is 1000 in binary
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert hamming_Distance(4,8) == 2
    assert hamming_Distance(2,4) == 2
    assert hamming_Distance(1,2) == 2
