# MBPP/420
### Completion
def cube_Sum(n):
    """
    Calculate the sum of the cubes of the first n even natural numbers.

    Parameters:
    n (int): The number of even natural numbers to consider.

    Returns:
    int: The sum of the cubes of the first n even natural numbers.
    """
    # Initialize the sum
    total_sum = 0
    
    # Loop through the first n even natural numbers
    for i in range(1, n + 1):
        even_number = 2 * i  # Calculate the ith even number
        total_sum += even_number ** 3  # Add the cube of the even number to the total sum
    
    return total_sum

# Test the function with the provided test case
assert cube_Sum(2) == 72  # 2^3 + 4^3 = 8 + 64 = 72
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800
