# MBPP/717
### Completion
import math

def sd_calc(data):
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The standard deviation of the numbers in the list.
    """
    if len(data) == 0:
        raise ValueError("The data list cannot be empty.")
    
    # Step 1: Calculate the mean
    mean = sum(data) / len(data)
    
    # Step 2: Calculate the variance
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    
    # Step 3: Calculate the standard deviation
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

# Test case
assert sd_calc([4, 2, 5, 8, 6]) == 2.23606797749979
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sd_calc([4, 2, 5, 8, 6])== 2.23606797749979
    assert sd_calc([1,2,3,4,5,6,7])==2.160246899469287
    assert sd_calc([5,9,10,15,6,4])==4.070217029430577
