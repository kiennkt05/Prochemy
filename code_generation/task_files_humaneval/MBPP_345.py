# MBPP/345
### Completion
def diff_consecutivenums(nums):
    """
    Calculate the difference between consecutive numbers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list of differences between consecutive numbers.
    """
    # Initialize an empty list to store the differences
    differences = []
    
    # Iterate through the list, stopping one element before the end
    for i in range(len(nums) - 1):
        # Calculate the difference between the current and next number
        difference = nums[i + 1] - nums[i]
        # Append the difference to the list
        differences.append(difference)
    
    return differences

# Test the function with the provided test case
assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7]) == [0, 2, 1, 0, 1, 1, 1]

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7])==[0, 2, 1, 0, 1, 1, 1]
    assert diff_consecutivenums([4, 5, 8, 9, 6, 10])==[1, 3, 1, -3, 4]
    assert diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7])==[1, 1, 1, 1, 0, 0, 0, 1, 2]
