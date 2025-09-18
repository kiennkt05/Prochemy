# MBPP/784
### Completion
def mul_even_odd(numbers):
    first_even = None
    first_odd = None
    
    # Iterate through the list to find the first even and odd numbers
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            if first_even is None:  # Store the first even number
                first_even = num
        else:  # The number is odd
            if first_odd is None:  # Store the first odd number
                first_odd = num
        
        # If both first even and odd numbers are found, we can break early
        if first_even is not None and first_odd is not None:
            break
    
    # If we found both numbers, return their product
    if first_even is not None and first_odd is not None:
        return first_even * first_odd
    else:
        # If either is not found, we can return None or raise an error
        return None  # or raise ValueError("Both even and odd numbers must be present in the list.")

# Test case
assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10
