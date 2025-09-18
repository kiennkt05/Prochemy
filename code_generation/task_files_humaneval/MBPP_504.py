# MBPP/504
### Completion
def sum_Of_Series(n):
    """
    Calculate the sum of the cubes of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    int: The sum of the cubes of the first n natural numbers.
    """
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2
    # Return the square of that sum
    return sum_n ** 2

# Test the function with the provided test case
assert sum_Of_Series(5) == 225

# Additional test cases (optional)
print(sum_Of_Series(1))  # Should return 1
print(sum_Of_Series(2))  # Should return 9
print(sum_Of_Series(3))  # Should return 36
print(sum_Of_Series(4))  # Should return 100
print(sum_Of_Series(10)) # Should return 3025
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_Series(5) == 225
    assert sum_Of_Series(2) == 9
    assert sum_Of_Series(3) == 36
