# MBPP/168
### Completion
def frequency(arr, num):
    """
    This function returns the frequency of a given number in the provided array.

    Parameters:
    arr (list): The list of numbers in which to search.
    num (int): The number whose frequency is to be found.

    Returns:
    int: The frequency of the number in the array.
    """
    return arr.count(num)

# Test case
assert frequency([1, 2, 3], 4) == 0  # 4 is not in the array, so frequency should be 0

# Additional test cases for verification
assert frequency([1, 2, 3, 1, 1], 1) == 3  # 1 appears 3 times
assert frequency([1, 2, 3], 2) == 1  # 2 appears 1 time
assert frequency([], 1) == 0  # Empty array, frequency should be 0
assert frequency([5, 5, 5, 5], 5) == 4  # 5 appears 4 times
assert frequency([1, 2, 3], 0) == 0  # 0 is not in the array, frequency should be 0

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency([1,2,3],4) == 0
    assert frequency([1,2,2,3,3,3,4],3) == 3
    assert frequency([0,1,2,3,1,2],1) == 2
