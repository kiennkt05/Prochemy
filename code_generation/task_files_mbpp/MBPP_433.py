# MBPP/433
### Completion
def check_greater(arr, num):
    if all(num > element for element in arr):
        return 'Yes, entered number is greater than all elements in the array'
    else:
        return 'No, entered number is less than those in the array'

# Example usage
assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
    assert check_greater([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'
