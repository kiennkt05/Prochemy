# MBPP/258
### Completion
def count_odd(numbers):
    return len(list(filter(lambda x: x % 2 != 0, numbers)))

# Test the function with the provided assertion
assert count_odd([1, 2, 3, 5, 7, 8, 10]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_odd([1, 2, 3, 5, 7, 8, 10])==4
    assert count_odd([10,15,14,13,-18,12,-20])==2
    assert count_odd([1, 2, 4, 8, 9])==2
