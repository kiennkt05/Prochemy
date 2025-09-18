# MBPP/80
### Completion
def tetrahedral_number(n):
    """
    Calculate the nth tetrahedral number.

    The nth tetrahedral number is given by the formula:
    T_n = n * (n + 1) * (n + 2) / 6

    Parameters:
    n (int): The index of the tetrahedral number to calculate.

    Returns:
    float: The nth tetrahedral number.
    """
    # Calculate the nth tetrahedral number using the formula
    return n * (n + 1) * (n + 2) / 6

# Test the function with the provided test case
assert tetrahedral_number(5) == 35.0

# You can add more test cases to validate the function
print(tetrahedral_number(5))  # Output: 35.0
print(tetrahedral_number(1))  # Output: 1.0
print(tetrahedral_number(2))  # Output: 4.0
print(tetrahedral_number(3))  # Output: 10.0
print(tetrahedral_number(4))  # Output: 20.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tetrahedral_number(5) == 35.0
    assert tetrahedral_number(6) == 56.0
    assert tetrahedral_number(7) == 84.0
