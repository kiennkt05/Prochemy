# MBPP/433
### Completion
def check_greater(arr, num):
    """
    Check if the entered number is greater than all elements in the given array.

    Parameters:
    arr (list): A list of numbers to compare against.
    num (int or float): The number to check.

    Returns:
    str: A message indicating whether the number is greater than all elements in the array.
    """
    # Check if the number is greater than all elements in the array
    for element in arr:
        if num <= element:
            return 'No, entered number is less than those in the array'
    return 'Yes, entered number is greater than all elements in the array'

# Test case
assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
    assert check_greater([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'
