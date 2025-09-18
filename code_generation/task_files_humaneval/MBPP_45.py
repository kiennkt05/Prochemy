# MBPP/45
### Completion
from math import gcd
from functools import reduce

def get_gcd(arr):
    """
    Calculate the GCD of a list of numbers.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The GCD of the list of integers.
    """
    if not arr:
        return 0  # Return 0 if the list is empty

    # Use reduce to apply gcd across the array
    return reduce(gcd, arr)

# Test case
assert get_gcd([2, 4, 6, 8, 16]) == 2

# Additional test cases
assert get_gcd([12, 15, 21]) == 3
assert get_gcd([7, 14, 21]) == 7
assert get_gcd([5, 10, 15, 20]) == 5
assert get_gcd([100, 200, 300]) == 100
assert get_gcd([]) == 0  # Edge case: empty list

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_gcd([2, 4, 6, 8, 16]) == 2
    assert get_gcd([1, 2, 3]) == 1
    assert get_gcd([2, 4, 6, 8]) == 2 
