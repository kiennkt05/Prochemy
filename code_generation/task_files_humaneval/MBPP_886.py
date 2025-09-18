# MBPP/886
### Completion
def sum_num(numbers):
    """
    Calculate the average of a list or tuple of numbers.

    Parameters:
    numbers (list or tuple): A collection of numeric values.

    Returns:
    float: The average of the numbers in the collection.
    """
    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    # Calculate the length of the collection
    count = len(numbers)
    
    # Return the average (sum divided by count)
    return total_sum / count

# Test case
assert sum_num((8, 2, 3, 0, 7)) == 4.0

# Additional test cases for verification
assert sum_num([1, 2, 3, 4, 5]) == 3.0
assert sum_num((10, 20, 30)) == 20.0
assert sum_num([0, 0, 0]) == 0.0
assert sum_num((5, 15)) == 10.0

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_num((8, 2, 3, 0, 7))==4.0
    assert sum_num((-10,-20,-30))==-20.0
    assert sum_num((19,15,18))==17.333333333333332
