# MBPP/837
### Completion
def cube_Sum(n):
    """
    Calculate the sum of the cubes of the first n odd natural numbers.

    Parameters:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of the cubes of the first n odd natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        odd_number = 2 * i - 1  # Calculate the i-th odd number
        total_sum += odd_number ** 3  # Add the cube of the odd number to the total sum
    return total_sum

# Test the function with the provided test case
assert cube_Sum(2) == 28  # 1^3 + 3^3 = 1 + 27 = 28

# Additional test cases for verification
assert cube_Sum(1) == 1  # 1^3 = 1
assert cube_Sum(3) == 216  # 1^3 + 3^3 + 5^3 = 1 + 27 + 125 = 153
assert cube_Sum(4) == 728  # 1^3 + 3^3 + 5^3 + 7^3 = 1 + 27 + 125 + 343 = 496

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cube_Sum(2) == 28
    assert cube_Sum(3) == 153
    assert cube_Sum(4) == 496
