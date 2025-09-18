# MBPP/267
### Completion
def square_Sum(n):
    """
    Calculate the sum of squares of the first n odd natural numbers.

    Parameters:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of squares of the first n odd natural numbers.
    """
    # Initialize the sum
    sum_of_squares = 0
    
    # Loop through the first n odd natural numbers
    for i in range(1, n + 1):
        odd_number = 2 * i - 1  # Calculate the i-th odd number
        sum_of_squares += odd_number ** 2  # Add its square to the sum
    
    return sum_of_squares

# Test the function with the provided test case
assert square_Sum(2) == 10  # 1^2 + 3^2 = 1 + 9 = 10

# Additional test cases for verification
assert square_Sum(1) == 1  # 1^2 = 1
assert square_Sum(3) == 35  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
assert square_Sum(4) == 84  # 1^2 + 3^2 + 5^2 + 7^2 = 1 + 9 + 25 + 49 = 84

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84
