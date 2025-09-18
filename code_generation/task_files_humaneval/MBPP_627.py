# MBPP/627
### Completion
def find_First_Missing(arr, start, end):
    # Convert the array to a set for O(1) lookups
    num_set = set(arr)
    
    # Iterate through the range from start to end
    for num in range(start, end + 1):
        if num not in num_set:
            return num
    
    # If all numbers in the range are present, return the next number
    return end + 1

# Test case
assert find_First_Missing([0, 1, 2, 3], 0, 3) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_First_Missing([0,1,2,3],0,3) == 4
    assert find_First_Missing([0,1,2,6,9],0,4) == 3
    assert find_First_Missing([2,3,5,8,9],0,4) == 0
