# MBPP/870
### Completion
def sum_positivenum(numbers):
    return sum(filter(lambda x: x > 0, numbers))

# Test the function with the provided assertion
assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 48
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==48
    assert sum_positivenum([10,15,-14,13,-18,12,-20])==50
    assert sum_positivenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==522
