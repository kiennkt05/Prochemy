# MBPP/594
### Completion
def diff_even_odd(numbers):
    first_even = None
    first_odd = None
    
    for number in numbers:
        if number % 2 == 0 and first_even is None:
            first_even = number
        elif number % 2 != 0 and first_odd is None:
            first_odd = number
        
        # Break the loop if both numbers are found
        if first_even is not None and first_odd is not None:
            break
    
    if first_even is not None and first_odd is not None:
        return first_even - first_odd
    else:
        raise ValueError("The list must contain at least one even and one odd number.")

# Example usage
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
