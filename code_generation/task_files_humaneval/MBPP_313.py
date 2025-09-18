# MBPP/313
### Completion
def pos_nos(numbers):
    """
    This function takes a list of numbers and returns a tuple of positive numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    tuple: A tuple containing all positive integers from the input list.
    """
    # Filter positive numbers using a list comprehension
    positive_numbers = [num for num in numbers if num > 0]
    
    # Return the positive numbers as a tuple
    return tuple(positive_numbers)

# Test the function with the provided assertion
assert pos_nos([-1, -2, 1, 2]) == (1, 2)

# You can also print the result if needed
print(pos_nos([-1, -2, 1, 2]))  # Output: (1, 2)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pos_nos([-1,-2,1,2]) == 1,2
    assert pos_nos([3,4,-5]) == 3,4
    assert pos_nos([-2,-3,1]) == 1
