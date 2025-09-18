# MBPP/472
### Completion
def check_Consecutive(nums):
    if not nums:
        return False
    
    # Sort the list to check for consecutive numbers
    nums = sorted(set(nums))  # Remove duplicates and sort
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            return False
    return True

# Test the function with the provided assertion
assert check_Consecutive([1, 2, 3, 4, 5]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False
