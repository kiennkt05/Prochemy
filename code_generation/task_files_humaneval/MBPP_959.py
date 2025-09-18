# MBPP/959
### Completion
def Average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The average of the numbers in the list.
    """
    if not numbers:  # Check if the list is empty
        return 0  # Return 0 for an empty list to avoid division by zero

    total_sum = sum(numbers)  # Calculate the sum of the list
    count = len(numbers)  # Get the number of elements in the list
    average = total_sum / count  # Calculate the average
    return average  # Return the average

# Test the function with the provided test case
assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75

# You can add more test cases if needed
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
    assert Average([4, 5, 1, 2, 9, 7, 10, 8]) == 5.75
    assert Average([1,2,3]) == 2
