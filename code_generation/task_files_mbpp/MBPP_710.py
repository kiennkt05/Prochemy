# MBPP/710
### Completion
def front_and_rear(record):
    # Access the first and last elements of the tuple
    return (record[0], record[-1])

# Test the function with the provided assertion
assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)
    assert front_and_rear((1, 2, 3, 4, 5)) == (1, 5)
    assert front_and_rear((6, 7, 8, 9, 10)) == (6, 10)
