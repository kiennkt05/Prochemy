# MBPP/886
### Completion
def sum_num(numbers):
    total = sum(numbers)  # Calculate the sum of the numbers
    count = len(numbers)  # Get the number of elements in the list
    return total / count  # Return the average

# Test the function with the provided assertion
assert sum_num((8, 2, 3, 0, 7)) == 4.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_num((8, 2, 3, 0, 7))==4.0
    assert sum_num((-10,-20,-30))==-20.0
    assert sum_num((19,15,18))==17.333333333333332
