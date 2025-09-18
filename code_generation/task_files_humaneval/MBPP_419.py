# MBPP/419
### Completion
def round_and_sum(numbers):
    """
    Rounds each number in the given list and returns the total sum
    multiplied by the length of the list.

    Parameters:
    numbers (list of float): A list of floating-point numbers.

    Returns:
    int: The total sum of rounded numbers multiplied by the length of the list.
    """
    # Round each number in the list
    rounded_numbers = [round(num) for num in numbers]
    
    # Calculate the total sum of the rounded numbers
    total_sum = sum(rounded_numbers)
    
    # Get the length of the list
    length_of_list = len(numbers)
    
    # Calculate the final result
    result = total_sum * length_of_list
    
    return result

# Test case
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
    assert round_and_sum([5,2,9,24.3,29])==345
    assert round_and_sum([25.0,56.7,89.2])==513
