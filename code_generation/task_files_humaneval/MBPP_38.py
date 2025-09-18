# MBPP/38
### Completion
def div_even_odd(numbers):
    # Initialize variables to store the first even and odd numbers
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
    
    # Check if both even and odd numbers were found
    if first_even is not None and first_odd is not None:
        return first_even / first_odd
    else:
        raise ValueError("The list must contain at least one even and one odd number.")

# Test case
assert div_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_even_odd([1,3,5,7,4,1,6,8])==4
    assert div_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert div_even_odd([1,5,7,9,10])==10
