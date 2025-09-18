# MBPP/807
### Completion
def first_odd(numbers):
    for number in numbers:
        if number % 2 != 0:  # Check if the number is odd
            return number
    return None  # Return None if no odd number is found

# Test the function with the provided assertion
assert first_odd([1, 3, 5]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_odd([1,3,5]) == 1
    assert first_odd([2,4,1,3]) == 1
    assert first_odd ([8,9,1]) == 9
