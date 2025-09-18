# MBPP/675
### Completion
def sum_nums(a, b, lower, upper):
    """
    Adds two integers and checks if the sum falls within a specified range.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    lower (int): The lower bound of the range.
    upper (int): The upper bound of the range.
    
    Returns:
    int: 20 if the sum is within the range [lower, upper], otherwise the sum of a and b.
    """
    total = a + b  # Calculate the sum of the two integers
    # Check if the sum is within the specified range
    if lower <= total <= upper:
        return 20
    else:
        return total

# Test case
assert sum_nums(2, 10, 11, 20) == 20  # This should return 20 since 2 + 10 = 12 is within the range [11, 20]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_nums(2,10,11,20)==20
    assert sum_nums(15,17,1,10)==32
    assert sum_nums(10,15,5,30)==20
