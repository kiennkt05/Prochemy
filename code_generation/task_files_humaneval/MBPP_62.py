# MBPP/62
### Completion
def smallest_num(numbers):
    """
    Function to find the smallest number in a list.
    
    Parameters:
    numbers (list): A list of numerical values.
    
    Returns:
    int/float: The smallest number in the list.
    """
    if not numbers:  # Check if the list is empty
        raise ValueError("The list cannot be empty.")
    
    return min(numbers)

# Test case
assert smallest_num([10, 20, 1, 45, 99]) == 1

# You can add more test cases to validate the function
assert smallest_num([-10, -20, -1, -45, -99]) == -99
assert smallest_num([5]) == 5
assert smallest_num([3.5, 2.1, 4.8]) == 2.1

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45
