# MBPP/397
### Completion
def median_numbers(a, b, c):
    """
    This function takes three numbers as input and returns the median of those numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    c (float): The third number.
    
    Returns:
    float: The median of the three numbers.
    """
    # Create a list of the numbers
    numbers = [a, b, c]
    
    # Sort the list
    numbers.sort()
    
    # The median is the second element in the sorted list
    return numbers[1]

# Test case
assert median_numbers(25, 55, 65) == 55.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0
