# MBPP/527
### Completion
def get_pairs_count(arr, n, target_sum):
    # Dictionary to store the count of each number
    num_count = {}
    pair_count = 0
    
    # Count occurrences of each number in the array
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Iterate through the array to find pairs
    for num in arr:
        complement = target_sum - num
        
        # Check if the complement exists in the dictionary
        if complement in num_count:
            pair_count += num_count[complement]
        
        # If the complement is the same as the current number,
        # we need to decrease the count to avoid counting the pair (num, num)
        if complement == num:
            pair_count -= 1
    
    # Each pair is counted twice, so divide by 2
    return pair_count // 2

# Test case
assert get_pairs_count([1, 5, 7, -1, 5], 5, 6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_pairs_count([1, 5, 7, -1, 5], 5, 6) == 3
    assert get_pairs_count([1, 5, 7, -1], 4, 6) == 2
    assert get_pairs_count([1, 1, 1, 1], 4, 2) == 6
