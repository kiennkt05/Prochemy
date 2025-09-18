# MBPP/78
### Completion
def count_With_Odd_SetBits(n):
    """
    Count the number of integers from 1 to n that have an odd number of set bits.

    Parameters:
    n (int): The upper limit of the range (inclusive).

    Returns:
    int: The count of integers with an odd number of set bits.
    """
    count = 0
    for i in range(1, n + 1):
        # Count the number of set bits in the binary representation of i
        set_bits = bin(i).count('1')
        # Check if the count of set bits is odd
        if set_bits % 2 == 1:
            count += 1
    return count

# Test case
assert count_With_Odd_SetBits(5) == 3  # The integers are 1 (1), 3 (11), 5 (101)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_With_Odd_SetBits(5) == 3
    assert count_With_Odd_SetBits(10) == 5
    assert count_With_Odd_SetBits(15) == 8
