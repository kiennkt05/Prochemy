# MBPP/221
### Completion
def first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None  # Return None if no even number is found

# Test the function with the provided assertion
assert first_even([1, 3, 5, 7, 4, 1, 6, 8]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_even ([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert first_even([2, 3, 4]) == 2
    assert first_even([5, 6, 7]) == 6
