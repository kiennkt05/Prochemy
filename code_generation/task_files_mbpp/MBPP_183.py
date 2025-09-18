# MBPP/183
### Completion
def count_pairs(arr, n, k):
    # Create a set to store the elements of the array
    elements = set(arr)
    count = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Check if there exists a pair with the given difference k
        if (num + k) in elements:
            count += 1
        if (num - k) in elements:
            count += 1
    
    # Since each pair is counted twice, we divide the count by 2
    return count // 2

# Test the function with the provided assertion
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
