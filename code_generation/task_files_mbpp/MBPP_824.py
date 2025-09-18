# MBPP/824
### Completion
def remove_even(numbers):
    return [num for num in numbers if num % 2 != 0]

# Test the function with the provided assertion
assert remove_even([1, 3, 5, 2]) == [1, 3, 5]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_even([1,3,5,2]) == [1,3,5]
    assert remove_even([5,6,7]) == [5,7]
    assert remove_even([1,2,3,4]) == [1,3]
