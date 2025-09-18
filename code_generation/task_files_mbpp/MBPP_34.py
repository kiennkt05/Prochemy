# MBPP/34
### Completion
def find_missing(arr, n):
    # Calculate the expected sum of the first n natural numbers
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the elements in the array
    actual_sum = sum(arr)
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

# Test the function with the provided assertion
assert find_missing([1, 2, 3, 5], 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_missing([1,2,3,5],4) == 4
    assert find_missing([1,3,4,5],4) == 2
    assert find_missing([1,2,3,5,6,7],5) == 4
