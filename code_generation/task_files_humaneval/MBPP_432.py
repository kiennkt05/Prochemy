# MBPP/432
### Completion
def median_trapezium(base1, base2, height):
    """
    Calculate the median of a trapezium given the lengths of the two bases and the height.
    
    Parameters:
    base1 (float): Length of the first base of the trapezium.
    base2 (float): Length of the second base of the trapezium.
    height (float): Height of the trapezium (not used in median calculation).
    
    Returns:
    float: The median of the trapezium.
    """
    # Calculate the median using the formula
    median = (base1 + base2) / 2
    return median

# Test case
assert median_trapezium(15, 25, 35) == 20, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert median_trapezium(15,25,35)==20
    assert median_trapezium(10,20,30)==15
    assert median_trapezium(6,9,4)==7.5
