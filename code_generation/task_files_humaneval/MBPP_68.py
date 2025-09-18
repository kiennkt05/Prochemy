# MBPP/68
### Completion
def is_Monotonic(array):
    if len(array) <= 1:
        return True  # An array with 0 or 1 element is monotonic

    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            is_non_increasing = False
        elif array[i] < array[i - 1]:
            is_non_decreasing = False

    return is_non_decreasing or is_non_increasing

# Test case
assert is_Monotonic([6, 5, 4, 4]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False
