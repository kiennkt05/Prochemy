# MBPP/211
### Completion
def count_Num(n):
    """
    Count how many numbers from 0 to n (inclusive) have both the 0th and nth bits set.

    Parameters:
    n (int): The upper limit of the range to check.

    Returns:
    int: The count of numbers with both the 0th and nth bits set.
    """
    count = 0
    for num in range(n + 1):
        # Check if the 0th bit is set
        if num & 1:
            # Check if the nth bit is set
            if num & (1 << n):
                count += 1
    return count

# Test case
assert count_Num(2) == 1  # The only number is 3 (binary 11) which has both 0th and 2nd bits set.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Num(2) == 1
    assert count_Num(3) == 2
    assert count_Num(1) == 1
