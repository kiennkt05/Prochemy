# MBPP/46
### Completion
def test_distinct(numbers):
    return len(numbers) == len(set(numbers))

# Test the function with the provided assertion
assert test_distinct([1, 5, 7, 9]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_distinct([1,5,7,9]) == True
    assert test_distinct([2,4,5,5,7,9]) == False
    assert test_distinct([1,2,3]) == True
