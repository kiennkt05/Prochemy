# MBPP/503
### Completion
def add_consecutive_nums(nums):
    """
    This function takes a list of numbers and returns a new list where each element
    is the sum of the current element and the previous element from the input list.
    
    :param nums: List of integers
    :return: List of integers with consecutive sums
    """
    if not nums:  # Handle empty list case
        return []
    
    result = [nums[0]]  # Start with the first element
    
    for i in range(1, len(nums)):
        # Add the current number to the previous number
        result.append(result[i - 1] + nums[i])
    
    return result

# Test case
assert add_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7]) == [2, 4, 7, 8, 9, 11, 13]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[2, 4, 7, 8, 9, 11, 13]
    assert add_consecutive_nums([4, 5, 8, 9, 6, 10])==[9, 13, 17, 15, 16]
    assert add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[3, 5, 7, 9, 11, 13, 15, 17, 19]
