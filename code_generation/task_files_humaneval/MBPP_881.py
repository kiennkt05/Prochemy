# MBPP/881
### Completion
def sum_even_odd(numbers):
    """
    This function finds the sum of the first even and first odd number in a given list.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The sum of the first even and first odd number. If either is not found, returns None.
    """
    first_even = None
    first_odd = None
    
    # Iterate through the list to find the first even and odd numbers
    for num in numbers:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        
        # Break early if both numbers are found
        if first_even is not None and first_odd is not None:
            break
    
    # If both even and odd numbers are found, return their sum
    if first_even is not None and first_odd is not None:
        return first_even + first_odd
    else:
        return None  # Return None if either is not found

# Test the function with the provided test case
assert sum_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 5  # 4 (even) + 1 (odd) = 5

# You can add more test cases to validate the function
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_even_odd([1,3,5,7,4,1,6,8])==5
    assert sum_even_odd([1,2,3,4,5,6,7,8,9,10])==3
    assert sum_even_odd([1,5,7,9,10])==11
