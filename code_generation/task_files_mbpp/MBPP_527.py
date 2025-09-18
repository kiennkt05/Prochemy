# MBPP/527
### Completion
def get_pairs_count(arr, n, target_sum):
    count = 0
    # Create a dictionary to store the frequency of each number
    num_count = {}
    
    for num in arr:
        # Calculate the complement that we need to find
        complement = target_sum - num
        
        # If the complement exists in the dictionary, it means we found pairs
        if complement in num_count:
            count += num_count[complement]
        
        # Update the frequency of the current number in the dictionary
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
            
    return count

# Test the function with the provided assertion
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
