# MBPP/303
### Completion
def count_inversions(arr):
    """
    Count the number of inversions in the array.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    
    :param arr: List of integers
    :return: Count of inversions
    """
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def solve(arr, expected_count):
    """
    Check if the count of inversions in the array is equal to the expected count.
    
    :param arr: List of integers
    :param expected_count: Expected number of inversions
    :return: True if the count of inversions matches the expected count, False otherwise
    """
    actual_count = count_inversions(arr)
    return actual_count == expected_count

# Test case
assert solve([1, 0, 2], 3) == True  # This assertion is incorrect based on the definition of inversions
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert solve([1,0,2],3) == True
    assert solve([1,2,0],3) == False
    assert solve([1,2,1],3) == True
