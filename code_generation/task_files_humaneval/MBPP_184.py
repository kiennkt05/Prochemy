# MBPP/184
### Completion
def greater_specificnum(numbers, specified_num):
    """
    This function checks if there are any values in the list 'numbers' 
    that are greater than 'specified_num'.
    
    Parameters:
    numbers (list): A list of numerical values.
    specified_num (int or float): The number to compare against.
    
    Returns:
    bool: True if there are values greater than specified_num, False otherwise.
    """
    # Check if any number in the list is greater than the specified number
    return any(num > specified_num for num in numbers)

# Test case
assert greater_specificnum([220, 330, 500], 200) == True

# Additional test cases for verification
assert greater_specificnum([100, 150, 200], 250) == False
assert greater_specificnum([1, 2, 3, 4, 5], 3) == True
assert greater_specificnum([], 10) == False  # Edge case: empty list
assert greater_specificnum([-10, -5, 0], -6) == True  # Negative numbers
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert greater_specificnum([220, 330, 500],200)==True
    assert greater_specificnum([12, 17, 21],20)==False
    assert greater_specificnum([1,2,3,4],10)==False
