# MBPP/510
### Completion
def no_of_subsequences(arr, k):
    def count_subsequences(index, product):
        # If the product is already greater than or equal to k, return 0
        if product >= k:
            return 0
        # If we have considered all elements, return 1 (the empty subsequence)
        if index == len(arr):
            return 1
        
        # Count subsequences including the current element
        include_current = count_subsequences(index + 1, product * arr[index])
        # Count subsequences excluding the current element
        exclude_current = count_subsequences(index + 1, product)
        
        return include_current + exclude_current

    # Start counting from index 0 and initial product 1
    return count_subsequences(0, 1) - 1  # Subtract 1 to exclude the empty subsequence

# Test the function with the provided assertion
assert no_of_subsequences([1, 2, 3, 4], 10) == 11
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert no_of_subsequences([1,2,3,4], 10) == 11
    assert no_of_subsequences([4,8,7,2], 50) == 9
    assert no_of_subsequences([5,6,7,8], 15) == 4
