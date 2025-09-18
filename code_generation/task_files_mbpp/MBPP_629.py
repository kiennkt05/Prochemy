# MBPP/629
### Completion
def find_even_numbers(mixed_list):
    """Return a list of even numbers from the given mixed list."""
    return [num for num in mixed_list if num % 2 == 0]

# Test the function with the provided assertion
assert find_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Split([1,2,3,4,5]) == [2,4]
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert Split ([8,12,15,19]) == [8,12]
