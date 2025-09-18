# MBPP/881
### Completion
def sum_even_odd(numbers):
    first_even = None
    first_odd = None
    
    for number in numbers:
        if number % 2 == 0 and first_even is None:
            first_even = number
        elif number % 2 != 0 and first_odd is None:
            first_odd = number
        
        # Break the loop if both first even and odd are found
        if first_even is not None and first_odd is not None:
            break
    
    # If either is not found, we can return 0 for that part
    return (first_even if first_even is not None else 0) + (first_odd if first_odd is not None else 0)

# Test the function with the provided assertion
assert sum_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_even_odd([1,3,5,7,4,1,6,8])==5
    assert sum_even_odd([1,2,3,4,5,6,7,8,9,10])==3
    assert sum_even_odd([1,5,7,9,10])==11
