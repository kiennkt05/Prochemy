# MBPP/509
### Completion
def average_Odd(n):
    """
    Calculate the average of all odd numbers from 1 to n (inclusive).
    
    Parameters:
    n (int): The upper limit, which should be a positive odd number.
    
    Returns:
    float: The average of odd numbers from 1 to n.
    
    Raises:
    ValueError: If n is not a positive odd number.
    """
    # Validate input
    if n <= 0 or n % 2 == 0:
        raise ValueError("Input must be a positive odd number.")
    
    # Generate odd numbers from 1 to n
    odd_numbers = list(range(1, n + 1, 2))
    
    # Calculate the average
    average = sum(odd_numbers) / len(odd_numbers)
    
    return average

# Test case
assert average_Odd(9) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert average_Odd(9) == 5
    assert average_Odd(5) == 3
    assert average_Odd(11) == 6
