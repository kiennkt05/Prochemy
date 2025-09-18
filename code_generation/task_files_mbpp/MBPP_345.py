# MBPP/345
### Completion
def diff_consecutivenums(nums):
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]

# Test the function with the provided assertion
assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7]) == [0, 2, 1, 0, 1, 1, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7])==[0, 2, 1, 0, 1, 1, 1]
    assert diff_consecutivenums([4, 5, 8, 9, 6, 10])==[1, 3, 1, -3, 4]
    assert diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7])==[1, 1, 1, 1, 0, 0, 0, 1, 2]
