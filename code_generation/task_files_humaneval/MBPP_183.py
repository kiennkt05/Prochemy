# MBPP/183
### Completion
def count_pairs(arr, n, k):
    # Create a set to store unique pairs
    pairs = set()
    
    # Convert the list to a set for O(1) lookups
    num_set = set(arr)
    
    # Iterate through each number in the array
    for num in arr:
        # Check for the two possible pairs
        if (num + k) in num_set:
            pairs.add((num, num + k))
        if (num - k) in num_set:
            pairs.add((num - k, num))
    
    # Return the count of unique pairs
    return len(pairs)

# Test the function with the provided test case
assert count_pairs([1, 5, 3, 4, 2], 5, 3) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_pairs([1, 5, 3, 4, 2], 5, 3) == 2
    assert count_pairs([8, 12, 16, 4, 0, 20], 6, 4) == 5
    assert count_pairs([2, 4, 1, 3, 4], 5, 2) == 3
