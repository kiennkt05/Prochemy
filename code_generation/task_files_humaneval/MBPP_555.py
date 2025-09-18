# MBPP/555
### Completion
def difference(n):
    """
    Calculate the difference between the sum of cubes of the first n natural numbers
    and the sum of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    int: The difference between the sum of cubes and the sum of natural numbers.
    """
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2
    
    # Calculate the sum of cubes of the first n natural numbers
    sum_cubes = sum_n ** 2
    
    # Calculate the difference
    difference = sum_cubes - sum_n
    
    return difference

# Test the function with the provided test case
assert difference(3) == 30

# Additional test cases
assert difference(1) == 0  # 1^3 - 1 = 0
assert difference(2) == 6   # (1^3 + 2^3) - (1 + 2) = 9 - 3 = 6
assert difference(4) == 210  # (1^3 + 2^3 + 3^3 + 4^3) - (1 + 2 + 3 + 4) = 100 - 10 = 90
assert difference(5) == 600  # (1^3 + 2^3 + 3^3 + 4^3 + 5^3) - (1 + 2 + 3 + 4 + 5) = 225 - 15 = 210

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6
