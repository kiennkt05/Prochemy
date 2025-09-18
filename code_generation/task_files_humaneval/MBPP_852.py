# MBPP/852
### Completion
def remove_negs(numbers):
    """
    Remove negative numbers from a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    list: A new list containing only non-negative integers.
    """
    # Using list comprehension to filter out negative numbers
    return [num for num in numbers if num >= 0]

# Test case
assert remove_negs([1, -2, 3, -4]) == [1, 3]

# Additional test cases for verification
assert remove_negs([-1, -2, -3]) == []
assert remove_negs([0, 1, 2, 3]) == [0, 1, 2, 3]
assert remove_negs([-5, 5, -10, 10]) == [5, 10]
assert remove_negs([]) == []

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_negs([1,-2,3,-4]) == [1,3]
    assert remove_negs([1,2,3,-4]) == [1,2,3]
    assert remove_negs([4,5,-6,7,-8]) == [4,5,7]
