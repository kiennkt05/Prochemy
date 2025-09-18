# MBPP/664
### Completion
def average_Even(n):
    """
    Calculate the average of all even numbers from 2 to n (inclusive).
    
    Parameters:
    n (int): An even number up to which the average of even numbers is calculated.
    
    Returns:
    float: The average of even numbers from 2 to n.
    
    Raises:
    ValueError: If n is not an even number or less than 2.
    """
    # Validate input
    if n < 2 or n % 2 != 0:
        raise ValueError("Input must be an even number greater than or equal to 2.")
    
    # Generate even numbers from 2 to n
    even_numbers = list(range(2, n + 1, 2))
    
    # Calculate the average
    average = sum(even_numbers) / len(even_numbers)
    
    return average

# Test case
assert average_Even(2) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert average_Even(2) == 2
    assert average_Even(4) == 3
    assert average_Even(100) == 51
