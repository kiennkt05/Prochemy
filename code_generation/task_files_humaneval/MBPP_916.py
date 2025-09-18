# MBPP/916
### Completion
def find_triplet_array(arr, n, target_sum):
    # Sort the array to use the two-pointer technique
    arr.sort()
    
    # Iterate through the array
    for i in range(n - 2):
        # Set the left and right pointers
        left = i + 1
        right = n - 1
        
        # Use two pointers to find the required pair
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return (arr[i], arr[left], arr[right])  # Return the triplet
            elif current_sum < target_sum:
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
    
    return None  # Return None if no triplet is found

# Test case
assert find_triplet_array([1, 4, 45, 6, 10, 8], 6, 22) == (4, 10, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_triplet_array([1, 4, 45, 6, 10, 8], 6, 22) == (4, 10, 8)
    assert find_triplet_array([12, 3, 5, 2, 6, 9], 6, 24) == (12, 3, 9)
    assert find_triplet_array([1, 2, 3, 4, 5], 5, 9) == (1, 3, 5)
