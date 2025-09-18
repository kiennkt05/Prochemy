# MBPP/690
### Completion
def mul_consecutive_nums(nums):
    if not nums:
        return []
    
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] * nums[i + 1])
    
    # Append the last number as it is not multiplied with any next number
    result.append(nums[-1])
    
    return result

# Test the function with the provided assertion
assert mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7]) == [1, 3, 12, 16, 20, 30, 42]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[1, 3, 12, 16, 20, 30, 42]
    assert mul_consecutive_nums([4, 5, 8, 9, 6, 10])==[20, 40, 72, 54, 60]
    assert mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 6, 12, 20, 30, 42, 56, 72, 90]
