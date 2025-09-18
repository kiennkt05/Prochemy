# MBPP/959
### Completion
def Average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

# Test the function with the provided assertion
assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
    assert Average([4, 5, 1, 2, 9, 7, 10, 8]) == 5.75
    assert Average([1,2,3]) == 2
