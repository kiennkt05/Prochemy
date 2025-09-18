# MBPP/436
### Completion
def neg_nos(numbers):
    """
    This function takes a list of numbers and returns a tuple of negative numbers found in the list.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    tuple: A tuple containing all negative numbers from the input list.
    """
    # Filter negative numbers using a list comprehension
    negative_numbers = tuple(num for num in numbers if num < 0)
    
    return negative_numbers

# Test the function with the provided test case
assert neg_nos([-1, 4, 5, -6]) == (-1, -6)

# If you want to see the output, you can print the result
print(neg_nos([-1, 4, 5, -6]))  # Output: (-1, -6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert neg_nos([-1,4,5,-6]) == -1,-6
    assert neg_nos([-1,-2,3,4]) == -1,-2
    assert neg_nos([-7,-6,8,9]) == -7,-6
