# MBPP/38
### Completion
def div_even_odd(numbers):
    first_even = None
    first_odd = None
    
    for num in numbers:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        
        # Break the loop if both numbers are found
        if first_even is not None and first_odd is not None:
            break
    
    # Check if both even and odd numbers were found
    if first_even is not None and first_odd is not None:
        return first_even / first_odd
    else:
        raise ValueError("The list must contain at least one even and one odd number.")

# Test the function with the provided assertion
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
