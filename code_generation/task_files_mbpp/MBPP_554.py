# MBPP/554
### Completion
def find_odd_numbers(mixed_list):
    return [num for num in mixed_list if num % 2 != 0]

# Test the function with the provided assertion
assert find_odd_numbers([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Split([1,2,3,4,5,6]) == [1,3,5]
    assert Split([10,11,12,13]) == [11,13]
    assert Split([7,8,9,1]) == [7,9,1]
