# MBPP/836
### Completion
def max_sub_array_sum(arr, n):
    # Initialize variables
    max_sum = float('-inf')  # Start with the lowest possible value
    current_sum = 0
    max_length = 0
    current_length = 0

    for i in range(n):
        current_sum += arr[i]
        current_length += 1
        
        # Update max_sum and max_length if we found a new maximum
        if current_sum > max_sum:
            max_sum = current_sum
            max_length = current_length
        
        # If current_sum drops below zero, reset it
        if current_sum < 0:
            current_sum = 0
            current_length = 0

    return max_length

# Test case
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3],8) == 5
    assert max_sub_array_sum([1, -2, 1, 1, -2, 1],6) == 2
    assert max_sub_array_sum([-1, -2, 3, 4, 5],5) == 3
