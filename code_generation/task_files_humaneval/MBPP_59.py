# MBPP/59
### Completion
def is_octagonal(n):
    """
    Calculate the nth octagonal number using the formula:
    O(n) = n * (3n - 2)

    Parameters:
    n (int): The position in the sequence of octagonal numbers.

    Returns:
    int: The nth octagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the nth octagonal number
    octagonal_number = n * (3 * n - 2)
    return octagonal_number

# Test the function with the provided assertion
assert is_octagonal(5) == 65

# You can add more test cases if needed
print("The 5th octagonal number is:", is_octagonal(5))  # Output: 65
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645
