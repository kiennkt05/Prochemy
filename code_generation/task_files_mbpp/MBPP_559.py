# MBPP/559
### Completion
def max_sub_array_sum(arr, n):
    # Initialize variables
    max_sum = float('-inf')  # To store the maximum sum found
    current_sum = 0          # To store the current subarray sum

    for i in range(n):
        current_sum += arr[i]  # Add the current element to the current sum
        
        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
        
        # If current_sum drops below 0, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Test the function with the provided assertion
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
