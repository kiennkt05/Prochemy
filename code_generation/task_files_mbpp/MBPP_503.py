# MBPP/503
### Completion
def add_consecutive_nums(nums):
    if not nums:
        return []
    
    result = []
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum += nums[i]
        result.append(current_sum)
    
    # Prepend the first element to the result
    result.insert(0, nums[0])
    
    return result

# Test the function with the provided assertion
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
