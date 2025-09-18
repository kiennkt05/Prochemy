# MBPP/784
### Completion
def mul_even_odd(numbers):
    first_even = None
    first_odd = None
    
    for num in numbers:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        
        # Break the loop if both first even and odd are found
        if first_even is not None and first_odd is not None:
            break
    
    # If either even or odd number is not found, return 0
    if first_even is None or first_odd is None:
        return 0
    
    return first_even * first_odd

# Test the function with the provided assertion
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
