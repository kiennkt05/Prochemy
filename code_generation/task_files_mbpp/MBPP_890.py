# MBPP/890
### Completion
def find_Extra(arr1, arr2, n):
    # Since arr1 is longer than arr2, we can iterate through arr2
    for i in range(n):
        if arr1[i] != arr2[i]:
            return i  # Return the index of the extra element in arr1
    return n  # If no difference found, the extra element is at the end of arr1

# Example usage
assert find_Extra([1, 2, 3, 4], [1, 2, 3], 3) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Extra([1,2,3,4],[1,2,3],3) == 3
    assert find_Extra([2,4,6,8,10],[2,4,6,8],4) == 4
    assert find_Extra([1,3,5,7,9,11],[1,3,5,7,9],5) == 5
