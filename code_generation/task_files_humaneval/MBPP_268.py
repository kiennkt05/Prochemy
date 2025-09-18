# MBPP/268
### Completion
def find_star_num(n):
    """
    Calculate the n-th star number using the formula:
    S(n) = 3n^2 - 3n + 1

    Parameters:
    n (int): The index of the star number to find (1-based index).

    Returns:
    int: The n-th star number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the n-th star number
    star_number = 3 * n**2 - 3 * n + 1
    return star_number

# Test the function with the provided test case
assert find_star_num(3) == 37

# Additional test cases (optional)
assert find_star_num(1) == 1
assert find_star_num(2) == 7
assert find_star_num(4) == 61

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121
