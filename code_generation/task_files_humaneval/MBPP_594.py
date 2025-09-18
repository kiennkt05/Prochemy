# MBPP/594
### Completion
def diff_even_odd(numbers):
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
    
    # If either even or odd number is not found, we can return None or raise an error
    if first_even is None or first_odd is None:
        raise ValueError("The list must contain at least one even and one odd number.")
    
    # Calculate and return the difference
    return first_even - first_odd

# Test case
assert diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9
