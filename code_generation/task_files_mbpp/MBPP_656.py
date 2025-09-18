# MBPP/656
### Completion
def find_Min_Sum(arr1, arr2, n):
    # Sort both arrays
    arr1.sort()
    arr2.sort()
    
    # Calculate the sum of absolute differences
    min_sum = sum(abs(arr1[i] - arr2[i]) for i in range(n))
    
    return min_sum

# Test the function with the provided assertion
assert find_Min_Sum([3, 2, 1], [2, 1, 3], 3) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Sum([3,2,1],[2,1,3],3) == 0
    assert find_Min_Sum([1,2,3],[4,5,6],3) == 9
    assert find_Min_Sum([4,1,8,7],[2,3,6,5],4) == 6
