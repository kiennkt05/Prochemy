# MBPP/412
### Completion
def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

# Test the function with the provided assertion
assert remove_odd([1, 2, 3]) == [2]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_odd([1,2,3]) == [2]
    assert remove_odd([2,4,6]) == [2,4,6]
    assert remove_odd([10,20,3]) == [10,20]
