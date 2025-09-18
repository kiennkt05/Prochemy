# MBPP/510
### Completion
def no_of_subsequences(arr, k):
    def count_subsequences(index, current_product):
        # Base case: if we have considered all elements
        if index == len(arr):
            # Count this subsequence if the product is less than k
            return 1 if current_product < k else 0
        
        # Exclude the current element and move to the next
        count_exclude = count_subsequences(index + 1, current_product)
        
        # Include the current element and move to the next
        count_include = 0
        if current_product * arr[index] < k:  # Only include if the product remains valid
            count_include = count_subsequences(index + 1, current_product * arr[index])
        
        # Return the total count of subsequences
        return count_exclude + count_include

    # Start the recursion with the first index and a product of 1 (neutral for multiplication)
    return count_subsequences(0, 1)

# Test case
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
