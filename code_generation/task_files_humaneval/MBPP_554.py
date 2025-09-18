# MBPP/554
### Completion
def Split(mixed_list):
    """
    This function takes a list of integers and returns a list containing only the odd numbers.
    
    Parameters:
    mixed_list (list): A list of integers.
    
    Returns:
    list: A list of odd integers from the input list.
    """
    # Using list comprehension to filter out odd numbers
    return [num for num in mixed_list if num % 2 != 0]

# Test case
assert Split([1, 2, 3, 4, 5, 6]) == [1, 3, 5]

# Additional test cases for verification
assert Split([10, 15, 20, 25, 30]) == [15, 25]
assert Split([0, -1, -2, -3, -4]) == [-1, -3]
assert Split([]) == []  # Testing with an empty list
assert Split([2, 4, 6]) == []  # Testing with no odd numbers
assert Split([7, 8, 9, 10, 11]) == [7, 9, 11]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Split([1,2,3,4,5,6]) == [1,3,5]
    assert Split([10,11,12,13]) == [11,13]
    assert Split([7,8,9,1]) == [7,9,1]
