# MBPP/558
### Completion
def digit_distance_nums(num1, num2):
    """
    Calculate the digit distance between two integers.
    
    Parameters:
    num1 (int): The first integer.
    num2 (int): The second integer.
    
    Returns:
    int: The absolute difference between the two integers.
    """
    # Calculate the absolute difference
    distance = abs(num1 - num2)
    return distance

# Test case
assert digit_distance_nums(1, 2) == 1  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7
