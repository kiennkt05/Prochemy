# MBPP/576
### Completion
def is_Sub_Array(arr1, arr2, len1, len2):
    # Loop through the first array
    for i in range(len1 - len2 + 1):
        # Check if the subarray matches
        if arr1[i:i + len2] == arr2:
            return True
    return False

# Test the function with the provided assertion
assert is_Sub_Array([1, 4, 3, 5], [1, 2], 4, 2) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2],4,2) == False
    assert is_Sub_Array([1,2,1],[1,2,1],3,3) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0],4,3) ==False
